from apscheduler.schedulers.blocking import BlockingScheduler
import app, aliexpress_setup

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=30)
def timed_job():
    print('Starting scrape...')
    app.main()

aliexpress_setup.setup_ali()
sched.start()