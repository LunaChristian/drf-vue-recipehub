from rest_framework.views import APIView
from django.http import HttpResponse

# Create your views here.
class Class_Ejemplo_View(APIView):
    def get(self, request):
        return HttpResponse("Texto de ejemplo")

    def post(self, request):
        return HttpResponse("Salida con el método POST")

    def put(self, request):
        return HttpResponse("Salida con el método PUT")

    def delete(self, request):
        return HttpResponse("Salida con el método DELETE")
    
class Class_Ejemplo_View_Parametros(APIView):
    def get(self, request, id: int):
        return HttpResponse(f"Salida con el método GET | parametro={id}")

    def post(self, request, id: int):
        return HttpResponse(f"Salida con el método POST | parametro={id}")

    def put(self, request, id: int):
        return HttpResponse(f"Salida con el método PUT | parametro={id}")

    def delete(self, request, id: int):
        return HttpResponse(f"Salida con el método DELETE | parametro={id}")