from apscheduler.schedulers.blocking import BlockingScheduler
from helper import your_function_a, your_function_b

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes='30')
def print_data():
	print("Have a good day!")

@sched.scheduled_job('cron', day_of_week='sat-sun', hour='8-14', minute='0-59/10', timezone='America/New_York')
def update_a():
 	your_function_a()

@sched.scheduled_job('cron', day_of_week='fri', hour='15-19/2', timezone='America/New_York')
def update_b():
 	your_function_b()

sched.start()



# from apscheduler.schedulers.blocking import BlockingScheduler

# sched = BlockingScheduler()


# @sched.scheduled_job('interval', minutes=3)
# def timed_job():
#     print('This job is run every three minutes.')


# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')


# sched.start()
