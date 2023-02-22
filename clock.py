from apscheduler.schedulers.blocking import BlockingScheduler
import app

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=30)
def timed_job():
    print('Starting scrape...')
    app.main()

sched.start()