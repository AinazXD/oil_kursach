from django.contrib import admin
from .models import Pipeline, Product, Batch, Separator, QualityControl, Report

# Регистрация модели Pipeline
@admin.register(Pipeline)
class PipelineAdmin(admin.ModelAdmin):
    list_display = ('id', 'length', 'diameter', 'material', 'status')
    list_filter = ('status', 'material')
    search_fields = ('id', 'material')
    ordering = ('id',)

# Регистрация модели Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'pipeline', 'volume', 'order')
    list_filter = ('pipeline',)
    search_fields = ('name', 'pipeline__id')
    ordering = ('order',)

# Регистрация модели Batch
@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'volume', 'quality', 'created_at')
    list_filter = ('type', 'quality', 'created_at')
    search_fields = ('type', 'user__username')
    ordering = ('-created_at',)

# Регистрация модели Separator
@admin.register(Separator)
class SeparatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'pipeline', 'status', 'fill_level', 'created_at')
    list_filter = ('status', 'pipeline')
    search_fields = ('pipeline__id', 'status')
    ordering = ('-created_at',)

# Регистрация модели QualityControl
@admin.register(QualityControl)
class QualityControlAdmin(admin.ModelAdmin):
    list_display = ('id', 'batch', 'created_at')
    list_filter = ('batch__type', 'created_at')
    search_fields = ('batch__id',)
    ordering = ('-created_at',)

# Регистрация модели Report
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'pipeline', 'volume', 'quality', 'created_at')
    list_filter = ('pipeline', 'quality', 'created_at')
    search_fields = ('pipeline__id', 'user__username')
    ordering = ('-created_at',)


from django.contrib import admin
from .models import System, Route

@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'startDate', 'endDate', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    ordering = ('id',)

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'startPoint', 'endPoint', 'volume', 'productType')
    list_filter = ('productType',)
    search_fields = ('startPoint', 'endPoint')
    ordering = ('id',)