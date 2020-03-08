import schedule
import time
import helper


def job():
    print("I'm working...")
    print(time.ctime())
    helper.add_file()
    helper.record_success()


schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

schedule.every().minute.at(":15").do(helper.hello_world)
schedule.every().minute.at(":30").do(helper.goodbye)
schedule.every().minute.at(":45").do(helper.flavor_text)

while True:
    schedule.run_pending()
    time.sleep(1)
