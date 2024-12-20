# Generated by Django 3.2.25 on 2024-12-18 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_route_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipeline',
            name='material',
            field=models.CharField(default='Unknown', max_length=100, verbose_name='Material'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Администратор'), ('operator', 'Оператор'), ('employee', 'Сотрудник')], default='employee', max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
