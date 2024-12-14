import datetime
import subprocess
import time
import sys

snap_time_video = datetime.timedelta(minutes=1, seconds=11, milliseconds=910)
snap_time_video = datetime.timedelta(minutes=1, seconds=12, milliseconds=100)

now = datetime.datetime.now()

val = sys.argv[1]
assert(len(val) == 3 or len(val) == 4)

val = val.zfill(4)

day_shift = int(val) // 2400
hour = int(val[0:2])
minute = int(val[2:4])

snap_time = datetime.time(hour, minute)
snap_day = now.date() + datetime.timedelta(days=day_shift)

time_to_snap = datetime.datetime.combine(snap_day, snap_time)
start_time = time_to_snap - snap_time_video

if now >= start_time:
    print("Video start before now")

    elapsed_time_since_start = now - start_time

    seconds_into_video = elapsed_time_since_start.total_seconds()

    _ = subprocess.run(["mpv", f"--start={seconds_into_video}", "snap.mkv"])
else:
    print("Video start after now")

    seconds_to_sleep = (start_time - now).total_seconds()
    print(f"Seconds to sleep = {seconds_to_sleep}")

    time.sleep(seconds_to_sleep)
    _ = subprocess.run(["mpv", "snap.mkv"])
