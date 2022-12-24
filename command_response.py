import random
from asyncio import sleep

async def main(message):
	channel = message.channel
	author_name = message.author.display_name
	if message.content.startswith('!roll'):
		await roll(channel, author_name)
		return

	if message.content.startswith('!bulkdelete'):
		await bulk_delete(channel)
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

async def roll(channel, author_name):
	to_send = f'{author_name} rolled {random.randint(1, 6)}'
	await channel.send(to_send)
	return
