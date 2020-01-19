from django.db import models

# Create your Blog models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pup_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Add the blog app to settings

#create migration
