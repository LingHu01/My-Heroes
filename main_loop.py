import schedule
import discord
import command_response


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)

        self.role_message_id = 1055867648891703376
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴')           : 1055864399421771807,
            discord.PartialEmoji(name='🟢')           : 1055864488357810357,
        }

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        channel = client.get_channel(1055175384926273546)
        await client.loop.create_task(schedule.schedule_message(channel))

    async def on_message(self, message):
        if message.author.bot:
            return
        if not message.guild.id == 1048019801802555392:
            return

        if message.content.startswith('!'):
            await command_response.main(message)


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run('MTA1NTE0MTk3OTIyNDI4OTM4MA.GeC4YO.tEdxG5_CsGM4UVjMRGFtkP6xpweI36RUQ5jjNc')
