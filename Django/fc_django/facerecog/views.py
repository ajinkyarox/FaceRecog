# pages/views.py
from django.http import HttpResponse
from facerecog.models import EmpDetails
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
        else:

            newemp.save()
            newemp=EmpDetails.objects.filter(firstname=body_data['firstname'],lastname=body_data['lastname']).first()
            print(newemp.id)
            newemp={'id':newemp.id,'firstname':newemp.firstname,'lastname':newemp.lastname}
            response={'status':'Success','responseObject':newemp}
    else:
        response={'status':'Failure','responseObject':None}
    return JsonResponse(response, safe=False)