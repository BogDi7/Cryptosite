from django.db import models

class CryptoCurrency(models.Model):
    title = models.CharField(max_length=255)
    usd_rate = models.FloatField()
    eur_rate = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title