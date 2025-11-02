import os
from datetime import datetime
from http import HTTPStatus

from django.http import Http404, JsonResponse
from django.core.files.storage import FileSystemStorage
from django.utils.dateformat import DateFormat
from django.contrib.auth.models import User
from rest_framework.views import APIView

from recetas.models import Receta
from recetas.serializers import RecetaSerializer
from categorias.models import Categoria
from seguridad.decorators import login_successful



class RecetaHelperView(APIView):
    @login_successful()
    def get(self, request, id):
        try:
            existe = User.objects.filter(pk=id).get()
        except User.DoesNotExist:
            return JsonResponse(
                {"estado":"error", "mensaje":"Error inesperado [metodo GET en recetas_helper]"},
                status=HTTPStatus.BAD_REQUEST,
            )
        data = Receta.objects.filter(user_id=id).order_by('-id').all()
        datos_json = RecetaSerializer(data, many=True)
        return JsonResponse({"data":datos_json.data}, status=HTTPStatus.OK)
    
class ImgEditorHelperView(APIView):
    @login_successful()
    def post(self, request):
        
        # Validaciones
        required_fields = ['id']
        for field in required_fields:
            if not request.data.get(field):
                return JsonResponse(
                    {"estado": "error", "mensaje": f"El campo '{field}' es obligatorio"},
                    status=HTTPStatus.BAD_REQUEST,
                )
            
        try:
            existe=Receta.objects.filter(pk=request.data["id"]).get()
            anterior = existe.foto
        except Receta.DoesNotExist:
            return JsonResponse({"estado":"error", "mensaje":"La receta informada no existe en la base de datos"}, status=HTTPStatus.BAD_REQUEST)
        
        fs = FileSystemStorage()
        try:
            foto = f"{datetime.timestamp(datetime.now())}{os.path.splitext(str(request.FILES['foto']))[1]}"
        except Exception as e:
            return JsonResponse({"estado":"error", "mensaje":"Debe adjuntar una foto en el campo foto"}, status=HTTPStatus.BAD_REQUEST)
        
        if request.FILES["foto"].content_type=="image/jpeg" or request.FILES["foto"].content_type=="image/png":
            try:
                fs.save(f"recetas/{foto}", request.FILES['foto'])
                fs.url( request.FILES['foto'])
            except Exception as e:
                return JsonResponse({"estado":"error", "mensaje":"Se produjo un error al intentar subir el archivo"}, status=HTTPStatus.BAD_REQUEST)
            
            try:
                Receta.objects.filter(id=request.data["id"]).update(foto=foto)
                os.remove(f"./uploads/recetas/{anterior}")
                return JsonResponse({"estado":"ok", "mensaje":"Se modifica el registro exitosamente"}, status=HTTPStatus.OK)
            except Exception as e:
                return JsonResponse({"estado":"error", "mensaje":"Ocurrió un error inesperado"}, status=HTTPStatus.BAD_REQUEST)
        else:
            return JsonResponse({"estado":"error", "mensaje":"La foto sólo puede ser PNG y JPG"}, status=HTTPStatus.BAD_REQUEST)
