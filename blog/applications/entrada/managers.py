from pickle import TRUE
from django.db import models

class EntryManager(models.Manager):
    """Querys para buscar las entradas"""

    def entrada_en_portada(self):
        return self.filter(
            public=True,
            portada=True,

        ).order_by('-created').first()
        
    def entradas_recientes(self):
        return self.filter(
            public=True,

        ).order_by('-created')[:6]