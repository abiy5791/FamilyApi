from django.db import models

# lets us explicitly set upload path and filename


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Blog(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField(blank=True, null=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    posted_by = models.CharField(max_length=100)
    post_date = models.DateTimeField()
