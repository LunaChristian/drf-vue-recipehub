from datetime import datetime
from http import HTTPStatus
import os
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse, JsonResponse

from categorias.models import Categoria

from .serializers import RecetaSerializer
from .models import Receta
from django.utils.text import slugify
from django.utils.dateformat import DateFormat
from dotenv import load_dotenv

# Create your views here.
class Class_Receta_View(APIView):
   
    def get(self, request):
        data = Receta.objects.order_by('-id').all()
        data_json = RecetaSerializer(data, many=True)
        return JsonResponse({"data":data_json.data}, status=HTTPStatus.OK)
    
    def post(self, request):
        required_fields = ["titulo_receta", "tiempo", "descripcion", "categoria_id"]
        for field in required_fields:
            if not request.data.get(field):
                return JsonResponse(
                    {"estado": "error", "mensaje": f"El campo '{field}' es obligatorio"},
                    status=HTTPStatus.BAD_REQUEST,
                )
        
        try:
            Categoria.objects.filter(pk=request.data["categoria_id"]).get()
        except Categoria.DoesNotExist:
            return JsonResponse(
                {"estado":"error", "mensaje":"La categoria no existe"},
                status=HTTPStatus.BAD_REQUEST,
            )
        
        if Receta.objects.filter(titulo_receta=request.data.get("titulo_receta")).exists():
            return JsonResponse(
                {
                    "estado":"error",
                    "mensaje":f"Ya existe otro registro con el nombre '{request.data['titulo_receta']}'"
                }, 
                status=HTTPStatus.BAD_REQUEST,
            )
        
        try:
            Receta.objects.create(
                titulo_receta=request.data['titulo_receta'],
                tiempo = request.data['tiempo'],
                descripcion = request.data['descripcion'],
                categoria_id = request.data['categoria_id'],
                fecha = datetime.now(),
                foto = "sss"            
                )
            return JsonResponse({"estado":"ok", "mensaje":"registro exitoso"}, status=HTTPStatus.CREATED)
        except Exception as e:
            print(f'error: {e}')
            raise Http404
    
class Class_Receta_View2(APIView):   
    
    def get(self, request, id):
        try:
            data = Receta.objects.filter(pk=id).get()
            
            return JsonResponse(
                {"data":
                    {
                        "id": data.id,
                        "titulo_receta": data.titulo_receta,
                        "slug": data.slug,
                        "tiempo": data.tiempo,
                        "descripcion": data.descripcion,
                        "fecha": DateFormat(data.fecha).format('d/m/Y'),
                        "categoria": data.categoria.titulo,
                        "categoria_id": data.categoria_id,
                        "imagen": f"{os.getenv("BASE_URL")}uploads/recetas/{data.foto}"
                    }
                }, status=HTTPStatus.OK)
            
        except Receta.DoesNotExist:
            raise Http404