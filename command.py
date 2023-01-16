import random
from asyncio import sleep
import pickle
import discord

async def main(self, message):
	channel = message.channel
	author= message.author
	user = message.author
	await try_delete(message)

	if message.content.startswith('!roll'):
		await roll(channel, author)
		return

	if message.content.startswith('!bulkdelete'):
		if 'staff' in  (role.name for role in message.author.roles):
			await bulk_delete(channel)
		else:
			await channel.send(f'{author.name} tried to bulk delete')
		return

	if message.content.startswith('!GIF'):
		await GIF_list(user)
		return

	if message.content.startswith('!setting'):
		await send_setting(user, message)
		return

	if message.content.startswith('!night'):
		await night(self, message, user)
		return

	await send_help(user)

async def bulk_delete(channel):
	messages_id = [message async for message in channel.history(limit=123)]
	for message in messages_id :
		await message.delete()
		await sleep(1)


async def roll(channel, author):
	to_send = f'{author.display_name} rolled {random.randint(1, 6)}'
	await channel.send(to_send)


async def GIF_list(user):
	dct = pickle.load(open('GIF_dict.pkl', 'rb'))
	embed = discord.Embed(
		title='GIF list',
		description= 'list of availeble GIF',
		color=0x51F5EA
	)
	await user.send(embed= embed)
	for key in dct.keys():
		file = discord.File('/'.join(dct[key].split('\\')), filename=key + '.gif')
		embed = discord.Embed(
			title= ':' + key + ':',
			color=0x51F5EA
		).set_thumbnail(url= "attachment://" + file.filename)
		await user.send(file= file, embed=embed)

async def send_help(user):
	embed = discord.Embed(title='command list', color=0x51F5EA)
	with open('text/helptext.txt') as file :
		lines = file.readlines()
		for line in lines:
			command, description = line.rstrip().split(' | ')
			embed.add_field(name= command.rstrip(), value= description, inline=False)
			embed.add_field(name='\u200b', value='\u200b', inline=False)
	await user.send(embed= embed)

async def send_setting(user, message):
	if not 'staff' in (role.name for role in message.author.roles) :
		return

	embed = discord.Embed(title='command list', color=0x51F5EA)
	with open('text/setting.txt') as file :
		lines = file.readlines()
		for line in lines:
			command, description = line.rstrip().split(' | ')
			embed.add_field(name= command.rstrip(), value= description, inline=False)
	await user.send(embed= embed)

async def try_delete(message):
	try:
		await message.delete()
	except discord.errors.Forbidden:
		pass

async def night(self, message, user):
	_, day, *time = message.content.rstrip().split(' ')
	if day == 'print':
		message_content = ''
		for key in self.night_raid_time.keys() :
			message_content += f"{key}: {self.night_raid_time[key]}\n"
		await user.send(message_content[:-1])
		return

	if 'staff' not in (role.name for role in user.roles) :
		await user.send(f'{user.name} have not that privilege')
		return

	day = int(day)
	if day in range(1, 6) and int(time[0].split(':')[0]) in range (0, 25) and int(time[0].split(':')[1]) in range (0,61):
		self.night_raid_time[day] = time[0]
		pickle.dump(self.night_raid_time, open('night_raid_time.pkl', 'wb'))
		await user.send(f"successfully set day {day} to {time[0]}")
	elif day not in range(1, 6):
		await user.send('invalid day')
	else:
		await user.send('invalid time')