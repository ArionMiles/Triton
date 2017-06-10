# Notifications Tracker
Forward GitHub notifications to Telegram.

Author: Arion Miles (Kanishk Singh)

# Introduction
Uses [GitHub API v3](https://developer.github.com/v3/) to monitor for new notifications and then formats it, and forwards to your Telegram Messenger via a bot. Who constantly checks email, amirite? I'm always online on Telegram so I might as well have the notifications delivered there instead of using the default email method. Plus, it was a learning experience! Really, I don't have a better motive to explain why I made this.

# Installation
You can use Heroku for deploying this bot. I'll be adding more details about it.

You need three pieces of information: `Telegram BOT TOKEN`, `Telegram CHAT ID`, and `GitHub TOKEN`. [Start here](https://core.telegram.org/bots#3-how-do-i-create-a-bot) to learn how to create a Telegram Bot for **Bot Token**. You can message [@get_id](https://telegram.me/get_id_bot) bot with `/my_id` and it'll give you a 9-digit `Chat ID`. You can make a new Personal Access Token for GitHub [here.](https://github.com/settings/tokens/new) Put any description you want, and check `Notifications` in the scope options and click Generate. Keep this token safe, because you cannot retrieve it back if it's lost, only generate a new one.

For running this locally, copy the `Bot Token` & `Chat ID` you received to `creds.ini` (remove [SAMPLE] from the name) file under `[BOT] TOKEN` & ` [BOT] CHAT_ID` respectively. Also copy the GitHub Personal Access Token and paste under `[GITHUB] GitToken`, remember to leave the `token` word in the value as it is because it is required in the headers by the API, or you'll get a `TypeError` because the program will never find any JSON output.

# To-Do
- [ ] Add images
- [ ] Edit/Fine Tune MessageContent. (add comment text, if possible)
- [ ] Put a try-except block to catch any exceptions for debugging.
- [ ] Change name to something better.
- [ ] Add repo to https://gallery.devup.in/
- [ ] Add python3 compatibility

# License
MIT License. Please see [License](LICENSE.md) file for more information.
