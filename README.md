# Discord Utility Bot

This project aims to design a self-hosted bot for Discord using the Discord.py API. The bot aims to provide complete integration with moderation actions and to be easily extensible by others through minor code changes.
This bot will be the baseline for a future personal project of mine which requires a fully functioning Discord utility bot as a baseline.

## Getting Started Requirements
- (Optional) Docker v.4.64 or above for containerization
- Python 3.14.3 or greater
  - If not using Docker, the Discord Dependency can be installed using ```python3 -m pip install discord.py```
- A valid Discord Bot Token

The Discord Bot Token can be injected directly into the client.run() call in src/bot.py and is required before running the bot.
Your bot must be configured to handle the intents of message_content, guilds and presences otherwise it will not start up. These are required for the functionality of the bot to be global and accessible without pinging the bot.


## Contributors
- @CSMRWEST-Port -- Ronnie Westhead
