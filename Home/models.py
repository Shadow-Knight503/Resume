from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from cloudinary.models import CloudinaryField as BaseCloudinaryField


class CloudinaryField(BaseCloudinaryField):
    def upload_options(self, model_instance):
        return {
            'public_id': model_instance.name,
            'filename': Profile.Name,
            'unique_filename': True,
            'overwrite': True,
            'resource_type': 'auto',
            'tags': ['Prof_Pic'],
            'invalidate': True,
            'quality': 'auto:eco',
            'folder': f'Resume/{Profile.Name}/'
        }


# Create your models here.
class Profile(models.Model):
    Acct = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=100, default="Some Name")
    Work = models.CharField(max_length=100, default="Some Work")
    PPic = CloudinaryField('Profile', resource_type="image")
    Abut = models.TextField(max_length=500, default="Description")

    def __str__(self):
        return self.Name


class Edu(models.Model):
    Acct = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    Inst = models.CharField(max_length=150, default="Institute")
    Durt = models.CharField(max_length=100, default="2020")
    Abut = models.TextField(max_length=500, default="Etc")

    def __str__(self):
        return self.Inst


class Work(models.Model):
    Acct = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    Comp = models.CharField(max_length=150, default="Company")
    Durt = models.CharField(max_length=100, default="2020")
    Abut = models.TextField(max_length=500, default="Etc")

    def __str__(self):
        return self.Comp


class Lang(models.Model):
    Acct = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=100, default="Lang")
    Dsrp = models.TextField(max_length=500, default="Etc")
    Cred = models.CharField(max_length=500, default="None")

    def nme(self):
        return self.Name.replace(' ', '+')

    Icon = CloudinaryField(public_id=nme, use_filename=False, unique_filename=False, resource_type="image",
                           folder=f'Resume/LangIcons/')

    def __str__(self):
        return self.Name


class Contact(models.Model):
    Acct = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    Text = models.CharField(max_length=100, default="Rando")
    Link = models.CharField(max_length=250, default="")
    Icon = CloudinaryField('Icon', resource_type="image")

    def __str__(self):
        return self.Text


class Credit(models.Model):
    Acct = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    Text = models.CharField(max_length=100, default="Rando")
    Source = models.CharField(max_length=250, default="Linkie")

    def __str__(self):
        return self.Text


class Project(models.Model):
    Acct = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    Title = models.CharField(max_length=100, default="Project")
    Dscrp = models.TextField(max_length=500, default="Etc")
    Lang = models.ManyToManyField(Lang)
    Git = models.CharField(max_length=100, default="None")
    Link = models.CharField(max_length=100, default="None")

    def ttl(self):
        return self.Title.replace(' ', '+')

    Cover = CloudinaryField(public_id=ttl, use_filename=False, unique_filename=False, resource_type="image",
                            folder=f'Resume/ProjectCovers/')

    def __str__(self):
        return self.Title
