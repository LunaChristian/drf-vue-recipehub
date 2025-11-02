from datetime import datetime
from http import HTTPStatus

from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from utilidades import utilidades

from .models import Contacto

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class Contactos_1(APIView):
    @swagger_auto_schema(
        operation_descripcion="Endpoint para Contacto",
        responses={
            200:"Success",
            400:"Bad request"
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name':openapi.Schema(type=openapi.TYPE_STRING, description="Nombre"),
                'correo':openapi.Schema(type=openapi.TYPE_STRING, description="E-Mail"),
                'telefono':openapi.Schema(type=openapi.TYPE_STRING, description="Teléfono"),
                'mensaje':openapi.Schema(type=openapi.TYPE_STRING, description="Mensaje")  
            },
            required=['name', 'correo', 'telefono', 'mensaje']
        )
    )
    
    def post(self, request):
        required_fields = ["nombre", "correo", "telefono", "mensaje"]
        for field in required_fields:
            if not request.data.get(field):
                return JsonResponse(
                    {"estado": "error", "mensaje": f"El campo '{field}' es obligatorio"},
                    status=HTTPStatus.BAD_REQUEST,
                )
        
        try:
            contacto = Contacto.objects.create(
                name=request.data['nombre'],
                correo=request.data['correo'],
                telefono=request.data['telefono'],
                mensaje=request.data['mensaje'], 
            )
            
            html = utilidades.build_contact_email(contacto)
            utilidades.send_email(html, "Nuevo contacto", contacto.correo)
            
        except Exception as e:
            return JsonResponse(
                {"estado": "error", "mensaje": f"Error en el registro de contacto: {str(e)}"},
                status=HTTPStatus.BAD_REQUEST,
            )  
        return JsonResponse({"estado":"ok", "mensaje":"Registro de contacto exitoso"}, status=HTTPStatus.OK)
