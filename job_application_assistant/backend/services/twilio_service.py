import os
from twilio.rest import Client


def send_sms(to_number: str, message: str) -> str:
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_PHONE_NUMBER")

    if not account_sid:
        raise ValueError("TWILIO_ACCOUNT_SID is not set in environment variables.")
    if not auth_token:
        raise ValueError("TWILIO_AUTH_TOKEN is not set in environment variables.")
    if not from_number:
        raise ValueError("TWILIO_PHONE_NUMBER is not set in environment variables.")

    client = Client(account_sid, auth_token)

    msg = client.messages.create(
        body=message,
        from_=from_number,
        to=to_number
    )
    return msg.sid
