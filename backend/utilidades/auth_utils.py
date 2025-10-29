from django.contrib.auth.models import User
from seguridad.models import UsersMetada
from django.http import Http404

def verify_user_by_token(token: str) -> User:
    """
    Verifica un usuario por token de registro.
    Limpia el token y activa el usuario si es válido.

    Args:
        token (str): token único de verificación.

    Returns:
        User: instancia del usuario activado.

    Raises:
        Http404: si el token no existe o el usuario ya está activo.
    """
    try:
        metadata = UsersMetada.objects.select_related("user").get(token=token, user__is_active=0)
        metadata.token = ""
        metadata.save()
        metadata.user.is_active = True
        metadata.user.save()
        
        return metadata.user
    
    except UsersMetada.DoesNotExist:
        raise Http404("Token inválido o usuario ya verificado")