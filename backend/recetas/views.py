from http import HTTPStatus
import os
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse, JsonResponse

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
    
    """def post(self, request):
        if request.data.get('titulo')==None or not request.data['titulo']:
            return JsonResponse({"estado":"error", "mensaje":"campo obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        try:
            Receta.objects.create(titulo=request.data['titulo'])
            return JsonResponse({"estado":"ok", "mensaje":"registro exitoso"}, status=HTTPStatus.CREATED)
        except Exception as e:
            print(f'error: {e}')
            raise Http404 """
    
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