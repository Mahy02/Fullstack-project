from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from FiFa.models import Tickets


#we will call it profile [extending user table model]:
class Profile (models.Model):
    #we want to create a one-one relation
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #user for this profile = one to one relation wuth user model , on deleting user delete profile but when profile deleted user is not deleted
    #now we can add any other field we want:
    #we already have username, password and email
    #First name - Last name - birth date- gender - nationality - role - is_auth
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    birth_date=  models.DateField(default=timezone.now)
    gender= models.CharField(max_length=1)
    nationality=  models.CharField(max_length=30, null=True)
    role= models.CharField(max_length=30, default='user')
    request_status = models.CharField(max_length=10, choices=[("requested", "requested"), ("approved", "approved"), ("denied", "denied"), ("none", "none")], default="none")
    def save(self, *args, **kwargs):
        if self.first_name and self.last_name and self.birth_date and self.gender:
            super(Profile, self).save(*args, **kwargs)
        
           
        
    #ticket_number=models.ForeignKey(Tickets, on_delete=models.CASCADE) 


    def __str__(self):
        return f'{self.user.username} Profile'

#dont forget to apply changes 
#register this model in admin model in our app
#later we will edit so that when user is added=>profile is added automatically 

# class Requests(models.Model):
#     user_name=models.ForeignKey(User, on_delete=models.CASCADE)
#     is_approved=models.BooleanField(default=False)