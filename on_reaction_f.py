async def add(self, payload, discord, client):
	if payload.member.bot :
		return

	if payload.message_id != self.role_message_id :
		return

	channel = client.get_channel(payload.channel_id)
	message = await channel.fetch_message(payload.message_id)
	await message.remove_reaction(payload.emoji, payload.member)

	try :
		role_id = self.emoji_to_role[payload.emoji]
	except KeyError :
		return

	guild = self.get_guild(payload.guild_id)
	role = guild.get_role(role_id)

	if role is None :
		return

	try :
		member = await guild.fetch_member(payload.member.id)
		if role not in payload.member.roles :
			await payload.member.add_roles(role)
			await member.send(f'role @{role.name} added ')
		else :
			await payload.member.remove_roles(role)
			await member.send(f'role @{role.name} removed ')
	except discord.HTTPException :
		pass
