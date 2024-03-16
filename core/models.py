from django.contrib.auth.models import AbstractUser
from django.db import models
from core import utils

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    profile = models.ImageField(upload_to=utils.image_upload, validators=[utils.user_profile_validator], null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs):
        self.slug = utils.slug_generator(self) if not self.slug else self.slug
        return super().save(*args, **kwargs)

class Season(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = utils.slug_generator(self) if not self.slug else self.slug
        return super().save(*args, **kwargs)

class Quest(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    distance = models.PositiveIntegerField()
    prize = models.PositiveIntegerField()
    season = models.ForeignKey(Season, related_name='quest_season', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = utils.slug_generator(self) if not self.slug else self.slug
        return super().save(*args, **kwargs)

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    user = models.ForeignKey(User, related_name='location_user', on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, related_name='location_quest', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = utils.slug_generator(self) if not self.slug else self.slug
        return super().save(*args, **kwargs)

class Reward(models.Model):
    user = models.ForeignKey(User, related_name='reward_user', on_delete=models.CASCADE)
    quest = models.ForeignKey(Quest, related_name='reward_quest', on_delete=models.CASCADE)
    claimed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = utils.slug_generator(self) if not self.slug else self.slug
        return super().save(*args, **kwargs)