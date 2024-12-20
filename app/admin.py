from django.contrib import admin
from .models import (
    Pipeline, Product, Batch, Separator, QualityControl, Report, System, Route
)

# Регистрация моделей в админке
@admin.register(Pipeline)
class PipelineAdmin(admin.ModelAdmin):
    list_display = ('id', 'length', 'diameter', 'material', 'status')
    list_filter = ('status', 'material')
    search_fields = ('id', 'material')
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pipeline', 'volume', 'order')
    list_filter = ('pipeline', 'name')
    search_fields = ('name', 'pipeline__id')
    ordering = ('order',)


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'volume', 'quality', 'created_at')
    list_filter = ('type', 'quality', 'user')
    search_fields = ('type', 'user__username')
    ordering = ('-created_at',)


@admin.register(Separator)
class SeparatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'pipeline', 'status', 'fill_level', 'created_at')
    list_filter = ('status', 'pipeline')
    search_fields = ('pipeline__id',)
    ordering = ('-created_at',)


@admin.register(QualityControl)
class QualityControlAdmin(admin.ModelAdmin):
    list_display = ('id', 'batch', 'created_at')
    list_filter = ('batch',)
    search_fields = ('batch__type',)
    ordering = ('-created_at',)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pipeline', 'volume', 'quality', 'created_at')
    list_filter = ('user', 'pipeline', 'quality')
    search_fields = ('user__username', 'pipeline__id')
    ordering = ('-created_at',)


@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'startDate', 'endDate', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    ordering = ('startDate',)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'startPoint', 'endPoint', 'volume', 'productType')
    list_filter = ('productType',)
    search_fields = ('startPoint', 'endPoint')
    ordering = ('startPoint',)

from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone_number', 'position')
    list_filter = ('role',)
    search_fields = ('user__username', 'phone_number', 'position')