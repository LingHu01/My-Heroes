import discord
import pickle
import discord_method
from discord import app_commands
import atexit
import drive


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tree = None
        self.drive = None
        self.role_channel = None
        self.cmd_log = None
        self.log_channel = None
        self.announcement_channel = None
        self.bot_channel = None

        self.night_raid_time = pickle.loads(dbx.files_download(path='/night_raid_time.pkl')[1].content)
        self.GIF_dict = pickle.load(open('GIF_dict.pkl', 'rb'))
        self.role_message_id = 1069345953217253456
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴'): 1055864399421771807,
            discord.PartialEmoji(name='🟢'): 1055864488357810357,
            discord.PartialEmoji(name='🔵'): 1062791691544830113,
            discord.PartialEmoji(name='⚪'): 1069338069314052146
        }

    async def setup_hook(self):
        self.tree = tree
        self.drive = dbx

    async def on_ready(self):
        self.role_channel = client.get_channel(1055865903906046054)
        self.cmd_log = client.get_channel(1082773264939626526)
        self.log_channel = client.get_channel(1082778992907669564)
        self.announcement_channel = client.get_channel(1051111394436718673)
        await discord_method.on_ready(self, client)

    def closing(self):
        discord_method.on_disconnect(self)

    async def on_message(self, message):  # noqa
        await discord_method.on_message(self, message, client)

    async def on_member_join(self, member):  # noqa
        await discord_method.on_memeber_join(member)

    async def on_raw_member_remove(self, member: discord.RawMemberRemoveEvent):  # noqa
        await discord_method.on_memeber_leave(member, client)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):  # noqa
        await discord_method.on_reaction(self, payload, client)

    async def on_message_edit(self, before, after):  # noqa
        await discord_method.on_message_edit(self, before, after)

    async def on_message_delete(self, message):  # noqa
        await discord_method.on_message_delete(self, message)


def cleanup():
    client.closing()


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    dbx = drive.main()

    client = MyClient(intents=intents, drive=dbx)
    atexit.register(cleanup)
    guild = discord.Object(id=1048019801802555392)
    tree = app_commands.CommandTree(client)

    client.run('MTA1NTE0MTk3OTIyNDI4OTM4MA.G_4X8D.cl5QasCdeCCoTpFSU5AAEoS7Xn5TGu1AhQhaXU')
