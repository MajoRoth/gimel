import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(name, phone, email, message):
    port = 465  # For SSL
    password = "********"
    sender_email = "gimel1987dev@gmail.com"
    receiver_email = "gimel1987dev@gmail.com"

    msg = MIMEMultipart('alternative')
    msg['Subject'] = name
    msg['From'] = sender_email
    msg['To'] = receiver_email

    text = "phone: " + phone + '\n' + "mail: " + email + '\n' + '\n' + 'message: ' + message
    html = """\
    <html>
      <head></head>
      <body>
        <p>
        {}
        </p>
      </body>
    </html>
    """.format(text)

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, msg.as_string())
