import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from agents import function_tool
from .config import RECIPIENT_EMAIL, SENDER_EMAIL
from .clients import get_brevo_api_instance

@function_tool
def send_email(body: str):
    """ Send out an email with the given body to all sales prospects """
    print(f"--- TOOL CALLED: Sending Email via Brevo ---")
    api_instance = get_brevo_api_instance()
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=RECIPIENT_EMAIL,
        sender=SENDER_EMAIL,
        subject="Sales email",
        text_content=body
    )
    try:
        api_instance.send_transac_email(send_smtp_email)
        return {"status": "success"}
    except ApiException as e:
        return {"status": "error", "message": str(e)}

@function_tool
def send_html_email(subject: str, html_body: str, to_email: str = None, to_name: str = None, from_email: str = None, from_name: str = None):
    """ Send HTML email. If to/from params provided, overrides defaults. """
    print(f"--- TOOL CALLED: Sending HTML Email via Brevo ---")
    
    # Dynamic Recipient
    if to_email:
        recipient = [{"email": to_email, "name": to_name or "Valued Prospect"}]
    else:
        recipient = RECIPIENT_EMAIL
        
    # Dynamic Sender
    if from_email:
        sender = {"email": from_email, "name": from_name or "Sales Rep"}
    else:
        sender = SENDER_EMAIL

    print(f"-> Sending... To: {recipient}, From: {sender}")

    api_instance = get_brevo_api_instance()
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=recipient,
        sender=sender,
        subject=subject,
        html_content=html_body
    )
    try:
        api_instance.send_transac_email(send_smtp_email)
        return {"status": "success", "recipient": recipient, "sender": sender}
    except ApiException as e:
        return {"status": "error", "message": str(e)}
