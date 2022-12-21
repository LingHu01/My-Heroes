from datetime import datetime
import pytz
from asyncio import sleep

async def schedule_message(channel):
    server_timezone = pytz.timezone("America/New_York")
    while True:
        time_info = datetime.now(server_timezone)
        weekday = datetime.weekday(time_info)
        current_server_time = time_info.strftime("%H:%M")

        if weekday in range(0, 5):
            if current_server_time == '15:00':
                channel.send('@everyone night raid in 1 hour')
            if current_server_time == '15:50':
                channel.send('@everyone night raid in 10 min')
        if weekday in range(5, 6):
            if current_server_time in {'08:00', '15:00', '20:00'}:
                channel.send('@everyone world boss')



        print(weekday, current_server_time)

        await sleep(60)