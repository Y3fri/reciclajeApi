import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_recogida(email, idRecogida):        
            smtp_server = "smtp.gmail.com" 
            smtp_port = 587
            smtp_username = "yeferguzman11@gmail.com"
            smtp_password = "kepm prma yrip umuk"
            
       
            subject = "Nueva Recogida de Materiales Registrada"
            body = f"""
            <html>
            <head>
                <style>
                    body {{
                        font-family: 'Arial', sans-serif;
                        background-color: #f0f0f0;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }}
                    .container {{
                        background-color: #ffffff;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                        text-align: center;
                        width: 80%;
                        max-width: 600px;
                    }}
                    .header {{
                        background-color: #4CAF50;
                        color: white;
                        padding: 10px 0;
                        border-radius: 10px 10px 0 0;
                    }}
                    .content {{
                        padding: 20px;
                    }}
                    .footer {{
                        margin-top: 20px;
                        font-size: 12px;
                        color: #888;
                    }}
                    .button {{
                        background-color: #4CAF50;
                        color: white;
                        padding: 10px 20px;
                        text-decoration: none;
                        border-radius: 5px;
                        display: inline-block;
                        margin-top: 20px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>Nueva Recogida de Materiales</h1>
                    </div>
                    <div class="content">
                        <p>Se ha registrado una nueva recogida de materiales.</p>
                        <p><strong>ID de Recogida:</strong> {idRecogida}</p>
                        <p>Por favor, revisa los detalles en el sistema de administración.</p>
                        <a href="https://www.google.com/?hl=es" class="button">Ver Recogida</a>
                    </div>
                    <div class="footer">
                        <p>Este es un mensaje automático, por favor no responder a este correo.</p>
                        <p>&copy; 2024 Tu Empresa. Todos los derechos reservados.</p>
                    </div>
                </div>
            </body>
            </html>
            """
            sender_email = "yeferguzman11@gmail.com"
            receiver_email = email
        
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "html"))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                
                server.sendmail(sender_email, receiver_email, message.as_string())
