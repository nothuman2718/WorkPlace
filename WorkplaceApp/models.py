from django.db import models
import uuid


# Create your models here.

class studentDataTable(models.Model):
    objects = None
    stuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=200)
    tel = models.CharField(max_length=50)
    university = models.CharField(max_length=200)
    degree = models.TextField(blank=True, null=True)
    linkedin = models.CharField(blank=True, null=True, max_length=1000)
    createtimestamp = models.DateTimeField(auto_now_add=True)
    updatetimestamp = models.DateTimeField(auto_now_add=True)
    profilepic = models.ImageField(null=True, blank=True)
    username = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=100)
    resume = models.FileField(null=True, blank=True)


class companyDataTable(models.Model):
    objects = None
    comid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    companyname = models.CharField(max_length=100)
    comregno = models.CharField(max_length=500)
    address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=200)
    tel = models.CharField(max_length=50)
    preffield = models.CharField(max_length=300)
    linkedin = models.CharField(blank=True, null=True, max_length=1000)
    createtimestamp = models.DateTimeField(auto_now_add=True)
    updatetimestamp = models.DateTimeField(auto_now_add=True)
    profilepic = models.ImageField(null=True, blank=True)
    username = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=100)


class flyerdata(models.Model):
    flyerid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    company = models.ForeignKey(companyDataTable, on_delete=models.CASCADE, null=True, blank=True)
    jobfield = models.CharField(max_length=100)
    jobpost = models.CharField(max_length=100)
    salary = models.CharField(max_length=50)
    location = models.CharField(max_length=1000)
    flyerimage = models.ImageField()
    createtimestamp = models.CharField(max_length=30)
    updatetimestamp = models.CharField(max_length=30)


class studentfavorite(models.Model):
    flyer = models.ForeignKey(flyerdata, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(studentDataTable, on_delete=models.CASCADE, null=True, blank=True)


class studentapply(models.Model):
    flyer = models.ForeignKey(flyerdata, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(studentDataTable, on_delete=models.CASCADE, null=True, blank=True)


class message(models.Model):
    msgid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    msg = models.TextField(blank=True, null=True)
    student = models.ForeignKey(studentDataTable, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(companyDataTable, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.CharField(max_length=200)
    senderID = models.CharField(max_length=200, blank=True, null=True)
    Receiver = models.CharField(max_length=200)
    ReceiverID = models.CharField(max_length=200, blank=True, null=True)
    MarkAsRead = models.CharField(max_length=5, blank=True, null=True)
    createtimestamp = models.CharField(max_length=30)


class StuNotification(models.Model):
    StuNotificationId = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    notification = models.TextField(blank=True, null=True)
    student = models.ForeignKey(studentDataTable, on_delete=models.CASCADE, null=True, blank=True)
    createtimestamp = models.CharField(max_length=30, blank=True, null=True)
    MarkAsRead = models.CharField(max_length=5, blank=True, null=True)


class ComNotification(models.Model):
    ComNotificationId = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    notification = models.TextField(blank=True, null=True)
    company = models.ForeignKey(companyDataTable, on_delete=models.CASCADE, null=True, blank=True)
    createtimestamp = models.CharField(max_length=30, blank=True, null=True)
    MarkAsRead = models.CharField(max_length=5, blank=True, null=True)