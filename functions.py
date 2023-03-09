import random
from asyncio import sleep
import pickle
import discord
import io
import quickstart
from googleapiclient.http import MediaIoBaseUpload
from googleapiclient.errors import HttpError
from google.auth.exceptions import RefreshError

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
	await user.send(embed= embed)

async def send_setting(user, message):
	if not 'staff' in (role.name for role in message.author.roles) :
		return

	embed = discord.Embed(title='setting list', color=0x51F5EA)
	with open('text/setting.txt') as file :
		lines = file.readlines()
		for line in lines:
			command, description = line.rstrip().split(' | ')
			embed.add_field(name= command.rstrip(), value= description, inline=False)
	await user.send(embed= embed)

async def try_delete(self, message):
	embed = discord.Embed(title=f'{message.author.display_name} used', color=0x51F5EA, description= message.content)
	await self.cmd_log.send(embed= embed)
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
		await user.send(f"successfully set day {day} to {time[0]}")

		try :
			await save_to_cloud(self, user, file_id = '16zD6USJln7fmlAd2V5EcmE28m0xnwwRR')

		except RefreshError:
			await user.send('token expired')
			self.drive = await quickstart.refresh()
			await user.send('token refreshed')

		except HttpError as error :
			await user.send(f'An error occurred: {error}')

	elif day not in range(1, 6):
		await user.send('invalid day')
	else:
		await user.send('invalid time')

async def reaction(self, message, user):
	react_id = message.content.rstrip().split(' ')[1]
	self.role_message_id = react_id
	await user.send(f"id set to {react_id}")

async def sync(self, message, user):
	if 'staff' in (role.name for role in message.author.roles) :
		await self.tree.sync(guild=discord.Object(id=1048019801802555392))
		await user.send('sync successful')

async def say(message, user, channel):
	if 'staff' in (role.name for role in user.roles):
		await channel.send(message.content.rstrip().split(' ', maxsplit= 1)[1])

async def react(self, message, user):
	if not 'staff' in (role.name for role in user.roles) :
		return

	channel = self.role_channel
	target_message = await channel.fetch_message(self.role_message_id)
	_, emoji = message.content.rstrip().split(' ', maxsplit=1)
	for x in emoji:
		await target_message.add_reaction(x)

async def announce(self, message, user):
	if 'staff' in (role.name for role in user.roles) :
		channel = self.announcement_channel
		await channel.send(message.content.rstrip().split(' ', maxsplit= 1)[1])

async def save_to_cloud(self, user, file_id):
	pkl_data = pickle.dumps(self.night_raid_time)
	file_stream = io.BytesIO(pkl_data)
	media = MediaIoBaseUpload(file_stream, mimetype='application/octet-stream')
	file_metadata = {'name' : 'night_raid_time.pkl'}
	await self.drive.files().update(fileId=file_id, media_body=media, body=file_metadata).execute()
	await user.send('File updated successfully.')