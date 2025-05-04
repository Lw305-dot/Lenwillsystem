from django.db import models
from admin_panel.models import Location, User
# Create your models here.
class Asset(models.Model):
    asset_number = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=100, unique=True)
    install_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.type})"

class TechnicalData(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='technical_data')
    key = models.CharField(max_length=100)   # e.g., "Motor Power"
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.key}: {self.value}"

class WorkOrder(models.Model):
    STATUS_CHOICES = (
        ('un-released', 'Un-Released'),
        ('released', 'Released'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on-hold parts', 'On-Hold Parts'),
        ('on-hold resources', 'On-Hold Resources'),
        ('closed', 'Closed'),
    )
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    technician = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'technician'})
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='un-released')
    scheduled_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"WorkOrder #{self.id} - {self.status}"


class MaintenanceLog(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField()
    photo = models.ImageField(upload_to='maintenance_photos/', null=True, blank=True)

    def __str__(self):
        return f"Log for WO #{self.work_order.id} at {self.timestamp}"
