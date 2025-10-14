import os
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView


# Create your views here.
class Class_Ejemplo_View(APIView):
    def get(self, request):
        #Respuesta con HttpResponse
        #return HttpResponse(f"Salida con el método GET | id={request.GET.get('id', None)} | slug={request.GET.get('slug', None)}")

        #Respuesta con Response (DRF)
        """ return Response({
            "estado": "ok",
            "mensaje": f"Salida con el método GET | id={request.GET.get('id', None)} | slug={request.GET.get('slug', None)}"
        }) """
        
        #Respuesta con JsonResponse
        return JsonResponse({
            "estado": "ok",
            "mensaje": f"Salida con el método GET | id={request.GET.get('id', None)} | slug={request.GET.get('slug', None)}"
        })
        
    def post(self, request):
        #Respuesta con HttpResponse
        #return HttpResponse("Salida con el método POST")
        
        #Respuesta con JsonResponse
        correo = request.data.get('correo', None)
        password = request.data.get('password', None)
        
        if correo == None or password == None:
            raise Http404
        return JsonResponse({
            "estado": "ok",
            "mensaje": f"Salida con el metodo GET | correo={correo} | password={password}"
        })

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
    
class Class_Ejemplo_Upload(APIView):
    def post(self, request):
        """
        fs = FileSystemStorage()
        fecha = datetime.now()
        foto = f"{datetime.timestamp(fecha)}{os.path.splitext(str(request.FILES['file']))[1]}"
        #Para la siguiente linea sera en fs guardar lo que reciba por el request.
        #En este caso esta recibiendo un archivo llamado 'file'
        fs.save(f"ejemplo/{foto}", request.FILES['file'])  #Sintaxis .save(filename, file)
        fs.url(request.FILES['file'])
        return JsonResponse({
            "estado": "ok",
            "mensaje": "Subido correctamente"
        })
        """
        
        try:
            file = request.FILES["file"]

            # Generar nombre único. Ver tambien UUID
            timestamp = int(datetime.now().timestamp())
            
            # Obtener el nombre y la extension con splitext. En este caso se descarta el nombre (variable _ )
            _, extension = os.path.splitext(file.name)
            filename = f"{timestamp}{extension}"    

            # Guardar archivo
            fs = FileSystemStorage(location="upload/ejemplo")
            fs.save(filename, file)

            return JsonResponse({
                "estado": "ok",
                "mensaje": "Archivo subido correctamente",
                "archivo": filename
            })
            
        except Exception as e:
            return JsonResponse({
                "estado": "error",
                "mensaje": str(e)
            }, status=400)