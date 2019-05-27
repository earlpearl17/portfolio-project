from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    #pub_date = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField()
    #body = models.CharField(max_length=400)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title + " " + str(self.pub_date)

    def summary(self):
        return self.body[:100] + "..."

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
