import datetime
import pytz
from asyncio import sleep
from command import bulk_delete

async def schedule_message(self, channel):
    server_timezone = pytz.timezone("America/New_York")
    while True:
        time_info = datetime.datetime.now(server_timezone)
        weekday = datetime.datetime.weekday(time_info) + 1
        current_server_time = time_info.strftime("%H:%M")

        hours, minutes = map(int, self.night_raid_time[weekday].split(':'))
        target_time = datetime.time(hours, minutes, 0)

        if target_time.strftime('%H:%M') == (time_info + datetime.timedelta(minutes= 30)).strftime('%H:%M'):
            await channel.send('<@&1055864399421771807> in 30 min')
        if target_time.strftime('%H:%M') == (time_info + datetime.timedelta(minutes= 5)).strftime('%H:%M'):
            await channel.send('<@&1055864399421771807> in 5 min')
        if target_time.strftime('%H:%M') == time_info.strftime('%H:%M'):
            await channel.send('<@&1055864399421771807> now')
        if weekday in range(5, 7):
            if current_server_time in {'08:00', '15:00', '20:00'}:
                await channel.send('<@&1055864488357810357>')

        if current_server_time == '01:00' and weekday == 6:
            await bulk_delete(channel)

        await sleep(60)