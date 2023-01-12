import discord
import pickle
import on_message_f
import on_ready_f
import on_member_f
import on_reaction_f

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.GIF_dict = pickle.load(open('GIF_dict.pkl', 'rb'))
        self.role_message_id = 1055867648891703376
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴')           : 1055864399421771807,
            discord.PartialEmoji(name='🟢')           : 1055864488357810357,
            discord.PartialEmoji(name='🔵')           : 1062791691544830113
        }

    async def on_ready(self):
        await on_ready_f.main(self, client)

    async def on_message(self, message): # noqa
        await on_message_f.main(self, message, client)


    async def on_member_join(self, member): # noqa
        await on_member_f.join(member)

    async def on_raw_member_remove(self, member: discord.RawMemberRemoveEvent): # noqa
        await on_member_f.leave(member, client)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent) : # noqa
        await on_reaction_f.add(self, payload, discord)



intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run('MTA1NTE0MTk3OTIyNDI4OTM4MA.G_4X8D.cl5QasCdeCCoTpFSU5AAEoS7Xn5TGu1AhQhaXU')
