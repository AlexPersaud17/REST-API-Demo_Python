from django.db import models

class Stock(models.Model):
  ticker_sym = models.CharField(max_length=10)
  mrkt_open = models.FloatField()
  mrkt_close = models.FloatField()
  mrkt_cap_volume = models.IntegerField()

  def __str__(self):
    return self.ticker_sym