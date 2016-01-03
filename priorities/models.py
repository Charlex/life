from django.db import models
from django.utils.text import slugify
from django.template.loader import render_to_string
from django.conf import settings


class Priority(models.Model):
    """
    A habit to form, a goal to live by, etc.
    """
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )

