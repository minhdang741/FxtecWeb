from django.db import models

# Create your models here.

class Robot(models.Model):
    EQTCHECK = models.BooleanField()
    TIMECHECK = models.IntegerField()
    SERVER = models.CharField(max_length=20)
    LOGIN = models.CharField(max_length=20)
    VPS = models.CharField(max_length=20)
    TIME = models.CharField(max_length=20)
    CURRENCY = models.CharField(max_length=20)
    BALANCE = models.CharField(max_length=20)
    PROFIT = models.CharField(max_length=20)
    EQUITY = models.CharField(max_length=20)
    MARGIN = models.CharField(max_length=20)
    MARGIN_LEVEL = models.CharField(max_length=20)
    MARGIN_FREE = models.CharField(max_length=20)
    RUN = models.CharField(max_length=20)
    BEAR_LEVEL = models.CharField(max_length=20)
    SYSTEM_ALERT = models.CharField(max_length=1)
    CONTRACT_EXPIRED = models.CharField(max_length=20)
    ROI_LEVEL = models.CharField(max_length=20)
    N0_OF_LOSS = models.CharField(max_length=20)
    N0_TRUST_WIN = models.CharField(max_length=20)
    ACCOUNT_WARNING_LEVEL = models.CharField(max_length=20)
