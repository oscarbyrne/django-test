from django.db import models


class Asset(models.Model):

    AVAILABLE = 'AV'
    BUSY = 'BU'
    OFFLINE = 'OF'

    STATUS_CHOICES = (
        (AVAILABLE, 'Available'),
        (BUSY, 'Busy'),
        (AVAILABLE, 'Offline'),
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=AVAILABLE,
    )

    host = models.GenericIPAddressField()


    class Meta:
        abstract = True

    def is_available(self):
        if self.id: self.refresh_from_db(fields=['status'])
        return self.status is self.AVAILABLE

    def reserve(self):
        # probably need more logic here to stop race conditions
        self.status = self.BUSY
        if self.id: self.save(update_fields=['status'])

    def relinquish(self):
        self.status = self.AVAILABLE
        if self.id: self.save(update_fields=['status'])
