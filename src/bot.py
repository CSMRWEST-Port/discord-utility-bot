import discord, UserManagement.ModerationActions

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!'):
            if (message.content.startswith('!ban')):
                await UserManagement.ModerationActions.onBan(self, message)
            elif (message.content.startswith('!unban')):
                await UserManagement.ModerationActions.onUnban(self, message)
            elif (message.content.startswith('!kick')):
                await UserManagement.ModerationActions.onKick(self, message)
            elif (message.content.startswith('!mute')):
                await UserManagement.ModerationActions.onMute(self, message)
            elif (message.content.startswith('!unmute')):
                await UserManagement.ModerationActions.onUnmute(self, message)
# Necessary intents for the bot to do what I want it to do
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.presences = True

# Start the bot baby
client = MyClient(intents=intents)
client.run('YOUR_BOT_TOKEN_HERE')