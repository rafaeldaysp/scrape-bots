from apscheduler.schedulers.blocking import BlockingScheduler
import app

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=5)
def timed_job():
    print('Starting scrape...')
    app.main()

sched.start()