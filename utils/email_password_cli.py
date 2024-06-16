import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_reset_password_email(email: str, verification_code: str):
    
    smtp_server = 'smtp.gmail.com'  
    smtp_port = 587  

    
    sender_email = 'yeferguzman11@gmail.com'  
    sender_password = 'kepm prma yrip umuk' 

    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = 'Código de verificación para restablecimiento de contraseña'

    
    message = f"""
    Hola,

    Hemos recibido una solicitud para restablecer la contraseña de tu cuenta.

    Utiliza el siguiente código de verificación para proceder con el cambio de contraseña:
    Código de verificación: {verification_code}

    Este código es válido por 15 minutos. Si no solicitaste este cambio, puedes ignorar este mensaje.

    Atentamente,
    Tu aplicación
    """

    msg.attach(MIMEText(message, 'plain'))

    
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(sender_email, sender_password)  
        server.sendmail(sender_email, email, msg.as_string()) 

    print(f"Correo electrónico enviado a {email} con el código de verificación.")
