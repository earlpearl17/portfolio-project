from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    #pub_date = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField()
    #body = models.CharField(max_length=400)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
