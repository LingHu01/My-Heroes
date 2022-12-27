from datetime import datetime
import pytz
from asyncio import sleep
from command_response import bulk_delete

async def schedule_message(channel):
    server_timezone = pytz.timezone("America/New_York")
    while True:
        time_info = datetime.now(server_timezone)
        weekday = datetime.weekday(time_info)
        current_server_time = time_info.strftime("%H:%M")

        if weekday in range(0, 5):
            if current_server_time == '15:30':
                await channel.send('<@&1055864399421771807> in 30 min')
            if current_server_time == '15:50':
                await channel.send('<@&1055864399421771807> in 10 min')
            if current_server_time == '16:00':
                await channel.send('<@&1055864399421771807> now')
        if weekday in range(5, 7):
            if current_server_time in {'08:00', '15:00', '20:00'}:
                await channel.send('<@&1055864488357810357>')

        if current_server_time == '01:00' and weekday == 6:
            await bulk_delete(channel)

        await sleep(60)