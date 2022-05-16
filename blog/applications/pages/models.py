from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

#apps de terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField


class Pages(TimeStampedModel):
    pass

    class Meta:
        verbose_name = 'Página'
        verbose_name_plural = 'Páginas'

    def __str__(self):
        pass
