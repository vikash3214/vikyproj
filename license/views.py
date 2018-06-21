from license.models import Tbllicense
from django.http import HttpResponse

from django.shortcuts import render


# Create your views here.
def getLicDetails(request):
    #objects=Tbllicense.objects.raw("select id,LicenseKey,ResellerCompany,CustomerCompany,PurchaseOrderNo,SupportStart,SupportEnd,ExpiryDate,SalesOrderNo,CreationTime from tblLicense where LicenseType in ('Production','Subscription')")
    objects=Tbllicense.objects.all()
    return render(request, 'list.html', locals())
