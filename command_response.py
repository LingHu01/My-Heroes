import random
from asyncio import sleep
import pickle
import discord

async def main(message):
	channel = message.channel
	author= message.author
	user = message.author

	await message.delete()
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

	with open('helptext.txt') as file:
		await user.send('\n'.join(file.readlines()))

async def bulk_delete(channel):
	messages_id = [message async for message in channel.history(limit=123)]
	for message in messages_id :
		await message.delete()
		await sleep(1)
	return

async def roll(channel, author):
	to_send = f'{author.display_name} rolled {random.randint(1, 6)}'
	await channel.send(to_send)
	return

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
	return
