from django.db import models

# Create your models here.

class Robot(models.Model):
    SERVER = models.CharField(max_length=20)
    LOGIN = models.IntegerField()
    VPS = models.CharField(max_length=20)
    TIME = models.BigIntegerField()
    CURRENCY = models.CharField(max_length=20)
    BALANCE = models.FloatField()
    PROFIT = models.FloatField()
    EQUITY = models.FloatField()
    MARGIN = models.FloatField()
    MARGIN_LEVEL = models.FloatField()
    MARGIN_FREE = models.FloatField()
    RUN = models.IntegerField()
    BEAR_LEVEL = models.FloatField()
    SYSTEM_ALERT = models.CharField(max_length=1)
    CONTRACT_EXPIRED = models.IntegerField()
    ROI_LEVEL = models.FloatField()
    N0_OF_LOSS = models.IntegerField()
    N0_TRUST_WIN = models.FloatField()
    ACCOUNT_WARNING_LEVEL = models.IntegerField()
    EQTCHECK = models.BooleanField()
    TIMECHECK = models.IntegerField()
