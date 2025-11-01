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