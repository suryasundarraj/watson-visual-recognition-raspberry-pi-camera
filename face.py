import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3 as VisualRecognition
import picamera
from time import sleep
import os
import zipfile

#update the clasifier id here
classifier_ids = ["face_429689582"]

#Update the api key 
visual_recognition = VisualRecognition('2016-05-20',api_key='dec041de3393d4b66120d22e69999999999c0')

directory = "image"
url = None
file = open("image.zip","rb")

#intialize the camera 
camera = picamera.PiCamera()

if not os.path.exists(directory):
    os.makedirs(directory)

zipf = zipfile.ZipFile('image.zip', 'w', zipfile.ZIP_DEFLATED)
for i in range(10):
	filePath = 'image/'+str(i)+'.jpg'
	camera.capture(filePath)
	sleep(0.1)
	zipf.write(filePath , os.path.basename(filePath))
zipf.close()

print "Please Wait..Image Processing Started"

data = json.dumps(visual_recognition.classify(file,url,classifier_ids), indent=2)

data = json.loads(data)

print data

names = {}

if data.has_key("images"):
	for i in range(len(data["images"])):
		if(len(data["images"][i]["classifiers"]) > 0):
			classifiers = data["images"][i]["classifiers"][0]
			if(classifiers.has_key("name")):
				if(classifiers["name"] == "face"):
					if(classifiers["classes"][0]["score"] > 0.5):
						if not names.has_key(classifiers["classes"][0]["class"]):
							names.setdefault(classifiers["classes"][0]["class"],1)
						else:
							names[classifiers["classes"][0]["class"]] = names[classifiers["classes"][0]["class"]] + 1

prev_value = 0
name = None
if len(names) > 0:
	for key in names:
		value = names[key]
		if value > prev_value:
			name = key
			prev_value = value

if name == "surya":
	print("Hi Surya, Watson successfully recognized")
else:
	print("Sorry, not able to recognize you")

print "The End"
