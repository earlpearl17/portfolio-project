from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Topic(models.Model):
    """A tutorial topic."""
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/topics/', null=True, blank=True)
    summary = models.TextField(blank=True, default='')
    date_added = models.DateTimeField(auto_now_add=True)
    # url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

    # def get_absolute_url(self):
    #     # Slugify the combination of role and company_name as these may contain
    #     # whitespace or other characters that are not permitted in urls.
    #     slug = slugify(f"{self.text}")
    #     return reverse("topic_keywords", kwargs={"topic_id": self.id, "slug": slug})
    
class Tutorial(models.Model):
    """Specific tutorial based on topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    type = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/tutorials/', null=True, blank=True)
    file = models.FileField(upload_to='docs/tutorials/', null=True, blank=True)
    summary = models.TextField(blank=True, default='')
    LANGUAGES = (
        ('en', 'English'),
        ('fr', 'French'),
    )
    lang = models.CharField(max_length=2, choices=LANGUAGES, blank=False)
    
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            #return self.text[:50] + "..."
            return f"{self.topic}, {self.text[:50]}" + "..."
        else:
            return f"{self.topic}, {self.text}"

    def get_absolute_url(self):
        # Slugify the combination of role and company_name as these may contain
        # whitespace or other characters that are not permitted in urls.
        slug = slugify(f"{self.topic.text}-{self.text}")
        return reverse("topic_tutorial_keywords", kwargs={"topic_id": self.topic.id, "tutorial_id": self.id, "lang": self.lang, "slug": slug})
        