from django.db import models

class Job(models.Model):
    #title = models.CharField(max_length=50, default='ENTER TITLE')
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=200, blank=True)
    #url = models.TextField(default='ENTER URL')
    #url = models.URLField(max_length=200, default='ENTER URL')
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='images/jobs/')
    #image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.summary) > 15:
            #return self.summary[:15] + "..."
            return self.title # + " " + str(self.pub_date)
        else:
            #return self.summary
            return self.title # + " " + str(self.pub_date)
