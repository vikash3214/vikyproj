# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Licensetablebkp(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.CharField(db_column='UserId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    profile = models.CharField(db_column='Profile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    producttype = models.CharField(db_column='ProductType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licensetype = models.CharField(db_column='LicenseType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parentlicensekey = models.CharField(db_column='ParentLicenseKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licensekey = models.CharField(db_column='LicenseKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licensefileno = models.CharField(db_column='LicenseFileNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    purpose = models.CharField(db_column='Purpose', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resellercompany = models.CharField(db_column='ResellerCompany', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customercompany = models.CharField(db_column='CustomerCompany', max_length=100, blank=True, null=True)  # Field name made lowercase.
    purchaseorderno = models.CharField(db_column='PurchaseOrderNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    supportstart = models.DateTimeField(db_column='SupportStart')  # Field name made lowercase.
    supportend = models.DateTimeField(db_column='SupportEnd')  # Field name made lowercase.
    customercontactperson = models.CharField(db_column='CustomerContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customeraddress = models.CharField(db_column='CustomerAddress', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    customercontactnumber = models.CharField(db_column='CustomerContactNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customercontactemail = models.CharField(db_column='CustomerContactEmail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    resellercontactperson = models.CharField(db_column='ResellerContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reselleraddress = models.CharField(db_column='ResellerAddress', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    resellercontactnumber = models.CharField(db_column='ResellerContactNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resellercontactemail = models.CharField(db_column='ResellerContactEmail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    hostid = models.CharField(db_column='HostId', max_length=4000)  # Field name made lowercase.
    backuphostid = models.CharField(db_column='BackUpHostId', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    licenseperiod = models.IntegerField(db_column='LicensePeriod', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.CharField(db_column='ExpiryDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licenseedition = models.IntegerField(db_column='LicenseEdition')  # Field name made lowercase.
    rawlifetime = models.IntegerField(db_column='RAWLifeTime')  # Field name made lowercase.
    hourlifetime = models.IntegerField(db_column='HourLifeTime')  # Field name made lowercase.
    daylifetime = models.IntegerField(db_column='DayLifetime')  # Field name made lowercase.
    monthlifetime = models.IntegerField(db_column='MonthLifetime')  # Field name made lowercase.
    numberofdevices = models.IntegerField(db_column='NumberOfDevices')  # Field name made lowercase.
    numberofdesktopnodes = models.IntegerField(db_column='NumberOfDesktopNodes')  # Field name made lowercase.
    applicationlitenodes = models.IntegerField(db_column='ApplicationLiteNodes')  # Field name made lowercase.
    applicationstandardnodes = models.IntegerField(db_column='ApplicationStandardNodes')  # Field name made lowercase.
    applicationadvancednodes = models.IntegerField(db_column='ApplicationAdvancedNodes')  # Field name made lowercase.
    numberofstatistics = models.IntegerField(db_column='NumberOfStatistics')  # Field name made lowercase.
    ping = models.IntegerField(db_column='PING')  # Field name made lowercase.
    netflow = models.IntegerField(db_column='NetFlow')  # Field name made lowercase.
    sla = models.IntegerField(db_column='SLA')  # Field name made lowercase.
    syslog = models.IntegerField(db_column='Syslog')  # Field name made lowercase.
    rmon = models.IntegerField(db_column='RMON')  # Field name made lowercase.
    mpls = models.IntegerField(db_column='MPLS')  # Field name made lowercase.
    ciscosaa = models.IntegerField(db_column='CiscoSAA')  # Field name made lowercase.
    numberofaccounts = models.IntegerField(db_column='NumberOfAccounts')  # Field name made lowercase.
    servicedeskoperators = models.IntegerField(db_column='ServiceDeskOperators')  # Field name made lowercase.
    servicedeskexecutive = models.IntegerField(db_column='ServiceDeskExecutive')  # Field name made lowercase.
    servicedeskcustomer = models.IntegerField(db_column='ServiceDeskCustomer')  # Field name made lowercase.
    vmax = models.IntegerField(db_column='VMAX')  # Field name made lowercase.
    activemon = models.IntegerField(db_column='ActiveMon')  # Field name made lowercase.
    cqms = models.IntegerField(db_column='CQMS')  # Field name made lowercase.
    passivemonitoring = models.IntegerField(db_column='PassiveMonitoring')  # Field name made lowercase.
    nqms = models.IntegerField(db_column='NQMS')  # Field name made lowercase.
    numberofonsites = models.IntegerField(db_column='NumberOfOnsites')  # Field name made lowercase.
    numberofmsponsites = models.IntegerField(db_column='NumberOfMSPOnsites')  # Field name made lowercase.
    inventory = models.IntegerField(db_column='Inventory')  # Field name made lowercase.
    configurationmanagement = models.IntegerField(db_column='ConfigurationManagement')  # Field name made lowercase.
    patchmanagement = models.IntegerField(db_column='PatchManagement')  # Field name made lowercase.
    vmware = models.IntegerField(db_column='VMWARE')  # Field name made lowercase.
    servicedeskincidentmanagement = models.IntegerField(db_column='ServiceDeskIncidentManagement')  # Field name made lowercase.
    servicedeskproblemmanagement = models.IntegerField(db_column='ServiceDeskProblemManagement')  # Field name made lowercase.
    proxyping = models.IntegerField(db_column='ProxyPing')  # Field name made lowercase.
    reason = models.TextField(db_column='Reason', blank=True, null=True)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime')  # Field name made lowercase.
    salesorderno = models.CharField(db_column='SalesOrderNo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'licensetablebkp'


class Tbllicense(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.CharField(db_column='UserId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    profile = models.CharField(db_column='Profile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    producttype = models.CharField(db_column='ProductType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licensetype = models.CharField(db_column='LicenseType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    parentlicensekey = models.CharField(db_column='ParentLicenseKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licensekey = models.CharField(db_column='LicenseKey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licensefileno = models.CharField(db_column='LicenseFileNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    purpose = models.CharField(db_column='Purpose', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resellercompany = models.CharField(db_column='ResellerCompany', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customercompany = models.CharField(db_column='CustomerCompany', max_length=100, blank=True, null=True)  # Field name made lowercase.
    purchaseorderno = models.CharField(db_column='PurchaseOrderNo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    supportstart = models.DateTimeField(db_column='SupportStart')  # Field name made lowercase.
    supportend = models.DateTimeField(db_column='SupportEnd')  # Field name made lowercase.
    customercontactperson = models.CharField(db_column='CustomerContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customeraddress = models.CharField(db_column='CustomerAddress', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    customercontactnumber = models.CharField(db_column='CustomerContactNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customercontactemail = models.CharField(db_column='CustomerContactEmail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    resellercontactperson = models.CharField(db_column='ResellerContactPerson', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reselleraddress = models.CharField(db_column='ResellerAddress', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    resellercontactnumber = models.CharField(db_column='ResellerContactNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    resellercontactemail = models.CharField(db_column='ResellerContactEmail', max_length=200, blank=True, null=True)  # Field name made lowercase.
    hostid = models.CharField(db_column='HostId', max_length=4000)  # Field name made lowercase.
    backuphostid = models.CharField(db_column='BackUpHostId', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    licenseperiod = models.IntegerField(db_column='LicensePeriod', blank=True, null=True)  # Field name made lowercase.
    expirydate = models.CharField(db_column='ExpiryDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    licenseedition = models.IntegerField(db_column='LicenseEdition')  # Field name made lowercase.
    rawlifetime = models.IntegerField(db_column='RAWLifeTime')  # Field name made lowercase.
    hourlifetime = models.IntegerField(db_column='HourLifeTime')  # Field name made lowercase.
    daylifetime = models.IntegerField(db_column='DayLifetime')  # Field name made lowercase.
    monthlifetime = models.IntegerField(db_column='MonthLifetime')  # Field name made lowercase.
    numberofdevices = models.IntegerField(db_column='NumberOfDevices')  # Field name made lowercase.
    numberofdesktopnodes = models.IntegerField(db_column='NumberOfDesktopNodes')  # Field name made lowercase.
    applicationlitenodes = models.IntegerField(db_column='ApplicationLiteNodes')  # Field name made lowercase.
    applicationstandardnodes = models.IntegerField(db_column='ApplicationStandardNodes')  # Field name made lowercase.
    applicationadvancednodes = models.IntegerField(db_column='ApplicationAdvancedNodes')  # Field name made lowercase.
    numberofstatistics = models.IntegerField(db_column='NumberOfStatistics')  # Field name made lowercase.
    ping = models.IntegerField(db_column='PING')  # Field name made lowercase.
    netflow = models.IntegerField(db_column='NetFlow')  # Field name made lowercase.
    sla = models.IntegerField(db_column='SLA')  # Field name made lowercase.
    syslog = models.IntegerField(db_column='Syslog')  # Field name made lowercase.
    rmon = models.IntegerField(db_column='RMON')  # Field name made lowercase.
    mpls = models.IntegerField(db_column='MPLS')  # Field name made lowercase.
    ciscosaa = models.IntegerField(db_column='CiscoSAA')  # Field name made lowercase.
    numberofaccounts = models.IntegerField(db_column='NumberOfAccounts')  # Field name made lowercase.
    servicedeskoperators = models.IntegerField(db_column='ServiceDeskOperators')  # Field name made lowercase.
    servicedeskexecutive = models.IntegerField(db_column='ServiceDeskExecutive')  # Field name made lowercase.
    servicedeskcustomer = models.IntegerField(db_column='ServiceDeskCustomer')  # Field name made lowercase.
    vmax = models.IntegerField(db_column='VMAX')  # Field name made lowercase.
    activemon = models.IntegerField(db_column='ActiveMon')  # Field name made lowercase.
    cqms = models.IntegerField(db_column='CQMS')  # Field name made lowercase.
    passivemonitoring = models.IntegerField(db_column='PassiveMonitoring')  # Field name made lowercase.
    nqms = models.IntegerField(db_column='NQMS')  # Field name made lowercase.
    numberofonsites = models.IntegerField(db_column='NumberOfOnsites')  # Field name made lowercase.
    numberofmsponsites = models.IntegerField(db_column='NumberOfMSPOnsites')  # Field name made lowercase.
    inventory = models.IntegerField(db_column='Inventory')  # Field name made lowercase.
    configurationmanagement = models.IntegerField(db_column='ConfigurationManagement')  # Field name made lowercase.
    patchmanagement = models.IntegerField(db_column='PatchManagement')  # Field name made lowercase.
    vmware = models.IntegerField(db_column='VMWARE')  # Field name made lowercase.
    servicedeskincidentmanagement = models.IntegerField(db_column='ServiceDeskIncidentManagement')  # Field name made lowercase.
    servicedeskproblemmanagement = models.IntegerField(db_column='ServiceDeskProblemManagement')  # Field name made lowercase.
    proxyping = models.IntegerField(db_column='ProxyPing')  # Field name made lowercase.
    reason = models.TextField(db_column='Reason', blank=True, null=True)  # Field name made lowercase.
    creationtime = models.DateTimeField(db_column='CreationTime')  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime')  # Field name made lowercase.
    salesorderno = models.CharField(db_column='SalesOrderNo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblLicense'

