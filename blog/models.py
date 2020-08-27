from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Blog(models.Model):
    title = models.CharField(max_length=50)
    #pub_date = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField()
    #body = models.CharField(max_length=400)
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog/')
    #image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title + " " + str(self.pub_date)

    def summary(self):
        return self.body[:100] + "..."

    def pub_date_pretty(self):
        #return self.pub_date.strftime('%b %e %Y')
        return self.pub_date.strftime('%c')

    def get_absolute_url(self):
        # Slugify the combination of role and company_name as these may contain
        # whitespace or other characters that are not permitted in urls.
        slug = slugify(f"{self.title}-{self.pub_date_pretty()}")
        #return reverse("job-posting", kwargs={"blog_id": self.id, "slug": slug})
        return reverse("detail-keywords", kwargs={"blog_id": self.id, "slug": slug})