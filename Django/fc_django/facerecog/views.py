# pages/views.py
import os
import base64
from django.http import HttpResponse
from .models import EmpDetails,Attendance
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from os import path
import json
import cv2
import numpy as np
import re
from re import search
import datetime
from datetime import date



def homePageView(request):
    return HttpResponse('Hello from Django!')

def getEmpDetails(request):
    data=list(EmpDetails.objects.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def addEmployee(request):
    response=''
    newemp = EmpDetails()

    if request.method == "POST":
        response='Success'
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)


        newemp.firstname=body_data['firstname']
        newemp.lastname = body_data['lastname']
        if EmpDetails.objects.filter(firstname=body_data['firstname'],lastname=body_data['lastname']).first()!=None:
            print("Duplicate")
            newemp=None
            response = {'status': 'Failure', 'responseObject': newemp}
        elif body_data['firstname'].strip()!="" and body_data['lastname'].strip()!="":

            newemp.save()
            newemp=EmpDetails.objects.filter(firstname=body_data['firstname'],lastname=body_data['lastname']).first()
            print(newemp.id)
            newemp={'id':newemp.id,'firstname':newemp.firstname,'lastname':newemp.lastname}
            response={'status':'Success','responseObject':newemp}
        else:
            response = {'status': 'Failure', 'responseObject': None}
    else:
        response={'status':'Failure','responseObject':None}
    return JsonResponse(response, safe=False)

@csrf_exempt
def updateEmployee(request):
    response = ''
    newemp = EmpDetails()
    try:
        if request.method == "PUT":
            response = 'Success'
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)


            if EmpDetails.objects.get(id=body_data['id']) != None and body_data['firstname'].strip()!="" and body_data['lastname'].strip()!="":
                #newemp.firstname = body_data['firstname']
                #newemp.lastname = body_data['lastname']
                newemp=EmpDetails.objects.filter(id=body_data['id']).update(firstname=body_data['firstname'],lastname=body_data['lastname'])
                #newemp.save(update_fields=["active"])
                #print(newemp.id)
                #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
                response = {'status': 'Success', 'responseObject': None}
                print("Success")
            else:
                print("Does not exist.")
                newemp = None
                response = {'status': 'Failure', 'responseObject': None}

        else:
            response = {'status': 'Failure', 'responseObject': None}
    except:
        print("There is some problem.")
        response = {'status': 'Failure', 'responseObject': None}
    return JsonResponse(response, safe=False)

@csrf_exempt
def deleteEmployee(request):
    response = ''
    newemp = EmpDetails()

    try:
        if request.method == "DELETE":
            response = 'Success'
            #body_unicode = request.body.decode('utf-8')
            #body_data = json.loads(body_unicode)
            id = request.GET['id']
            if EmpDetails.objects.get(id=id) != None:
                newemp=EmpDetails.objects.get(id=id)
                newemp.delete()
                response = {'status': 'Success', 'responseObject': None}
            else:
                #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
                response = {'status': 'Failure', 'responseObject': None}
        else:
            response = {'status': 'Failure', 'responseObject': None}

    except:
        print("There's something wrong")
        #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
        response = {'status': 'Failure', 'responseObject': None}
    return JsonResponse(response, safe=False)

@csrf_exempt
def savePhoto(request):
    response=''
    if request.method == "POST":
        try:

            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            arr=body_data['photo'].split(",")

            if EmpDetails.objects.get(id=body_data['id']) != None:

                cwdname=os.path.abspath(os.getcwd())+os.path.sep+"TrainingData"+os.path.sep+str(body_data['id'])
                filepath = os.path.join(cwdname, body_data['filename'])
                if not os.path.exists(cwdname):
                    os.makedirs(cwdname)
                if path.exists(filepath)==False:
                    with open(filepath, "wb") as fh:
                        fh.write(base64.decodebytes(arr[1].encode('utf-8')))
                        response = {'status': 'Success', 'responseObject': None}
                        print("Success- -1")
                        faces=labels_for_training_data(cwdname)
                        print("Interim")
                        face_recognizer = train_classifier(faces, body_data['id'])
                        print("Success-0")
                        face_recognizer.write(cwdname+os.path.sep+'trainingData.yml')
                        print("Success-1")
                else:
                    response = {'status': 'Failure', 'responseObject': None}


            else:
                print("Else")
                response = {'status': 'Failure', 'responseObject': None}
        except Exception as e:
            print("PROBLEM.:-"+str(e))
            response = {'status': 'Failure', 'responseObject': None}
    else:
        response = {'status': 'Failure', 'responseObject': "Not Allowed"}
    return JsonResponse(response)

@csrf_exempt
def markAttendance(request):
    response = {'status': 'Failure', 'responseObject': None}
    try:

        result=0
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        arr = body_data['photo'].split(",")
        os.makedirs("Temp")
        fp=os.path.abspath(os.getcwd())+os.path.sep+"Temp"
        fp=os.path.join(fp, "temp.jpg")
        with open(fp, "wb") as fh:
            fh.write(base64.decodebytes(arr[1].encode('utf-8')))

        test_img = cv2.imread(fp)  # test_img path
        faces_detected, gray_img = faceDetection(test_img)
        print("faces_detected:", faces_detected)
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        ids=EmpDetails.objects.values('id')

        for i in range(len(ids)):
            r = ids[i]
            r = json.dumps(r)
            loaded_r = json.loads(r)

            if os.path.exists(os.getcwd()+os.path.sep+ "TrainingData" + os.path.sep + str(loaded_r['id'])+os.path.sep+"trainingData.yml"):
                print("L1")
                filepath=os.getcwd()+os.path.sep+ "TrainingData" + os.path.sep + str(loaded_r['id'])+os.path.sep+"trainingData.yml"
                face_recognizer.read(filepath)
                print("L2")
                for face in faces_detected:
                    (x, y, w, h) = face
                    roi_gray = gray_img[y:y + h, x:x + h]
                    label, confidence = face_recognizer.predict(roi_gray)  # predicting the label of given image
                    if (confidence < 75):
                        continue
                    else:



                        if datetime.datetime.today().weekday()==0 or datetime.datetime.today().weekday()==6:
                            response = {'status': 'Failure', 'responseObject': None}
                        else:
                            att = Attendance()
                            att.eid = label
                            att.attendance = 1
                            now = datetime.datetime.now()
                            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
                            print("date and time:", date_time)
                            att.datetime=date_time

                            att.save()
                            response = {'status': 'Present', 'responseObject': None}
                        break

                break
    except Exception as e:
        print("Exception is.:-"+str(e))
        response = {'status': 'Failure', 'responseObject': None}
        fp = os.path.join(os.path.abspath(os.getcwd())+os.path.sep+"Temp", "temp.jpg")
    os.remove((os.path.abspath(os.getcwd())+os.path.sep+"Temp"+os.path.sep+"temp.jpg"))
    os.rmdir(os.path.abspath(os.getcwd())+os.path.sep+"Temp")
    return JsonResponse(response, safe=False)

def getAttendance(request):
    data = list(Attendance.objects.values())
    for i in range(len(data)):
        data[i]['datetime']=data[i]['datetime'].strftime("%m/%d/%Y, %H:%M:%S")
    return JsonResponse(data, safe=False)


def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)#convert color image to grayscale
    print("H1")
    cwdname = os.path.abspath(os.getcwd() + os.path.sep + "haarcascade_frontalface_default.xml")
    print("H2")
    face_haar_cascade=cv2.CascadeClassifier(cwdname)#Load haar classifier
    faces=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)#detectMultiScale returns rectangles

    print("H3")
    return faces,gray_img

#Given a directory below function returns part of gray_img which is face alongwith its label/ID
def labels_for_training_data(directory):
    faces=[]

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            print(filename)
            if filename.startswith("."):
                print("Skipping system file")#Skipping files that startwith .
                continue
            #elif search("jpg",filename) and search("png",filename) and search("JPG",filename) and search("PNG",filename):
            print("Training...")
            id=os.path.basename(path)#fetching subdirectory names
            img_path=os.path.join(path,filename)#fetching image path
            print("img_path:",img_path)
            print("id:",id)
            test_img=cv2.imread(img_path)#loading each image one by one
            print("T1")
            if test_img is None:
                print("Image not loaded properly")
                continue
            print("T2")
            faces_rect,gray_img=faceDetection(test_img)#Calling faceDetection function to return faces detected in particular image
            if len(faces_rect)!=1:
                continue #Since we are assuming only single person images are being fed to classifier
            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from grayscale image
            faces.append(roi_gray)
    print(len(faces))
    return faces


#Below function trains haar classifier and takes faces,faceID returned by previous function as its arguments
def train_classifier(faces,faceID):
    faceID=np.full(len(faces),faceID)
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,faceID)
    return face_recognizer

#Below function draws bounding boxes around detected face in image
def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)

#Below function writes name of person for detected label
def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),4)

