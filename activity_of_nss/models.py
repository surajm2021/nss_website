from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.urls import reverse
from django.conf import settings
from PIL import Image


class Activity(models.Model):
    title = models.CharField(max_length=100, help_text='Title of activity')
    description = models.TextField(help_text='Description of activity')
    address = models.CharField(max_length=100, help_text='Address of activity')
    date_of_activity = models.DateTimeField(default=timezone.now)
    time_of_activity = models.TimeField(default=now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='Activity_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('activity-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    activity = models.ForeignKey(Activity, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=150, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.activity.title, self.author)
