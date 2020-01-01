# pages/views.py
from django.http import HttpResponse
from facerecog.models import EmpDetails


def homePageView(request):
    return HttpResponse('Hello from Django!')

def getEmpDetails(request):
    return HttpResponse(EmpDetails.objects.all())