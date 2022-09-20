from tkinter import CASCADE
import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# class Ticket(models.Model):
#     ticket_id = models.CharField(max_length=8, default='NS000001')
#     ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     server_details = models.CharField(max_length=100)
#     send_date = models.DateTimeField(default=timezone.now)
#     license_no = models.CharField(max_length=25)
#     file = models.FileField(upload_to='documents/%Y%m%d/')

    # def save(self, force_insert=False, force_update=False):
    #     self.ticket_id = 'NS%08d' % self.ticket_id
    #     super(Ticket, self).save(force_insert, force_update)

class Ticket2(models.Model):
    ticketholder = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    ticket_id = models.CharField(max_length=8, default='NS000001')
    server_details = models.CharField(max_length=100)
    send_date = models.DateTimeField(default=timezone.now)
    license_no = models.CharField(max_length=25)
    file = models.FileField(upload_to='documents/%Y%m%d/')

    def __str__(self):
        return self.ticket_id