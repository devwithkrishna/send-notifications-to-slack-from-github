import argparse
import json
import os
from datetime import datetime, timezone

from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


def get_date_time():
	""" get the date time back"""
	# Get the current date and time in UTC
	now_utc = datetime.now(timezone.utc)

	# Format the date and time
	formatted_datetime = now_utc.strftime('%Y-%m-%d %H:%M UTC')

	return formatted_datetime


def read_json_file_and_return_str(file_name: str):
	"""
	Read the json file and return the formatted string
	:param file_name:
	:return:
	"""
	with open(file_name, 'r') as file:
		data = json.load(file)
	formatted_data = json.dumps(data, indent=4)
	# print(f'{formatted_data}')
	return formatted_data


def send_slack_msg_notification(channel_id: str, bot_name: str, text: str):
	"""
	send slack message as alert. No file upload through this function
	:param channel_id:
	:param bot_name:
	:param default_message:
	:param file_name:
	:return:
	"""
	slack_token = os.getenv('SLACK_TOKEN')
	# Initialize a slack WebClient instance with your token
	client = WebClient(token=slack_token)

	# try catch block
	try:
		response = client.chat_postMessage(channel=channel_id, text=text, username=bot_name)
		print("Message sent successfully!")
		print(f"The message is:\t  \n{response.data['message']['text']}")

	except SlackApiError as e:
		print(f"Error sending message: {e.response['error']}")

def send_slack_notifications_with_only_file_upload(channel_id: str, bot_name: str, file_name: str):
	"""
	Send alerts / communication to slack workspace
	:param bot_name str
	:param channel_id str
	:param text str
	:param file_name str
	:return:
	"""
	load_dotenv()
	slack_token = os.getenv('SLACK_TOKEN')
	# Initialize a slack WebClient instance with your token
	client = WebClient(token=slack_token)
	# Split the comma-separated string into a list of file names
	files = [file.strip() for file in file_name.split(',')]
	# try catch block
	for file in files:
		try:
			# extract file names in case files are inside nested folders
			file_name = os.path.basename(file)
			# get absolute path
			gh_workspace = os.getenv('GITHUB_WORKSPACE')
			full_path = f'{gh_workspace}/{file}'
			print(f'Looking for file under {full_path}')
			# Specify the directory you want to list
			directory = '.'

			# List all files and directories in the specified directory
			files = os.listdir(directory)
			print(files)
			# Upload each file individually
			upload_file = client.files_upload_v2(channel=channel_id, filename=file_name, file=full_path)
			print(f"File {file} sent successfully to Slack channel {channel_id}")
		except SlackApiError as e:
			# Error handling in case the message fails to send
			print(f"Error sending message: {e.response['error']}")
			break


def main():
	"""
	testing the code
	:return:
	"""
	load_dotenv()
	parser = argparse.ArgumentParser("Arguments for Slack channel notification")
	parser.add_argument("--channel_id", help="Slack Channel ID", type=str, required=True)
	parser.add_argument("--bot_name", help="Slack bot name", type=str, required=True)
	parser.add_argument("--file_name", help="File / content to be uploaded to slack", type=str, required=True)

	args = parser.parse_args()

	print(f'Process started at {get_date_time()}')

	channel_id = args.channel_id
	bot_name = args.bot_name
	file_name = args.file_name

	send_slack_notifications_with_only_file_upload(channel_id=channel_id, bot_name=bot_name, file_name=file_name)

	print(f'Process completed at {get_date_time()}')

if __name__ == "__main__":
	main()
