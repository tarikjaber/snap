import datetime
import subprocess
import time

# The time of the snap in the video (hours, minutes, seconds)
snap_time = datetime.timedelta(minutes=1, seconds=11, milliseconds=910)  # 1 minute and 11 seconds before the snap

# Calculate when to start the video
now = datetime.datetime.now()
midnight = datetime.datetime.combine(now.date() + datetime.timedelta(days=1), datetime.time(0, 0, 0))  # Midnight of the current day
# midnight = datetime.datetime.combine(now.date(), datetime.time(2, 30, 0))  # Midnight of the current day
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
    time.sleep((start_time - now).total_seconds())

    # Start the video from the beginning
    subprocess.run(["mpv", "snap.mkv"])
