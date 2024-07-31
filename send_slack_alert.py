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
	bot_name = "alerts-bot"

	# The channel ID or name where you want to send the message
	# channel_id = "alerts"
	channel_id = "C07EVSM8EUS"

	message = "This is being tested by githubofkrishnadhas :slack: "

	# json array attachment
	json = [
  {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year_published": 1960,
    "genre": "Fiction",
    "isbn": "978-0-06-112008-4"
  },
  {
    "title": "1984",
    "author": "George Orwell",
    "year_published": 1949,
    "genre": "Dystopian",
    "isbn": "978-0-452-28423-4"
  },
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year_published": 1925,
    "genre": "Tragedy",
    "isbn": "978-0-7432-7356-5"
  },
  {
    "title": "Pride and Prejudice",
    "author": "Jane Austen",
    "year_published": 1813,
    "genre": "Romance",
    "isbn": "978-0-19-280238-5"
  }
]


	text = fontstyle.apply(json,'RED/ ITALIC/ BOLD')
	print(text)

	# for item in json:

	try:
			# Use the chat.postMessage method to send a message to the channel
			response = client.chat_postMessage(channel=channel_id, text=str(message), username=bot_name)
			print("Message sent successfully!")

			upload_file = client.files_upload_v2(channel=channel_id, filename='imgqqq.png', file='img.png')
			print("File sent successfully")
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