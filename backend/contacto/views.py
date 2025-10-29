from datetime import datetime
from http import HTTPStatus

from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from utilidades import utilidades

from .models import Contacto


# Create your views here.

class Contacto_View(APIView):
    
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
                nombre=request.data['nombre'],
                correo=request.data['correo'],
                telefono=request.data['telefono'],
                mensaje=request.data['mensaje'],
                fecha=datetime.now(),
                )
            
            html = utilidades.build_contact_email(contacto)
            utilidades.send_email(html, "Nuevo contacto", contacto.correo)
            
            return JsonResponse({"estado":"ok", "mensaje":"registro exitoso"}, status=HTTPStatus.CREATED)
        except Exception as e:
            raise Http404
    
