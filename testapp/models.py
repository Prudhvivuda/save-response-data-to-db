from django.db import models

class Request(models.Model):
    endpoint = models.CharField(max_length=100, null=True) 
    response_code = models.PositiveSmallIntegerField() 
    method = models.CharField(max_length=10, null=True)
    remote_address = models.CharField(max_length=20, null=True)
    exec_time = models.IntegerField(null=True) 
    date = models.DateTimeField(auto_now=True)
    response = models.TextField() 
    request = models.TextField()

    def __str__(self):
        return f'{self.endpoint} {self.response_code} {self.method} {self.remote_address} {self.exec_time} {self.date} {self.response} {self.request}'