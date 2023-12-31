import datetime
import subprocess
import time

def wait_until(target):
    while True:
        now = datetime.datetime.now()
        if now >= target:
            break
        sleep_time = (target - now).total_seconds() / 2
        sleep_until = now + datetime.timedelta(seconds=sleep_time)
        print(f"Sleeping until {sleep_until}...")
        time.sleep((target - now).total_seconds() / 2)

# The time of the snap in the video (hours, minutes, seconds)
snap_time = datetime.timedelta(minutes=1, seconds=11, milliseconds=600)  # 1 minute and 11 seconds before the snap

# Calculate when to start the video
now = datetime.datetime.now()
midnight = datetime.datetime.combine(now.date() + datetime.timedelta(days=1), datetime.time(0, 0, 0))  # Midnight of the current day
# midnight = datetime.datetime.combine(now.date(), datetime.time(16, 5, 0))  # Midnight of the current day
start_time = midnight - snap_time

# Check if the current time is past the start time
if now >= start_time:
    # Calculate how far into the video we should be
    elapsed_time_since_start = now - start_time
    seconds_into_video = elapsed_time_since_start.total_seconds()

    # Start the video at the calculated position
    subprocess.run(["mpv", f"--start={seconds_into_video}", "snap.mkv"])
else:
    # Wait until it's time to start the video
    wait_until(start_time)

    # Start the video from the beginning
    subprocess.run(["mpv", "snap.mkv"])
