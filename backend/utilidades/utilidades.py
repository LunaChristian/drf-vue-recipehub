import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(html: str, subject: str, to: str) -> None:
    """
    Envía un correo electrónico en formato HTML.

    Args:
        html (str): contenido HTML del correo.
        subject (str): asunto del correo.
        to (str): destinatario.
    """
    content = MIMEMultipart("alternative")
    content["Subject"] = subject
    content["From"] = os.getenv("SMTP_USER")
    content["To"] = to
    content.attach(MIMEText(html, "html"))
    
    try:
        server = smtplib.SMTP(os.getenv("SMTP_SERVER"), os.getenv("SMTP_PORT"))
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
        server.sendmail(os.getenv("SMTP_USER"), to, content.as_string())
        server.quit()
        
    except smtplib.SMTPResponseException as e:
        print(f"Error al enviar: {e.smtp_code} - {e.smtp_error}")

def build_contact_email(contacto) -> str:
    """
    Genera el HTML para el correo de contacto.

    Args:
        contacto (Contacto): instancia del modelo Contacto.

    Returns:
        str: HTML formateado con los datos del contacto.
    """
    return f"""
        <h1>Nuevo contacto recibido</h1>
        <ul>
            <li><b>Nombre:</b> {contacto.nombre}</li>
            <li><b>Email:</b> {contacto.correo}</li>
            <li><b>Teléfono:</b> {contacto.telefono}</li>
            <li><b>Mensaje:</b> {contacto.mensaje}</li>
        </ul>
    """

def build_singup_email(userdata, url_token: str) -> str:
    """
    Genera el HTML para la confirmacion de registro.

    Args:
        contacto (userdata): instancia del modelo User.

    Returns:
        str: HTML formateado con los datos del contacto.
    """
    return f"""
        <h1>Verificacion nuevo registro</h1>
        <ul>
            <li><b>Nombre:</b> {userdata.username}</li>
            <li><b>Email:</b> {userdata.email}</li>
            <li><b>Url de verificación:</b> <a href="{url_token}">{url_token}</a></li>
        </ul>
    """
