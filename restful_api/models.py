from django.db import models


class Users(models.Model):
    firstname = models.CharField(max_length=100, blank=False, default='')
    lastname = models.CharField(max_length=100, blank=False, default='')
    username = models.CharField(max_length=255, blank=False, default='')
    password = models.CharField(max_length=255, blank=False, default='')
    userType = models.CharField(max_length=1, blank=False, default='')
    isLock = models.CharField(max_length=1, blank=False, default='')
    imgURL = models.CharField(
        max_length=255, blank=False, default='')
    occupationStatus = models.CharField(
        max_length=100, blank=False, default='')
    occupationDetails = models.CharField(max_length=255, blank=False, default='')
    occupationPositionWork = models.CharField(
        max_length=150, blank=False, default='')
    nameofschool = models.CharField(max_length=100, blank=False, default='')
    degree = models.CharField(max_length=100, blank=False, default='')
    address = models.TextField(blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tokenization(models.Model):
    userID = models.IntegerField()
    token = models.CharField(max_length=255, blank=False, default='')
    lastRoute = models.CharField(max_length=100, blank=False, default='')
    isDestroyed = models.CharField(max_length=1, blank=False, default='')
    isvalid = models.CharField(max_length=1, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Branches(models.Model):
    branchName = models.CharField(max_length=100, blank=False, default='')
    branchDescription = models.CharField(max_length=255, blank=False, default='')
    branchImg = models.CharField(max_length=255, blank=False, default='')
    branchRoute = models.CharField(max_length=100, blank=False, default='')
    branchIsActive = models.CharField(max_length=1, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
