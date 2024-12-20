from django.urls import path
from . import views

urlpatterns = [
    # CRUD для System
    path('systems/', views.system_list, name='system_list'),
    path('systems/create/', views.system_create, name='system_create'),
    path('systems/<int:system_id>/', views.system_detail, name='system_detail'),
    path('systems/<int:system_id>/update/', views.system_update, name='system_update'),
    path('systems/<int:system_id>/delete/', views.system_delete, name='system_delete'),

    # CRUD для Route
    path('routes/', views.route_list, name='route_list'),
    path('routes/create/', views.route_create, name='route_create'),
    path('routes/<int:route_id>/', views.route_detail, name='route_detail'),
    path('routes/<int:route_id>/update/', views.route_update, name='route_update'),
    path('routes/<int:route_id>/delete/', views.route_delete, name='route_delete'),


    #auth

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    #CRUD для Pipline

    path('pipelines/', views.pipeline_list, name='pipeline_list'),
    path('pipelines/create/', views.pipeline_create, name='pipeline_create'),
    path('pipelines/<int:pipeline_id>/', views.pipeline_detail, name='pipeline_detail'),
    path('pipelines/<int:pipeline_id>/update/', views.pipeline_update, name='pipeline_update'),
    path('pipelines/<int:pipeline_id>/delete/', views.pipeline_delete, name='pipeline_delete'),

    # CRUD для  Products

    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/<int:product_id>/update/', views.product_update, name='product_update'),
    path('products/<int:product_id>/delete/', views.product_delete, name='product_delete'),

    # CRUD для Batches

    path('batches/', views.batch_list, name='batch_list'),
    path('batches/create/', views.batch_create, name='batch_create'),
    path('batches/<int:batch_id>/', views.batch_detail, name='batch_detail'),
    path('batches/<int:batch_id>/update/', views.batch_update, name='batch_update'),
    path('batches/<int:batch_id>/delete/', views.batch_delete, name='batch_delete'),

    #CRUD для Sepators

    path('separators/', views.separator_list, name='separator_list'),
    path('separators/create/', views.separator_create, name='separator_create'),
    path('separators/<int:separator_id>/', views.separator_detail, name='separator_detail'),
    path('separators/<int:separator_id>/update/', views.separator_update, name='separator_update'),
    path('separators/<int:separator_id>/delete/', views.separator_delete, name='separator_delete'),

    #CRUD для Quality

    path('quality-controls/', views.quality_control_list, name='quality_control_list'),
    path('quality-controls/create/', views.quality_control_create, name='quality_control_create'),
    path('quality-controls/<int:quality_control_id>/', views.quality_control_detail, name='quality_control_detail'),
    path('quality-controls/<int:quality_control_id>/update/', views.quality_control_update, name='quality_control_update'),
    path('quality-controls/<int:quality_control_id>/delete/', views.quality_control_delete, name='quality_control_delete'),

    # CRUD для Reports

    path('reports/', views.report_list, name='report_list'),
    path('reports/create/', views.report_create, name='report_create'),
    path('reports/<int:report_id>/', views.report_detail, name='report_detail'),
    path('reports/<int:report_id>/update/', views.report_update, name='report_update'),
    path('reports/<int:report_id>/delete/', views.report_delete, name='report_delete'),

    #dashboard

    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/operator/', views.operator_dashboard, name='operator_dashboard'),
    path('dashboard/employee/', views.employee_dashboard, name='employee_dashboard'),


]