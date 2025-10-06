from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse, JsonResponse
from .models import Categoria
from .serializers import CategoriaSerializer

# Create your views here.
class Class_Categoria_View(APIView):
    def post(self, request):
        pass
   
    def get(self, request):
        data = Categoria.objects.order_by('-id').all()
        data_json = CategoriaSerializer(data, many=False)
        return JsonResponse(data_json.data)