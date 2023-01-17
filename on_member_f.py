async def join(member):
    guild = member.guild
    if guild.system_channel is None :
        return

    to_send = \
        f'Welcome {member.mention} to {guild.name}!\n' + \
        'do the following: \n' + \
        '-Change name to your in game name\n\n' + \
        '-To apply send the application in-game and ***ONLY*** after tag @staff in <#1055160381288501348>\n\n' + \
        '-check <#1055865903906046054> if you\'re interested in co-op content'
    await guild.system_channel.send(to_send)

async def leave(member, client):
    channel = client.get_channel(1060607557837795348)
    await channel.send(f'{member.user.display_name} has leave the server')