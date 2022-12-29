import requests
import discord
async def post_GIF(key, GIF_dict, channel, message):
    if key in GIF_dict.keys() :
        file ='/'.join(GIF_dict[key].split('\\'))
        original = message.author.display_name
        name = message.author.display_name
        try :
            req = requests.get(url=original.avatar.url)
            avatar = req.content
            webhook = await channel.create_webhook(name=name, avatar=avatar)
        except AttributeError :
            webhook = await channel.create_webhook(name=name)
            await webhook.send(file=discord.File(file))
        await webhook.delete()