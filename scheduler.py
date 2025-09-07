from apscheduler.schedulers.background import BackgroundScheduler
from pipeline import run_pipeline
import time

scheduler=BackgroundScheduler()
scheduler.add_job(run_pipeline,"interval",hours=6)
scheduler.start()

print("Scheduler running..... Press Ctrl+C to exit")

try:
    while True:
        time.sleep(60)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()