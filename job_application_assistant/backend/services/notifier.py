from . import twilio_service


def send_notifications(phone_numbers: list[str], message: str) -> list[str]:
    message_ids = []
    for number in phone_numbers:
        sid = twilio_service.send_sms(number, message)
        message_ids.append(sid)
    return message_ids
