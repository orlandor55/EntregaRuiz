from django.db import models
from datetime import timedelta, datetime
from django.conf import settings
from django.template.defaultfilters import slugify

#apps de terceros
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField
#managers
from .managers import PageManager
 

class PageModel(TimeStampedModel):
    """Modelo para las páginas del blog"""

    title = models.CharField(
        'Título',
        max_length=200
    )
    resume = RichTextUploadingField('Resumen', max_length=300)
    content = RichTextUploadingField('contenido')
    public = models.BooleanField(default=False)
    slug = models.SlugField(
        editable=False, 
        max_length=300
    )

    objects = PageManager()

    class Meta:
            verbose_name = 'Página'
            verbose_name_plural = 'Páginas'
            ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second,
        )
        seconds = int(total_time.total_seconds())
        slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)

        super(PageModel, self).save(*args, **kwargs)

