import discord

async def main(self, before, after):
	if before.content != after.content:
		embed = discord.Embed(title=f"{before.author.display_name}'s message edited", color=0x51F5EA)
		embed.add_field(name= 'from', value= before.content, inline=False)
		embed.add_field(name='to', value=after.content, inline=False)
		await self.log_channel.send(embed= embed)