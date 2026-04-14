import discord

class GameBot:
    def __init__(self):
        self.client = discord.Client()

    async def on_ready(self):
        print(f'Logged in as {self.client.user}')

    def run(self, token):
        self.client.run(token)

if __name__ == '__main__':
    bot = GameBot()
    bot.run('YOUR_BOT_TOKEN')
