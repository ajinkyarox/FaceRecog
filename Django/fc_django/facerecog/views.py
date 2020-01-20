# pages/views.py
import os
import base64
from django.http import HttpResponse
from facerecog.models import EmpDetails,Attendance
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from os import path
import json

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
    resonse=''

    return JsonResponse(resonse)

def getAttendance(request):
    data = list(Attendance.objects.values())
    return JsonResponse(data, safe=False)