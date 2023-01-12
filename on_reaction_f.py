async def add(self, payload, discord):
	if payload.message_id != self.role_message_id :
		return

	try :
		role_id = self.emoji_to_role[payload.emoji]
	except KeyError :
		return

	guild = self.get_guild(payload.guild_id)
	role = guild.get_role(role_id)

	if role is None :
		return

	try:
		if role not in payload.member.roles:
			await payload.member.add_roles(role)
		else:
			await payload.member.remove_roles(role)
	except discord.HTTPException :
		pass
