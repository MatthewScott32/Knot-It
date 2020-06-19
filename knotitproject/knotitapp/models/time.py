from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .knot import Knot

class Time(models.Model):

    time = models.CharField(max_length=50)
    knot = models.ForeignKey(Knot, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)

    class Meta:
            verbose_name =("time")
            verbose_name_plural = ("times")

    def __str__(self):
        return u'{0}'.format(self.name)

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})