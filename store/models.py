from django.db import models
from maintenance.models import WorkOrder
# Create your models here.
class SparePart(models.Model):
    name = models.CharField(max_length=255)
    part_number = models.CharField(max_length=100)
    supplier = models.CharField(max_length=200)
    uom = models.CharField("Unit of Measure", max_length=100)
    quantity_in_stock = models.PositiveIntegerField()
    reorder_level = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.part_number})"

class PartRequest(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE)
    part = models.ForeignKey(SparePart, on_delete=models.CASCADE)
    quantity_used = models.PositiveIntegerField()
    requested_by = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)