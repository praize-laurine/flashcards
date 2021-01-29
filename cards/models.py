from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime as dt


# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to = 'images/', default = 'image.jpeg')
    # image = CloudinaryField('images')
    name = models.CharField(max_length = 30)
    content = models.TextField()
    # location = models.ForeignKey('Location', on_delete=models.SET_NULL, default = '', null=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, default='')
    date_created= models.DateField(auto_now_add=True )


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    

    @classmethod
    def search_by_subject(cls,search_term):
        images = cls.objects.filter(subject__name__icontains = search_term)
        return images  

    def update_image(self, Name=None, subject=None):
        self.name = Name if Name else self.Name
        self.subject = subject if subject else self.subject
        self.save()    

    def __str__(self):
        return self.name
     



class Subject(models.Model):
    subject_name = models.CharField(max_length = 30)

    def save_subject(self):
        self.save()

    def delete_subject(self):
        self.delete()

    def __str__(self):
        return self.subject_name


class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)

    def __str__(self):
        return self.location_name    

# class Profile(models.Model):
#     profile_pic = models.ImageField(upload_to='profile/', blank ='true',default='default.png')
#     bio = models.TextField()
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     name = models.CharField(blank=True, max_length=120)
#     # date_created = models.DateField(auto_now_add = True)      

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save_profile(self):
#         self.save
    
#     def delete_user(self):
#         self.delete()

# @receiver(post_save, sender = User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)     

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()   