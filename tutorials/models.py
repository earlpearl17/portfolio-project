from django.db import models

class Topic(models.Model):
    """A tutorial topic."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Tutorial(models.Model):
    """Specific tutorial based on topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=200, blank=True)
    #image = models.ImageField(upload_to='tutorials/',null=True)
    file = models.FileField(upload_to='tutorials/', null=True, blank=True)
    #summary = models.CharField(max_length=200)
    summary = models.TextField(blank=True, default='')

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text