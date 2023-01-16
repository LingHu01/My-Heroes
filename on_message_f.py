import command
import GIF

async def main(self, message, client):
    if message.author.bot :
        return

    channel = client.get_channel(message.channel.id)

    if message.content.startswith('!') :
        await command.main(self, message)

    if message.content.startswith(':') and message.content.endswith(':') :
        await command.try_delete(message)
        key = message.content[1 :-1]
        await GIF.post_GIF(key, self.GIF_dict, channel, message)