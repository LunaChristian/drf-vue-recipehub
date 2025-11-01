from functools import wraps
from http import HTTPStatus
import time

from django.conf import settings
from django.http import JsonResponse
from jose import jwt

#La siguiente linea importa librerias para el codigo corregido/optimizado
from jose import JWTError, ExpiredSignatureError

def login_successful():
    def metodo(func):
        @wraps(func)
        def _decorator(request, *args, **kwargs):
            req = args[0]
            if not req.headers.get('Authorization') or req.headers.get('Authorization')==None:
                return JsonResponse({"estado":"error", "mensaje":"No autorizado"}, status=HTTPStatus.UNAUTHORIZED)
            header = req.headers.get('Authorization').split(" ")
            try:
                resuelto=jwt.decode(header[1], settings.SECRET_KEY, algorithms=['HS512'])
                print(f"Debug payload (token resuelto) {resuelto}")
            except Exception as e:
                return JsonResponse({"estado":"error", "mensaje":"No autorizado"}, status=HTTPStatus.UNAUTHORIZED)
            
            if int(resuelto["exp"])>int(time.time()):
                return func(request, *args, **kwargs)
            else:
                return JsonResponse({"estado":"error", "mensaje":"No autorizado"}, status=HTTPStatus.UNAUTHORIZED)
        return _decorator
    return metodo

# Decorador optimizado

#def login_successful(func):
    """
    Decorador que valida la autenticación por JWT en vistas de Django.
    Requiere un header 'Authorization: Bearer <token>'.
    """
""" 
    @wraps(func)
    def _decorator(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return JsonResponse(
                {"estado": "error", "mensaje": "No autorizado"},
                status=HTTPStatus.UNAUTHORIZED
            )

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,  # ideal: usar settings.JWT_SECRET
                algorithms=["HS512"],
                options={"verify_exp": True}  # valida exp automáticamente
            )
        except ExpiredSignatureError:
            return JsonResponse(
                {"estado": "error", "mensaje": "Token expirado"},
                status=HTTPStatus.UNAUTHORIZED
            )
        except JWTError:
            return JsonResponse(
                {"estado": "error", "mensaje": "Token inválido"},
                status=HTTPStatus.UNAUTHORIZED
            )

        # Si todo OK -> pasa a la vista
        return func(request, *args, **kwargs)

    return _decorator """