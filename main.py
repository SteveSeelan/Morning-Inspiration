from twilio.rest import Client
import utils
import time
import schedule
from quoters import Quote

client = Client(utils.account_sid, utils.auth_token)

def send_msg():
    message = Quote.print()
    client.messages.create(
        body=message,
        from_=utils.twilio_phone_number,
        to=utils.your_phone_number
    )

if __name__ == '__main__':
    schedule.every().day.at(utils.time_of_day).do(send_msg)

    while True:
        schedule.run_pending()
        time.sleep(1)