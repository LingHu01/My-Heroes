import random

async def main(message):
	channel = message.channel
	await message.delete()
	if message.content.startswith('!roll'):
		to_send = f'{message.author.display_name} rolled {random.randint(1,6)}'
		await channel.send(to_send)
		return

	with open('helptext.txt') as file:
		user = message.author
		await user.send('\n'.join(file.readlines()))
