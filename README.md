# send-notifications-to-slack-from-github
This action can be used send notifications of github workflows to slack

# Why slack

Slack is a powerful team collaboration tool that enhances communication and productivity.
It integrates with various apps and services, allowing for seamless workflow automation and centralized information sharing.
Slack's real-time messaging, file sharing, and customizable notifications keep teams connected and organized,
whether working remotely or in the office

# Prerequisites

* Ensure to have a slack account and have admin access there to create a bot.

* How to do it will be available in [prerequisites.md](prerequisites.md) file


# Input parameters
| Input      | Description  | Required   |
|------------|--------------|------------|    
| channel_id | Slack channel Id.| :heavy_check_mark: |
| bot_name   | slack bot name | :heavy_check_mark: |
| file_name | files to be uploadded to slack channel. more than one can be provided as a comma seperated value | :heavy_check_mark: |


# What it does

![github-slack.jpg](github-slack.jpg)

* This automation intends to use GitHub workflows to send communication to slack.

* The communications can be either files, or messages

* A GitHub workflow will be triggered with necessary input params and that can upload a file or a message to the specific Slack channel as a bot.

* The file can be of any type a json file, an image, an Excel or a xml. It Doesnt matter as long as you provide right name.

# Reference

https://api.slack.com/methods

