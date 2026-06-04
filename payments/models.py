from django.db import models
from accounts.models import CustomUser
# Create your models here.
class Transaction(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    transaction_uuid=models.CharField(max_length=200)
    transaction_code=models.CharField(max_length=200)
    product_code=models.CharField(max_length=200, null=True)
    status=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    total_amount=models.CharField(max_length=200)
    created_at=models.DateField(auto_now=True)