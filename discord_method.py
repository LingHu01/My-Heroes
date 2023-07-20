import functions
import GIF
import schedule
import discord


async def on_message(self, message, client):
    if message.author.bot:
        return
    channel = client.get_channel(message.channel.id)

    if message.content.startswith('!'):
        message_lower = message.content.lower()
        channel = message.channel
        user = message.author
        await functions.try_delete(self, message)

        if message_lower.startswith('!roll'):
            return await functions.roll(channel, user)
        if message_lower.startswith('!bulkdelete') and 'staff' in (role.name for role in message.author.roles):
            return await functions.bulk_delete(channel)
        if message_lower.startswith('!gif'):
            return await functions.GIF_list(user)
        if message_lower.startswith('!setting'):
            return await functions.send_setting(user, message)
        if message_lower.startswith('!night'):
            return await functions.night(self, message, user)
        if message_lower.startswith('!sync'):
            return await functions.sync(self, message, user)
        if message_lower.startswith('!reaction'):
            return await functions.reaction(self, message, user)
        if message_lower.startswith('!say'):
            return await functions.say(message, user, channel)
        if message_lower.startswith('!react'):
            return await functions.react(self, message, user)
        if message_lower.startswith('!announce'):
            return await functions.announce(self, message, user)
        if message_lower.startswith('!close'):
            return await functions.close()
        await functions.send_help(user)

    if message.content.startswith(':') and message.content.endswith(':'):
        await functions.try_delete(self, message)
        key = message.content[1:-1]
        await GIF.post_GIF(key, self.GIF_dict, channel, message)

async def on_ready(self, client):
    print(f'Logged on as {self.user}!')
    channel = client.get_channel(1055175384926273546)
    await client.loop.create_task(schedule.schedule_message(self, channel))

async def on_message_delete(self, message):
    if message.content.startswith('!') or message.content.startswith(':'):
        return
    if message.channel.id == 1055175384926273546:
        return
    embed = discord.Embed(title=f"{message.author.display_name}'s message was deleted", color=0x51F5EA,
                          description=message.content)
    await self.log_channel.send(embed=embed)

async def on_message_edit(self, before, after):
    if before.content != after.content:
        embed = discord.Embed(title=f"{before.author.display_name}'s message edited", color=0x51F5EA)
        embed.add_field(name='from', value=before.content, inline=False)
        embed.add_field(name='to', value=after.content, inline=False)
        await self.log_channel.send(embed=embed)

async def on_reaction(self, payload, client):
    if payload.member.bot:
        return

    if payload.message_id != self.role_message_id:
        return

    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    await message.remove_reaction(payload.emoji, payload.member)

    try:
        role_id = self.emoji_to_role[payload.emoji]
    except KeyError:
        return

    guild = self.get_guild(payload.guild_id)
    role = guild.get_role(role_id)

    if role is None:
        return

    try:
        member = await guild.fetch_member(payload.member.id)
        if role not in payload.member.roles:
            await payload.member.add_roles(role)
            await member.send(f'role @{role.name} added ')
        else:
            await payload.member.remove_roles(role)
            await member.send(f'role @{role.name} removed ')
    except discord.HTTPException:
        pass

async def on_memeber_leave(event, client):
    channel = client.get_channel(1060607557837795348)
    await channel.send(f'<@!{event.user.id}> {event.user.display_name} has left the server')

async def on_memeber_join(member):
    guild = member.guild
    if guild.system_channel is None:
        return

    to_send = \
        f'Welcome {member.mention} to {guild.name}!\n' + \
        'do the following: \n\n' + \
        '-Read <#1064163861244153856>\n\n' + \
        '-Change name to your in game name\n\n' + \
        '-To apply send the application in-game and ***ONLY*** after tag @staff in <#1055160381288501348>\n\n' + \
        '-check <#1055865903906046054> if you\'re interested in co-op content'
    await guild.system_channel.send(to_send)

def on_disconnect(self):
    print('disconnecting...')
