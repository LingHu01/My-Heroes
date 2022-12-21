from schedule import schedule_message
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        channel = client.get_channel(1055175384926273546)
        await client.loop.create_task(schedule_message(channel))

    async def on_message(self, message):
        if message.author != self.user and message.content:
            print(f'Message from {message.author}: {message.content}')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = \
                f'Welcome {member.mention} to {guild.name}!\n' + \
                'Change name to your in game name\n' + \
                'To apply tag @staff in <#1055160381288501348>'
            await guild.system_channel.send(to_send)







intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run('MTA1NTE0MTk3OTIyNDI4OTM4MA.GeWIjb.Q1SISwKy9jGXQTdmns2XxjTQygSg2Y5QeBJ8SI')
