import os
from unicodedata import name
from django.db import models
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=32, default="firstname")
    last_name = models.CharField(max_length=32, default="lastname")
    # full_name = first_name+" "+last_name
    email_address = models.EmailField(default="email@email.com")
    phone_number = models.CharField(max_length=13)
    biography = models.TextField(default="No Bio")
    last_update = models.DateTimeField('Last info update')
    active = models.BooleanField(default=False)
    alternate_email = models.EmailField(default="email@email.com")
    alternate_phone = models.CharField(max_length=13,default="0000000000000")
    show_alternate_contact = models.BooleanField(default=False)
    image_dir = models.FilePathField(path="mainsite/static/mainsite/images/")
    # profile_image = models.ImageField(upload_to="static/mainsite/images/")

    # def get_absolute_url(self):
    #     return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.first_name+" "+self.last_name

class Skills(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=64, default="skillname")
    skill_level = models.IntegerField(default=1)
    show = models.BooleanField(default=False)
    skill_icon_name = models.CharField(max_length=32,default="fa-code")

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name_plural = "skills"

class SocialMedia(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=32, default="sitename")
    site_url = models.URLField(max_length=256)
    username = models.CharField(max_length=64, default="username")
    show = models.BooleanField(default=False)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "social media"

class Accomplishment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    accomplishment_name = models.CharField(max_length=64, default="No Name")
    accomplishment_description = models.TextField(default="No description.")
    ranking = models.IntegerField(default=1)
    show = models.BooleanField(default=False)
    image_dir = models.FilePathField(path="mainsite/static/mainsite/images/")
    # image = models.ImageField(upload_to="static/mainsite/images/")

    def __str__(self):
        return self.accomplishment_name

    def imageName(self):
        return os.path.basename(self.image_dir)

    class Meta:
        verbose_name_plural = "accomplishments"

class Message(models.Model):
    name = models.CharField(max_length = 128, default="")
    email = models.EmailField(default="unknown@email.com")
    message = models.TextField(default="Message body")
    date_received = models.DateTimeField('Date message received')

    def __str__(self):
        return self.name
