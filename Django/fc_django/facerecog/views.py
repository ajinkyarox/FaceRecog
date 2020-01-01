# pages/views.py
from django.http import HttpResponse
from facerecog.models import EmpDetails
from django.http import JsonResponse


def homePageView(request):
    return HttpResponse('Hello from Django!')

def getEmpDetails(request):
    data=list(EmpDetails.objects.values())
    return JsonResponse(data, safe=False)