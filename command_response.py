import random
from asyncio import sleep

async def main(message):
	channel = message.channel
	author= message.author
	if message.content.startswith('!roll'):
		await roll(channel, author)
		return

	if message.content.startswith('!bulkdelete'):
		if message.author.server_permissions.administrator:
			await bulk_delete(channel)
		else:
			await channel.send(f'{author.name} tried to bulk delete')
		return

	with open('helptext.txt') as file:
		user = message.author
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
