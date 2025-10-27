from http import HTTPStatus

from django.http import Http404, JsonResponse
from rest_framework.views import APIView

from .models import *

# Create your views here.

class Clase_1(APIView):
    
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