import discord

async def main(self, before, after):
	if before.content != after.content:
		embed = discord.Embed(title=f'{before.author.display_name} message edited', color=0x51F5EA)
		embed.add_field(name= 'from', value= before.content)
		embed.add_field(name='to', value=after.content)
		await self.log_channel.send(embed= embed)