import os
import fontstyle
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
from datetime import datetime

def send_slack_notifications():
	"""
	Send alerts / communication to slack workspace
	:return:
	"""
	slack_token = os.getenv('SLACK_TOKEN')
	# Initialize a slack WebClient instance with your token
	client = WebClient(token=slack_token)
	# bot name
	bot_name = "alerts"

	# The channel ID or name where you want to send the message
	channel_id = "alerts"

	message = "This is being tested by githubofkrishnadhas :slack: "
	text = fontstyle.apply(message,'RED/ ITALIC/ BOLD')
	print(text)
	try:
		# Use the chat.postMessage method to send a message to the channel
		response = client.chat_postMessage(channel=channel_id, text=message, username=bot_name)
		print("Message sent successfully!")
	except SlackApiError as e:
		# Error handling in case the message fails to send
		print(f"Error sending message: {e}")


def main():
	"""
	testing the code
	:return:
	"""
	load_dotenv()
	send_slack_notifications()


if __name__ == "__main__":
	main()