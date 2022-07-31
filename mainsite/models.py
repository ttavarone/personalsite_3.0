from tabnanny import verbose
from unicodedata import name
from django.db import models

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

    def __str__(self):
        return self.first_name+" "+self.last_name

class Skills(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=64, default="skillname")
    skill_level = models.IntegerField(default=1)
    show = models.BooleanField(default=False)

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

class Accomplishments(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    accomplishment_name = models.CharField(max_length=64, default="No Name")
    accomplishment_description = models.TextField(default="No description.")
    ranking = models.IntegerField(default=1)
    show = models.BooleanField(default=False)
