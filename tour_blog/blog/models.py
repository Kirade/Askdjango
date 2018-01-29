import re

from django.db import models
from django.forms import ValidationError


def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50,
                              validators=[lnglat_validator],
                              help_text='경도,위도 포멧으로 입력', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title