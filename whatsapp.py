from twilio.rest import Client
from datetime import datetime
import time

account_sid = 'AC1c34d1fd5b65520e6c14394f796e47fd'
auth_token = 'fd516140182e537767a43910af7a6dfa'

client = Client(account_sid, auth_token)


def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f' An error occurred: {e}')

name = input("Enter the recipient name: ")
recipient_number = input("Enter the recipient WhatsApp number with country code (e.g., +919876543210): ")
message_body = input(f"Enter the message you want to send to {name}: ")

date_str = input("Enter the date you want to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24-hour format): ")


schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()


time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print(" The specified time is in the past. Please enter a future date and time.")
else:
    print(f" Message scheduled to be sent to {name} at {schedule_datetime}")
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number, message_body)
