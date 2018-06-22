from license.models import Tbllicense
from django.http import HttpResponse
from django.http import JsonResponse

from django.shortcuts import render
from datetime import datetime

x = datetime.strptime('2017-06-21 18:21', '%Y-%m-%d %H:%M')
y = datetime.strptime('2018-07-07 15:15', '%Y-%m-%d %H:%M')

print (x)
print (y)

# Create your views here.
def getLicDetails(request):
    objects=Tbllicense.objects.filter(creationtime__range=(x,y)).filter(licensetype__in=('Production','Subscription'))
    return render(request, 'list.html', locals())



