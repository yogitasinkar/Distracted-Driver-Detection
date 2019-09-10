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

# from pynput.keyboard import Key, Controller

import time

def evaluate_image(img) -> str:
    pred_class, pred_idx, outputs = trained_model.predict(img)
    return pred_class


def load_model():
    export_file_name = 'export.pkl'
    classes = ['c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9']
    learn = load_learner(path, export_file_name)
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

@app.route('/demo_video/analyse_vi')
def analyse_vi():
    from selenium import webdriver

    driver = webdriver.Firefox(executable_path = 'F:\\Yogita\\Knock-Knock\\ml\\Outp\\Project sem 8\\_Project\\geckodriver-v0.24.0-win64\\geckodriver.exe')


    # url = "http://192.168.43.1:8080/shot.jpg"
    # url = "http://192.168.43.120/html/cam_pic.php"
    url = "http://192.168.43.163:8081/out.jpg"
    cv2.namedWindow("RaspiCam", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("RaspiCam",600,500)

    timestext = 0
    timestalk = 0
    timesdist = 0

    driver.get("http://192.168.43.163:5000/buzz")
    # elem = driver.find_element_by_xpath("/html/body/form/button")
        # elem.click()

    while True:
        img_resp = requests.get(url, verify=False)
        img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
        img = cv2.imdecode(img_arr, -1)

        guess = str(evaluate_image(Image(pil2tensor(img, np.float32).div_(255))))

        ans = description_dict[guess]
        pred = guess + " " + ans
        print(guess)

        if guess!='c0':
            elem = driver.find_element_by_xpath("/html/body/form/button")
            elem.click()

        cv2.putText(img, pred ,(30,40),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,139), 2)
        cv2.imshow("RaspiCam", img)

        cv2.waitKey(1)
            


    return ('', 204)

@app.route('/demo_video/analyse_vi2')
def analyse_vi2():
    cv2.destroyWindow("AndroidCam")

    return render_template('home.html')


@app.route('/motivation')
def motivation():
    return 'Motivation'


if __name__ == '__main__':
    app.run(debug=True)
