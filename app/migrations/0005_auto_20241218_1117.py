# Generated by Django 3.2.25 on 2024-12-18 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20241218_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('operator', 'Оператор'), ('employee', 'Сотрудник')], default='employee', max_length=20, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
