import os
import base64
import cv2
from io import BytesIO
from flask import Flask, render_template, url_for, redirect, request,jsonify
from werkzeug.exceptions import BadRequest
import numpy as  np
import PIL.Image
import urllib.request


from fastai import *
from fastai.vision import *
path = Path(__file__).parent

from pynput.keyboard import Key, Controller

import time

def evaluate_image(img) -> str:
    pred_class, pred_idx, outputs = trained_model.predict(img)
    return pred_class


def load_model():
    export_file_name = 'export.pkl'
    classes = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
    learn = load_learner(path, export_file_name)
    # learn.load('clabby-stage-2')
    return learn


app = Flask(__name__)
trained_model = load_model()

description_dict = {"c0": "safe driving","c1": "texting - right","c2": "talking on the phone - right","c3": "texting - left","c4": "talking on the phone - left","c5": "operating the radio","c6": "drinking","c7": "reaching behind","c8": "hair and makeup","c9": "talking to passenger"}



@app.route('/')
def home():
    return render_template('home.html')

#==================#
# DEMO IMAGE
#==================#

@app.route('/demo_image')
def demo_image():
    return render_template('demo_image.html')

@app.route('/demo_image/analyse_im', methods=['POST'])
def analyse_im():
    """Evaluate the image!"""
    input_file = request.files.get('file')
    if not input_file:
        return BadRequest("File is not present in the request")
    if input_file.filename == '':
        return BadRequest("Filename is not present in the request")
    if not input_file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        return BadRequest("Invalid file type")


    input_buffer = BytesIO()
    input_file.save(input_buffer)
    print(type(input_file))

    guess = evaluate_image(open_image(input_buffer))
    ans = description_dict[str(guess)]

    return jsonify({
        'ans': ans,
        'guess': str(guess)
    })

#==================#
# DEMO VIDEO
#==================#

# @app.route('/demo_video')
# def demo_video():
#
#     # for i in range(10):
#     img_data = requests.get("https://192.168.43.1:8080/shot.jpg", verify=False).content
#     with open(f'shot.jpg', 'wb') as handler:
#         handler.write(img_data)
#     # img = open_image(f'shot{i}.jpg')
#     img = IPython.display.Image(filename='shot.jpg')
#     # img = open_image("shot.jpg")
#
#
#     # guess = evaluate_image(Image(pil2tensor(img, np.float32).div_(255)))
#     guess =evaluate_image(pil2tensor(PIL.Image.open(img), np.float32).div_(255))
#     ans = description_dict[str(guess)]
#
#     print(ans)
#     return render_template("demo_video.html", image=img)
#         # return send_file('shot.jpg')
#
# @app.route('/demo_video/analyse_vi')
# def analyse_vi():
#     # img =   open_image(f'shot{i}.jpg')
#     return send_file('shot.jpg')



@app.route('/demo_video')
def demo_video():
    return render_template('demo_video.html')
#
# @app.route('/demo_video/analyse_vi')
# def analyse_vi():
#     url = "http://192.168.43.1:8080/shot.jpg"
#
#     # url = "file:///C:/Users/Yogita/Desktop/sim/Webp.net-gifmaker%20(1).gif"
#     cv2.namedWindow("AndroidCam", cv2.WINDOW_NORMAL)
#     cv2.resizeWindow("AndroidCam",600,500)
#     pred = "Detecting.."
#     times = 0
#
#
#     number = '+916351751675'
#     message = 'texting'
#
#     # your_app_key = "5ce475f2-a0ac-4a7b-85cf-bb49cb983a36"
#     your_app_key = "c6ad0af4-77bf-4995-856e-0e0943a33501"
#     your_app_secret = "0Hdkaxv1MEqmEIitvyiQpw=="
#     # your_app_secret = "RytWbVR1JE+lA98GWq51Rg=="
#     client = SinchSMS(your_app_key, your_app_secret)
#
#
#     while True:
#         img_resp = requests.get(url, verify=False)
#         img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
#         img = cv2.imdecode(img_arr, -1)
#
#         guess = str(evaluate_image(Image(pil2tensor(img, np.float32).div_(255))))
#         ans = description_dict[guess]
#         pred = guess + " " + ans
#         print(guess)
#         if guess == 'c0':
#             times = 0
#
#         if guess !='c0':
#             times = times + 1
#             if times > 3:
#                 print("ALERTT")
#                 times = 0
#                 print("Sending '%s' to %s" % (message, number))
#                 response = client.send_message(number, message)
#                 message_id = response['messageId']
#
#                 response = client.check_status(message_id)
#                 while response['status'] != 'Successful':
#                     print(response['status'])
#                     # time.sleep(1)
#                     response = client.check_status(message_id)
#                     print(response['status'])
#
#
#         cv2.putText(img, pred,(30,40),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
#         # cv2.putText(img, "Press s to exit",(10,50),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
#         cv2.imshow("AndroidCam", img)
#
#         if cv2.waitKey(1) == ord('s'):
#             break
#
#
#     return ('', 204)



@app.route('/demo_video/analyse_vi')
def analyse_vi():
    from selenium import webdriver
    driver = webdriver.Firefox(executable_path = 'F:\\Yogita\\ml\\geckodriver-v0.24.0-win64\\geckodriver.exe')


    url = "http://192.168.43.1:8080/shot.jpg"

    cv2.namedWindow("AndroidCam", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("AndroidCam",600,500)

    timestext = 0
    timestalk = 0
    timesdist = 0

    driver.get("http://192.168.43.1:8080/")
    elem0 = driver.find_element_by_link_text("Tasker events control")
    elem0.click()
    # elem2 = driver.find_element_by_xpath('//*[@id="tasker_events"]/div/div/div/div[3]/button[1]')
    elem2 = driver.find_element_by_xpath('//*[@id="tasker_events"]/div/div/div/div[3]/button[2]')
    elem3 = driver.find_element_by_xpath('//*[@id="tasker_events"]/div/div/div/div[3]/button[3]')
    elem4 = driver.find_element_by_xpath('//*[@id="tasker_events"]/div/div/div/div[2]/button[1]')

    while True:
        img_resp = requests.get(url, verify=False)
        img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
        img = cv2.imdecode(img_arr, -1)

        guess = str(evaluate_image(Image(pil2tensor(img, np.float32).div_(255))))
        # if guess =='c8':
        #     guess = 'c0'
        ans = description_dict[guess]
        pred = guess + " " + ans
        print(guess)
        if guess== 'c0':
            timestext = 0
            timesdist = 0
            timestalk = 0
        elif guess=='c1' or guess == 'c3':
            timesdist = 0
            timestalk = 0
            timestext +=1
            if timestext>3:
                print('Texting')
                elem2.click()
        elif guess=='c2' or guess == 'c4':
            timestext = 0
            timesdist = 0
            timestalk +=1
            if timestalk>3:
                print('Talking')
                elem3.click()
        else:
            timestext = 0
            timestalk = 0
            timesdist +=1
            if timesdist>3:
                print('Distracted')
                elem4.click()

        cv2.putText(img, pred,(30,40),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.imshow("AndroidCam", img)

        if cv2.waitKey(1) == ord('s'):
            break


    return ('', 204)

@app.route('/demo_video/analyse_vi2')
def analyse_vi2():
    cv2.destroyWindow("AndroidCam")

    return render_template('home.html')


@app.route('/motivation')
def motivation():
    return 'Motivation'


if __name__ == '__main__':
    app.run()
