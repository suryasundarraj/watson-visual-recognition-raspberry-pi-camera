import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition
import picamera
import subprocess
from time import sleep
import os
import zipfile

visual_recognition = VisualRecognition('2016-05-20',api_key='dec041de3393d4b66120d22e628b81f2f3c1e9c0')

with open(join(dirname(__file__), 'surya.zip'), 'rb') as surya, \
       open(join(dirname(__file__), 'vijay.zip'), 'rb') as vijay:
       print(json.dumps(visual_recognition.create_classifier('face', surya_positive_examples=surya, vijay_positive_examples=vijay), indent=2))
