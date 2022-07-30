from datetime import datetime
from dateutil.relativedelta import relativedelta
import time

from flask import redirect
from razorpay import Client


RAZORPAY_KEY_ID = "RAZORPAY_KEY_ID"
RAZORPAY_SECRET = "RAZORPAY_SECRET"
RAZORPAY_PLAN_ID = "RAZORPAY_PLAN_ID"


client = Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET))


def create_plan(request):
    date_after_month = datetime.today()+ relativedelta(months=1)
    expire_by_timestamp = time.mktime(date_after_month.timetuple())
    response = client.subscription.create({
        "plan_id": RAZORPAY_PLAN_ID,
        "customer_notify": 1,
        "quantity": 1,
        "total_count": 99, # number of months
        "expire_by": expire_by_timestamp,
    })
    return redirect(response['short_url'])

