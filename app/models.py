from django.db import models
from django.contrib.auth.models import User

class Pipeline(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('under_maintenance', 'Under Maintenance'),
    ]

    length = models.FloatField(verbose_name="Length (m)",default=0)
    diameter = models.FloatField(verbose_name="Diameter (mm)", default=0)

    material = models.CharField(max_length=100, verbose_name="Material",default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Status")

    def checkPressure(self):
        # Пример метода для проверки давления
        return f"Pressure is within the normal range for a pipeline with diameter {self.diameter} mm."

    def checkFlowRate(self):
        # Пример метода для проверки скорости потока
        return f"Flow rate is optimal for a pipeline with length {self.length} m."

    def __str__(self):
        return f"Pipeline {self.id} ({self.status})"
class Product(models.Model):
    name = models.CharField(max_length=100)
    pipeline = models.ForeignKey(Pipeline, related_name='products', on_delete=models.CASCADE)
    volume = models.FloatField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.volume} л)"

class Batch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='batches')
    type = models.CharField(max_length=100)
    volume = models.FloatField()
    quality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.volume} л"

class Separator(models.Model):
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE, related_name='separators')
    status = models.CharField(max_length=50)
    fill_level = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pipeline.name} - {self.status}"

class QualityControl(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='quality_controls')
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quality for {self.batch.type}"

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE, related_name='reports')
    volume = models.FloatField()
    quality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.pipeline.name}"


class System(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('maintenance', 'Under Maintenance'),
    ]

    name = models.CharField(max_length=100, verbose_name="System Name")
    startDate = models.DateField(verbose_name="Start Date")
    endDate = models.DateField(verbose_name="End Date")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inactive', verbose_name="Status")

    def startSystem(self):
        return f"System {self.name} has been started."

    def stopSystem(self):
        return f"System {self.name} has been stopped."

    def monitorPipelines(self):
        return f"Monitoring pipelines for system {self.name}."

    def __str__(self):
        return f"{self.name} ({self.status})"


class Route(models.Model):
    startPoint = models.CharField(max_length=100, verbose_name="Start Point")
    endPoint = models.CharField(max_length=100, verbose_name="End Point")
    volume = models.FloatField(verbose_name="Volume (m³)")
    productType = models.CharField(max_length=100, verbose_name="Product Type")

    def calculateOptimalRoute(self):
        return f"Optimal route calculated for {self.startPoint} to {self.endPoint}."

    def __str__(self):
        return f"{self.startPoint} to {self.endPoint} ({self.productType})"