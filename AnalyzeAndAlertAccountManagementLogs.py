import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
sender_email = "touhidrevenger1997@gmail.com"
app_password = "lfyq rsus mpkl vnuk"  # This is the app password you generated
recipient_email = "topcoder2002@gmail.com"

# Create the email
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = "Test Email"

# Email body
body = "This is an automatically sent email using an App Password."
message.attach(MIMEText(body, "plain"))

# Connect to the Gmail SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Secure the connection
    server.login(sender_email, app_password)  # Login using the app password
    text = message.as_string()  # Convert the message to a string
    server.sendmail(sender_email, recipient_email, text)  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()  # Close the connection
