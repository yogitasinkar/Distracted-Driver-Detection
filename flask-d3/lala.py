import os
import base64
import cv2
from io import BytesIO
from flask import Flask, render_template, url_for, redirect, request,jsonify
from werkzeug.exceptions import BadRequest
import numpy as  np
import PIL.Image
import urllib.request
import requests

from selenium import webdriver

driver = webdriver.Firefox(executable_path = 'F:\\Yogita\\Knock-Knock\\ml\\Outp\\Project sem 8\\_Project\\geckodriver-v0.24.0-win64\\geckodriver.exe')

url = "http://192.168.43.163:8081/out.jpg"
cv2.namedWindow("RaspiCam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("RaspiCam",600,500)

driver.get("http://192.168.43.163:5000/buzz")

while True:
    img_resp = requests.get(url, verify=False)
    img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
    img = cv2.imdecode(img_arr, -1)

    # guess = str(evaluate_image(Image(pil2tensor(img, np.float32).div_(255))))

    # ans = description_dict[guess]
    # pred = guess + " " + ans
    # print(guess)
    #
    # if guess!='c0':
    #     elem = driver.find_element_by_xpath("/html/body/form/button")
    #     elem.click()

    cv2.putText(img, "pred" ,(30,40),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,139), 2)
    cv2.imshow("RaspiCam", img)

    cv2.waitKey(1)
