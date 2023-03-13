import os
import discord
import pickle
import discord_method
import quickstart as quickstart
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from discord import app_commands

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs) :
        super().__init__(*args, **kwargs)
        self.night_raid_time = pickle.loads(drive_service.files().get_media(fileId='16zD6USJln7fmlAd2V5EcmE28m0xnwwRR').execute())
        self.GIF_dict = pickle.load(open('GIF_dict.pkl', 'rb'))
        self.role_message_id = 1069345953217253456
        self.emoji_to_role = {
            discord.PartialEmoji(name='🔴')          : 1055864399421771807,
            discord.PartialEmoji(name='🟢')          : 1055864488357810357,
            discord.PartialEmoji(name='🔵')          : 1062791691544830113,
            discord.PartialEmoji(name='⚪')          : 1069338069314052146
        }

    async def setup_hook(self):
        self.tree = tree # noqa
        self.drive = drive_service # noqa

    async def on_ready(self):
        self.role_channel = client.get_channel(1055865903906046054)  # noqa
        self.cmd_log = client.get_channel(1082773264939626526)  # noqa
        self.log_channel = client.get_channel(1082778992907669564) # noqa
        self.announcement_channel = client.get_channel(1051111394436718673) # noqa
        await discord_method.on_ready(self, client)

    async def on_message(self, message): # noqa
        await discord_method.on_message(self, message, client)


    async def on_member_join(self, member): # noqa
        await discord_method.on_memeber_join(member)

    async def on_raw_member_remove(self, member: discord.RawMemberRemoveEvent): # noqa
        await discord_method.on_memeber_leave(member, client)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent) : # noqa
        await discord_method.on_reaction(self, payload, client)

    async def on_message_edit(self, before, after) : # noqa
        await discord_method.on_message_edit(self, before, after)

    async def on_message_delete(self, message) : # noqa
        await discord_method.on_message_delete(self, message)

if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    quickstart.main()
    script_path = os.getcwd()
    TOKEN_PATH = script_path + '/token.json'

    creds = Credentials.from_authorized_user_file(TOKEN_PATH)
    drive_service = build('drive', 'v3', credentials=creds)

    client = MyClient(intents=intents, drive= drive_service)
    guild = discord.Object(id=1048019801802555392)
    tree = app_commands.CommandTree(client)

    client.run('MTA1NTE0MTk3OTIyNDI4OTM4MA.G_4X8D.cl5QasCdeCCoTpFSU5AAEoS7Xn5TGu1AhQhaXU')
