from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Document(models.Model):
    # title = models.TextField(max_length = 30)
    image = models.ImageField(upload_to = 'index/', blank=True)
    content = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True ,related_name='author')
    date_created= models.DateField(auto_now_add=True )
    courses  = models.TextField(max_length = 30)

def save_document(self):
    self.save()

    @classmethod
    def all_documents(cls) :
        documents = cls.objects.all()
        return documents

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile/', blank ='true',default='default.png')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(blank=True, max_length=120)
    date_created = models.DateField(auto_now_add = True)      

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save
    
    def delete_user(self):
        self.delete()

@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)     

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()       





