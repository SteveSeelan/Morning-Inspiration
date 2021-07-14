# Morning-Inspiration
Automatically sends an inspirational quote to your phone every morning

## 1. Install requirements
```bash
npm install twilio-cli -g
python -m pip install -r quoters
python -m pip install -r schedule

```

## 2. Configure your settings in `utils.py`.
### Sign up for free twilio account
https://www.twilio.com/try-twilio

```py
account_sid = 'ACd29as291d09032d942848da71897a4817b' #example
auth_token = 'f8a5f8as5f785g61j6j45gfh3fgh623g5' #example
# enter accound sid and auth token from your free twilio account
twilio_phone_number = 'replace with twilio phone number'
your_phone_number = 'replace with your phone number'
# enter phone numbers using the format: "+15555555555"
time_of_day = "07:00"
# time of day in 24-hour standard, so for 2pm enter "14:00"
```

Note: If you want to send a message everyday at 6:45 AM, you will need to set `time_of_day = "06:45"` in `utils.py`

## 3. Run the script
```bash
python main.py
```
Note: If you want run in background
