from django.db import models
from django.contrib.auth.models import User

class conversations(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    input_text= models.TextField()
    response_text=models.TextField(blank=True,null=True)
    time=models.TimeField(auto_now=True)
    
