from http import HTTPStatus
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404, HttpResponse, JsonResponse
from .models import Categoria
from .serializers import CategoriaSerializer

# Create your views here.
class Class_Categoria_View(APIView):
   
    def get(self, request):
        data = Categoria.objects.order_by('-id').all()
        data_json = CategoriaSerializer(data, many=True)
        return JsonResponse({"data":data_json.data}, status=HTTPStatus.OK)
    
    def post(self, request):
        try:
            Categoria.objects.create(titulo=request.data['titulo'])
            return JsonResponse({"estado":"ok", "mensaje":"registro exitoso"}, status=HTTPStatus.CREATED)
        except Exception as e:
            print(f'error: {e}')
            raise Http404
    
class Class_Categoria_View2(APIView):   
    def get(self, request, id):
        try:
            data = Categoria.objects.filter(pk=id).get()
            return JsonResponse({"data": {"id": data.id, "titulo":data.titulo, "slug":data.slug}}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404