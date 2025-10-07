from http import HTTPStatus
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse, JsonResponse

from .serializers import RecetaSerializer
from .models import Receta
from django.utils.text import slugify

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
    
    pass