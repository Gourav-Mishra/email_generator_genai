import openai
from config import api_key
openai.api_key = api_key

def payload_for_api(email_tone_type, email_subject, email_content):
    """

    Args:
        email_subject:
        email_subject:
        email_tone_type:

    Returns:
        payload: Returns a payload to send to the api to make a request to generate the content of email.

    """

    email_instruction = f"I want a {email_tone_type} email, with about 80-120 words, describing the text in Email Body, make sure to cover all the points in Email Body"
    payload = [
        {"role": "system", "content": f"You are a helpful email assistant.{email_instruction}"},
        {"role": "user", "content": f"Subject: {email_subject}"},
        {"role": "user", "content": f"Email Body:{email_content}"},
    ]
    return payload

def call_open_ai_chatcompletion_api(payload):
    """
    Args:
        payload: The message instruction from the inputs of UI.
    return:
        assistant_reply: Response from the chat completion API.

    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can also use other models
        messages=payload,
        max_tokens=300  # Adjust the max tokens as needed to limit response length
    )

    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply
