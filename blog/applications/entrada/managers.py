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

    def buscar_entrada(self, kword, categoria):

        if len(categoria) > 0:
            return self.filter(
                category__short_name=categoria,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')
