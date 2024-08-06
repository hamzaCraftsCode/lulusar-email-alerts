# email_alerts.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import yaml

# Function to read YAML file
def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

# Read the YAML file
def load_config(yaml_file='config.yaml'):
    config = read_yaml(yaml_file)
    password = config.get('PASSWORD')
    sender_email = config.get('EMAIL')
    alerts_enabled = config.get('ALERTS_ENABLED', True)
    recipients = config.get('RECEIVERS', [])
    return sender_email, password, alerts_enabled, recipients

# Function to send email
def send_email(subject, body, yaml_file='config.yaml'):
    """Sends an email to multiple recipients."""
    sender_email, password, alerts_enabled, recipients = load_config(yaml_file)
    
    if not alerts_enabled:
        print("Alerts are disabled.")
        return

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Ensure recipients is a list
    if not isinstance(recipients, list):
        recipients = [recipients]

    recipient_string = ', '.join(recipients)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_string
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
