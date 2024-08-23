import pandas as pd
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define the path to the log file
log_file_path = "C:\\Logs\\AccountManagementLogs.csv"

# Email credentials
sender_email = "sender_email@gmail.com"
app_password = "your_16_character_code"  # This is the app password generated from gmail
recipient_email = "recipient_email@gmail.com"

# Function to send an email alert
def send_alert(subject, body):
    # Create the email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # Attach the email body
    message.attach(MIMEText(body, "plain"))

    # Connect to the Gmail SMTP server and send the email
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

# Check if the log file exists
if not os.path.exists(log_file_path):
    print("Log file not found. Please ensure the logs were collected successfully.")
else:
    # Load the CSV file into a pandas DataFrame
    logs = pd.read_csv(log_file_path)

    # Analyze the logs for specific events
    if not logs.empty:
        for index, row in logs.iterrows():
            event_id = row['Id']
            event_time = row['TimeCreated']
            event_message = row['Message']

            # Define the criteria for alerts and send email if conditions are met
            if event_id == 4720:
                subject = "Alert: User Account Created"
                body = f"User account created at {event_time}:\n{event_message}"
                send_alert(subject, body)
            elif event_id == 4726:
                subject = "Alert: User Account Deleted"
                body = f"User account deleted at {event_time}:\n{event_message}"
                send_alert(subject, body)
            elif event_id in [4732, 4728]:
                subject = "Alert: User Added to Group"
                body = f"User added to a group at {event_time}:\n{event_message}"
                send_alert(subject, body)
            elif event_id == 4723:
                subject = "Alert: Password Change Attempt"
                body = f"Password change attempt at {event_time}:\n{event_message}"
                send_alert(subject, body)
    else:
        print("No events found in the logs.")
