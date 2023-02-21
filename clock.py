from apscheduler.schedulers.blocking import BlockingScheduler
import app

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
   app.main()

sched.start()