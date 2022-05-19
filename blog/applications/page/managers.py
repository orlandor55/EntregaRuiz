from django.db import models

class PageManager(models.Manager):
    """Querys para buscar las páginas"""

    def buscar_pagina(self, kword):
        return self.filter(
            title__icontains=kword,
            public=True
        ).order_by('-created')
