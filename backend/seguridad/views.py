from http import HTTPStatus

from django.http import Http404, HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView

from django.contrib.auth.models import User
import uuid, os
from dotenv import load_dotenv

from utilidades.utilidades import build_singup_email, send_email
from utilidades.auth_utils import verify_user_by_token
from .models import UsersMetada


# Create your views here.

class Seguridad(APIView):
    
    def post(self, request):
        required_fields = ["nombre", "correo", "password"] 
        for field in required_fields:
            if not request.data.get(field):
                return JsonResponse(
                    {"estado": "error", "mensaje": f"El campo '{field}' es obligatorio"},
                    status=HTTPStatus.BAD_REQUEST,
                )
                
        if User.objects.filter(email=request.data["correo"]).exists():
            return JsonResponse({"estado":"error", "mensaje":"Error: el correo ya existe"}, status=HTTPStatus.BAD_REQUEST)
        
        token = uuid.uuid4()
        url_token = f"{os.getenv("BASE_URL")}api/v1/seguridad/verificacion/{token}"
        
        try:
            user = User.objects.create_user(
                username=request.data["nombre"],
                password=request.data["password"],
                email=request.data["correo"],
                first_name="",
                last_name="",
                is_active=0
            )
            
            UsersMetada.objects.create(user_id=user.id, token=token)
            html_content = build_singup_email(user, url_token)
            
            send_email(html_content, "Verificacion de registro", user.email)
            
        except Exception as e:
            raise Http404
        
        return JsonResponse({"estado":"ok", "mensaje":"registro exitoso"}, status=HTTPStatus.CREATED)
    
class Verificacion(APIView):
    def get(self, request, token):
        if not token:
            return JsonResponse({"estado":"error", "mensaje":"Recurso no disponible"}, status=404)
        
        try:
            verify_user_by_token(token)
            return HttpResponseRedirect(os.getenv("BASE_URL_FRONTEND"))
        except Exception as e:
            return JsonResponse({"estado": "error", "mensaje": str(e)}, status=404)