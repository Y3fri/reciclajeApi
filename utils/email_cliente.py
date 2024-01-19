import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_registration_email(email,nickname):        
            smtp_server = "smtp.gmail.com" 
            smtp_port = 587
            smtp_username = "yeferguzman11@gmail.com"
            smtp_password = "kepm prma yrip umuk"
            
            subject = "Registro exitoso"
            body =f"""
        <html>
        <head>
            <style>
                body {{
                    text-align: center;
                    font-family: 'Arial', sans-serif;
                    background-color: #f0f0f0;
                }}
                .container {{
                    width: 50%;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Bienvenido a *****</h1>
                <p>Haz un mundo mejor y reclica con nosotros.Este es tu nickname</p>
                <p><strong>Nickname:</strong> {nickname}</p>                
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
            message.attach(MIMEText(body, "plain"))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                
                server.sendmail(sender_email, receiver_email, message.as_string())
