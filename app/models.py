from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Модель профиля пользователя
class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('operator', 'Оператор'),
        ('employee', 'Сотрудник'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee', verbose_name="Роль")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Номер телефона")
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name="Должность")

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"


# Сигнал для автоматического создания профиля при создании пользователя
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Модель трубопровода
class Pipeline(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('under_maintenance', 'Under Maintenance'),
    ]

    length = models.FloatField(verbose_name="Length (m)", default=0)
    diameter = models.FloatField(verbose_name="Diameter (mm)", default=0)
    material = models.CharField(max_length=100, verbose_name="Material", default="Unknown")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Status")

    def checkPressure(self):
        return f"Pressure is within the normal range for a pipeline with diameter {self.diameter} mm."

    def checkFlowRate(self):
        return f"Flow rate is optimal for a pipeline with length {self.length} m."

    def __str__(self):
        return f"Pipeline {self.id} ({self.status})"


# Модель продукта
class Product(models.Model):
    name = models.CharField(max_length=100)
    pipeline = models.ForeignKey(Pipeline, related_name='products', on_delete=models.CASCADE)
    volume = models.FloatField()
    order = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.volume} л)"


# Модель партии
class Batch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='batches')
    type = models.CharField(max_length=100)
    volume = models.FloatField()
    quality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.volume} л"


# Модель сепаратора
class Separator(models.Model):
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE, related_name='separators')
    status = models.CharField(max_length=50)
    fill_level = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pipeline.name} - {self.status}"


# Модель контроля качества
class QualityControl(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='quality_controls')
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Quality for {self.batch.type}"


# Модель отчета
class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    pipeline = models.ForeignKey(Pipeline, on_delete=models.CASCADE, related_name='reports')
    volume = models.FloatField()
    quality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.pipeline.name}"


# Модель системы
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


# Модель маршрута
class Route(models.Model):
    startPoint = models.CharField(max_length=100, verbose_name="Start Point")
    endPoint = models.CharField(max_length=100, verbose_name="End Point")
    volume = models.FloatField(verbose_name="Volume (m³)")
    productType = models.CharField(max_length=100, verbose_name="Product Type")

    def calculateOptimalRoute(self):
        return f"Optimal route calculated for {self.startPoint} to {self.endPoint}."

    def __str__(self):
        return f"{self.startPoint} to {self.endPoint} ({self.productType})"