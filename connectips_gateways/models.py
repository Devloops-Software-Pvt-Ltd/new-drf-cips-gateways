from django.db import models

def creditor_pfx_file_upload_path(instance, filename):
    return 'creditor_pfx_file/{1}'.format(instance.id, filename)

class CipsPayment(models.Model):
    gateway_url = models.CharField(max_length=255)
    merchant_id = models.CharField(max_length=255)
    app_id = models.CharField(max_length=255)
    app_name = models.CharField(max_length=255)
    validation_url = models.CharField(max_length=255)  
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    creditor_password = models.CharField(max_length=255)
    creditor_pfx_file = models.FileField(upload_to= creditor_pfx_file_upload_path)

    def __str__(self):
        return f"{self.app_name} ({self.merchant_id})"
