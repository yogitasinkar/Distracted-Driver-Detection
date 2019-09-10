import time
from sinchsms import SinchSMS

# number = '+916351751675'
number = '+919725151620'
message = 'Alert1'

your_app_key = "5ce475f2-a0ac-4a7b-85cf-bb49cb983a36"
your_app_secret = "RytWbVR1JE+lA98GWq51Rg=="
client = SinchSMS(your_app_key, your_app_secret)

print("Sending '%s' to %s" % (message, number))
response = client.send_message(number, message)
message_id = response['messageId']

response = client.check_status(message_id)
while response['status'] != 'Successful':
    print(response['status'])
    time.sleep(1)
    response = client.check_status(message_id)
    print(response['status'])
