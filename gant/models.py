from django.db import models
from django.utils import timezone

USER = (
    ('0', 'Mamina'),
    ('1', 'Kengo'),
)

class Task(models.Model):
    # id は自動的に追加されるので定義不要
    title = models.CharField(max_length=100)
    user = models.CharField(max_length=100, choices=USER)
    progress = models.IntegerField(
            default=0)
    to_be_start_date = models.DateTimeField(
            default=timezone.now)
    to_be_complete_date = models.DateTimeField(
            blank=True, null=True)
    memo = models.CharField(
            blank=True, null=True, max_length=100)
    complete_date = models.DateTimeField(
            blank=True, null=True)
    update_at = models.DateTimeField(
            blank=True, null=True, default=timezone.now)
