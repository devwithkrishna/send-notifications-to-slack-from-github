# Step 1

* if you have a slack bot you can skip this step.

* Login to your Slack account and then access this url to create a bot (app) https://api.slack.com/apps 

* Click on create a new app at the top right to create a new bot account

![create-a-new-app.jpeg](image-references/create-a-new-app.jpeg)

* Click on `create from scratch` option . Provide a `name` and select `your Slack workspace` from drop down

* click on `Create App`

![new-bot-demo.jpeg](image-references/new-bot-demo.jpeg) 


# Step 2

* Under `Basic Information` You will see `Add features and functionality`. Click on `Bots`

![add-features-and-functionality.jpeg](image-references/add-features-and-functionality.jpeg)

* This will take you to `App Home`. Click on `review scopes to add` 

![review-scopes-to-add.png](image-references/review-scopes-to-add.png)

* scroll down to `scopes` section and choose below permissions under `bot token scopes`

![new-scopes.png](image-references/new-scopes.png)

| OAuth Scope | Description |
|-------------|-------------|
| chat:write | Send messages as demo-bot |
| chat:write.customize | Send messages as demo-bot with a customized username and avatar |
| files:write | Upload, edit, and delete files as demo-bot |

![permissions.jpeg](image-references/permissions.jpeg)

* You need to install the bot. for this scroll above under `OAuth & Permissions` click on `install to workspace`4

![allow.jpeg](image-references/allow.jpeg)  

* Then provide access by clicking allow. Once installed you will see a api token which you need to use. keep it safe and secure.

![api-token.png](image-references/api-token.png)

* Thats the end of all Prerequisites

* When you revisit your slack under home page under apps you will see the app you just created.