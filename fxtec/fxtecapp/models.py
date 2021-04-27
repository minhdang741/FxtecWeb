from django.db import models

# Create your models here.

class Robot(models.Model):
    EQTCHECK = models.BooleanField()
    TIMECHECK = models.IntegerField()
    SERVER = models.TextField()
    LOGIN = models.IntegerField()
    VPS = models.TextField()
    TIME = models.FloatField()
    CURRENCY = models.TextField()
    BALANCE = models.FloatField()
    PROFIT = models.FloatField()
    EQUITY = models.FloatField()
    MARGIN = models.FloatField()
    MARGIN_LEVEL = models.FloatField()
    MARGIN_FREE = models.FloatField()
    RUN = models.FloatField()
    BEAR_LEVEL = models.FloatField()
    SYSTEM_ALERT = models.TextField()
    CONTRACT_EXPIRED = models.IntegerField()
    ROI_LEVEL = models.FloatField()
    N0_OF_LOSS = models.FloatField()
    N0_TRUST_WIN = models.FloatField()
    ACCOUNT_WARNING_LEVEL = models.IntegerField()
