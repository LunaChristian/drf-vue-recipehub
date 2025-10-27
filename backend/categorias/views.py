from http import HTTPStatus

from django.http import Http404, HttpResponse, JsonResponse
from django.utils.text import slugify
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Categoria
from .serializers import CategoriaSerializer
from recetas.models import Receta


# Create your views here.
class Class_Categoria_View(APIView):
   
    def get(self, request):
        data = Categoria.objects.order_by('-id').all()
        data_json = CategoriaSerializer(data, many=True)
        return JsonResponse({"data":data_json.data}, status=HTTPStatus.OK)
    
    def post(self, request):
        
        required_fields = ["titulo"] 
        for field in required_fields:
            if not request.data.get(field):
                return JsonResponse(
                    {"estado": "error", "mensaje": f"El campo '{field}' es obligatorio"},
                    status=HTTPStatus.BAD_REQUEST,
                )
                
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
        
    def put(self, request, id):
        
        if request.data.get('titulo')==None or not request.data['titulo']:
            return JsonResponse({"estado":"error", "mensaje":"campo obligatorio"}, status=HTTPStatus.BAD_REQUEST)
        try:
            data = Categoria.objects.filter(pk=id).get()
            Categoria.objects.filter(pk=id).update(titulo=request.data['titulo'], slug=slugify(request.data.get('titulo')))
            return JsonResponse({"estado":"ok", "mensaje":"modificacion exitosa"}, status=HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
        
    def delete(sefl, request, id):
        
        try:
            data = Categoria.objects.filter(pk=id).get()
            
        except Categoria.DoesNotExist:
            raise Http404
        
        if Receta.objects.filter(categoria_id=id).exists():
            return JsonResponse({"estado":"error", "mensaje":"Error al eliminar Categoria"}, status=HTTPStatus.BAD_REQUEST)

        Categoria.objects.filter(pk=id).delete()
        return JsonResponse({"estado":"ok", "mensaje":"eliminacion exitosa"}, status=HTTPStatus.OK)