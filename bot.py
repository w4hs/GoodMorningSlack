import os

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from translations import *

load_dotenv()


token = os.environ['SLACK_BOT_TOKEN']
client = WebClient(token)

try:
    message = say_good_morning(good_morning_list)
    response = client.chat_postMessage(channel='#general', text=message)
    assert response["message"]["text"] == message
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")
