from apscheduler.schedulers.blocking import BlockingScheduler
from weather_fetcher import fetch_weather

sched = BlockingScheduler()

# Run every 10 minutes
@sched.scheduled_job('interval', minutes=10)
def timed_job():
    fetch_weather()

if __name__ == "__main__":
    print("Scheduler started. Press Ctrl+C to stop.")
    sched.start()
