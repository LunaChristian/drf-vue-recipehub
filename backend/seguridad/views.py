from http import HTTPStatus
from datetime import datetime, timedelta, timezone

from django.http import Http404, HttpResponseRedirect, JsonResponse
from rest_framework.views import APIView

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import uuid, os
from dotenv import load_dotenv
from jose import jwt
from django.conf import settings
import time

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
        
class Login(APIView):
    def post(self, request):        
        # Validaciones del curso
        
        """ 
        if request.data.get("correo")==None or not request.data.get("correo"):
            return JsonResponse(
                    {"estado": "error", "mensaje": "El campo correo es obligatorio"},
                    status=HTTPStatus.BAD_REQUEST,
                )
        
        if request.data.get("password")==None or not request.data.get("password"):
            return JsonResponse(
                    {"estado": "error", "mensaje": "El campo password es obligatorio"},
                    status=HTTPStatus.BAD_REQUEST,
                )

        try:
            user = User.objects.filter(email=request.data["correo"]).get()
        except User.DoesNotExist:
            return JsonResponse({"estado": "error", "mensaje": "Recurso no disponible"}, status=HTTPStatus.NOT_FOUND,)   

        auth = authenticate(request, username=request.data.get("correo"), password=request.data.get("password"))
        if auth is not None:
            fecha = datetime.now()
            despues = fecha + timedelta(days=1)
            fecha_numero = int(datetime.timestamp(despues))
            payload = {"id":user.id, "ISS":os.getenv('BASE_URL'), "iat":int(time.time()), "exp": int(fecha_numero)}
            
            try: 
                token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS512')
                return JsonResponse(
                    {"id": user.id, "nombre": user.first_name, "token":token})
            except Exception as e:
                return JsonResponse(
                    {"estado": "error", "mensaje": "Error inesperado"},
                    status=HTTPStatus.BAD_REQUEST,
                )
        else:
            return JsonResponse(
                    {"estado": "error", "mensaje": "Error en las credenciales"},
                    status=HTTPStatus.BAD_REQUEST,
                ) """

        # Validaciones propias
        required_fields = ["correo", "password"]
        for field in required_fields:
            if not request.data.get(field):
                return JsonResponse(
                    {"estado": "error", "mensaje": f"El campo '{field}' es obligatorio"},
                    status=HTTPStatus.BAD_REQUEST,
                )

        correo = request.data.get('correo')
        password = request.data.get('password')

        auth = authenticate(request, username=correo, password=password)
     
        if auth is None:
            return JsonResponse(
                {"estado": "error", "mensaje": "Error en las credenciales"},
                status=HTTPStatus.BAD_REQUEST,
            )

        # ✅ Aquí puedes continuar con login(auth) o devolver token/jwt
        exp_time = datetime.now(timezone.utc) + timedelta(days=1)
        
        payload = {
            "id": auth.id,
            "iss": os.getenv("BASE_URL"),
            "iat": int(time.time()),
            "exp": int(exp_time.timestamp()),
        }
        
        try:
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS512")
            return JsonResponse(
                {
                    "id": auth.id,
                    "nombre": auth.first_name,
                    "token": token,
                },
                status=HTTPStatus.OK,
            )
        except Exception:
            return JsonResponse(
                {"estado": "error", "mensaje": "Error inesperado"},
                status=HTTPStatus.BAD_REQUEST,
            )