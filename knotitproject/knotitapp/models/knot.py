from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError
from django.urls import reverse

class Knot(models.Model):
    name = models.CharField(max_length=50, default='')
    rope_type = models.CharField(max_length=50, default='')
    company = models.CharField(max_length=50, default='')
    notes = models.CharField(max_length=50, default='')
    video = models.FileField(upload_to='videos/', null=True, verbose_name="")
    image = models.ImageField(upload_to='images/', null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Meta:
        verbose_name =("knot")
        verbose_name_plural = ("knots")

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse("_detail", kwargs={"pk": self.pk})