from django.db import models

class Fonts(models.Model):
    name = models.CharField(max_length = 140, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='fonts/', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_url(self):
        try:
            return self.upload.url
        except ValueError:
            return ''

class Design(models.Model):
    name = models.CharField(max_length = 140, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='design/', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_url(self):
        try:
            return self.upload.url
        except ValueError:
            return ''


class Shops(models.Model):
    payment = models.IntegerField(default=0)

    def __str__(self):
        return self.payment


class Sertificates(models.Model):
    payment = models.IntegerField(default=0)

    def __str__(self):
        return str(self.payment)

