import schedule

async def main(self, client):
    print(f'Logged on as {self.user}!')
    channel = client.get_channel(1055175384926273546)
    await client.loop.create_task(schedule.schedule_message(channel))