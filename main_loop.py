import schedule
import discord
import command
import pickle
import GIF

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.GIF_dict = pickle.load(open('GIF_dict.pkl', 'rb'))
        self.role_message_id = 1055867648891703376
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴')           : 1055864399421771807,
            discord.PartialEmoji(name='🟢')           : 1055864488357810357,
        }

    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        channel = client.get_channel(1055175384926273546)
        await client.loop.create_task(schedule.schedule_message(channel))

    async def on_message(self, message): # noqa
        if message.author.bot:
            return

        channel = client.get_channel(message.channel.id)

        if message.content.startswith('!'):
            await command.main(message)

        if message.content.startswith(':') and message.content.endswith(':'):
            await command.try_delete(message)
            key = message.content[1:-1]
            await GIF.post_GIF(key, self.GIF_dict, channel, message)

    async def on_member_join(self, member): # noqa
        guild = member.guild
        if guild.system_channel is None:
            return

        to_send = \
            f'Welcome {member.mention} to {guild.name}!\n' + \
            'Change name to your in game name\n' + \
            'To apply tag @staff in <#1055160381288501348>\n' + \
            'check <#1055865903906046054> if you\'re interested in guild events'
        await guild.system_channel.send(to_send)

    async def on_raw_member_remove(self, member: discord.RawMemberRemoveEvent): #noqa
        channel = client.get_channel(1060607557837795348)
        await channel.send(f'{member.user.display_name} has leave the server')

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent) :
        if payload.message_id != self.role_message_id :
            return

        try :
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError :
            return

        guild = self.get_guild(payload.guild_id)
        role = guild.get_role(role_id)
        try :
            await payload.member.add_roles(role)
        except discord.HTTPException :
            pass

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if payload.message_id != self.role_message_id :
            return

        try :
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError :
            return

        guild = self.get_guild(payload.guild_id)
        role = guild.get_role(role_id)
        if role is None :
            return

        member = guild.get_member(payload.user_id)
        if member is None :
            return

        try :
            await member.remove_roles(role)
        except discord.HTTPException:
            pass

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run('MTA1NTE0MTk3OTIyNDI4OTM4MA.G_4X8D.cl5QasCdeCCoTpFSU5AAEoS7Xn5TGu1AhQhaXU')
