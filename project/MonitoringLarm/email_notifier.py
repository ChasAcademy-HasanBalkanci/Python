import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email_notification(alarm_type, threshold):
    message = Mail(
        from_email='hasan.balkanci@chasacademy.se',
        to_emails='hasan.balkanci@chasacademy.se',
        subject=f'Alarm Triggered: {alarm_type.capitalize()}',
        plain_text_content=f'{alarm_type.capitalize()} usage has exceeded {threshold}%.')
    try:
        sg = SendGridAPIClient(os.getenv('dNUasFB2TDekF6j9l_D8ZQ.BjWeBwhWUf0Tb6qDc6XFNLJ7iJtIft3P8ZryRlQinHU'))
        sg.send(message)
        print("Email notification sent.")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
