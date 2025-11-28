import os

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

load_dotenv()

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
channel = "#dsci-pipelines-stats"


def send_monthly_message():
    try:
        client.chat_postMessage(
            channel=channel,
            text="""
*<!channel> dataset updates needed!*

Please update the following datasets on Azure. Instructions are linked below.
- <https://knowledge.base.unocha.org/wiki/spaces/DSCI/pages/4829413383/Instructions+for+manual+updates#1.-EM-DAT|EM-DAT>
- <https://knowledge.base.unocha.org/wiki/spaces/DSCI/pages/4829413383/Instructions+for+manual+updates#2.-CERF-Allocations|CERF Allocations>

React with ✅ when done, for each dataset.
            """,  # noqa: E501
        )
    except SlackApiError as e:
        print(f"Error: {e.response['error']}")


if __name__ == "__main__":
    send_monthly_message()
