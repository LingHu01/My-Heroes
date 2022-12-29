import discord
async def post_GIF(key, GIF_dict, channel, message):
    if key in GIF_dict.keys() :
        file ='/'.join(GIF_dict[key].split('\\'))
        url = message.author.display_avatar
        name = message.author.display_name
        webhook = await channel.create_webhook(name=name)
        await webhook.send(file=discord.File(file), avatar_url=url)
        await webhook.delete()