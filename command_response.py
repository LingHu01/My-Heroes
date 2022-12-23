import random

async def main(message):
	channel = message.channel
	if message.content.startswith('!roll'):
		to_send = f'{message.author.display_name} rolled {random.randint(1,6)}'
		await channel.send(to_send)
	return
