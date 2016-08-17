from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Servers(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    ip = models.CharField(max_length=100, blank=True, default='')
    os = models.CharField(max_length=100, blank=True, default='')
    production = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
       return 'Server: ' + self.name
