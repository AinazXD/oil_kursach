from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Pipeline, Product, Batch, Separator, QualityControl, Report, System, Route
from .forms import (
    PipelineForm, ProductForm, BatchForm, SeparatorForm, QualityControlForm, ReportForm, SystemForm, RouteForm
)

# Главная страница
def home(request):
    return render(request, 'home.html')

# Регистрация
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Авторизация
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Выход
def user_logout(request):
    logout(request)
    return redirect('home')

# CRUD для Pipeline
@login_required
def pipeline_list(request):
    pipelines = Pipeline.objects.all()
    return render(request, 'pipeline_list.html', {'pipelines': pipelines})

@login_required
def pipeline_detail(request, pipeline_id):
    pipeline = get_object_or_404(Pipeline, id=pipeline_id)
    return render(request, 'pipeline_detail.html', {'pipeline': pipeline})

@login_required
def pipeline_create(request):
    if request.method == 'POST':
        form = PipelineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pipeline_list')
    else:
        form = PipelineForm()
    return render(request, 'pipeline_form.html', {'form': form})

@login_required
def pipeline_update(request, pipeline_id):
    pipeline = get_object_or_404(Pipeline, id=pipeline_id)
    if request.method == 'POST':
        form = PipelineForm(request.POST, instance=pipeline)
        if form.is_valid():
            form.save()
            return redirect('pipeline_list')
    else:
        form = PipelineForm(instance=pipeline)
    return render(request, 'pipeline_form.html', {'form': form})

@login_required
def pipeline_delete(request, pipeline_id):
    pipeline = get_object_or_404(Pipeline, id=pipeline_id)
    if request.method == 'POST':
        pipeline.delete()
        return redirect('pipeline_list')
    return render(request, 'pipeline_confirm_delete.html', {'object': pipeline})

# CRUD для Product
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'object': product})

# CRUD для Batch
@login_required
def batch_list(request):
    batches = Batch.objects.all()
    return render(request, 'batch_list.html', {'batches': batches})

@login_required
def batch_detail(request, batch_id):
    batch = get_object_or_404(Batch, id=batch_id)
    return render(request, 'batch_detail.html', {'batch': batch})

@login_required
def batch_create(request):
    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('batch_list')
    else:
        form = BatchForm()
    return render(request, 'batch_form.html', {'form': form})

@login_required
def batch_update(request, batch_id):
    batch = get_object_or_404(Batch, id=batch_id)
    if request.method == 'POST':
        form = BatchForm(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            return redirect('batch_list')
    else:
        form = BatchForm(instance=batch)
    return render(request, 'batch_form.html', {'form': form})

@login_required
def batch_delete(request, batch_id):
    batch = get_object_or_404(Batch, id=batch_id)
    if request.method == 'POST':
        batch.delete()
        return redirect('batch_list')
    return render(request, 'batch_confirm_delete.html', {'object': batch})

# CRUD для Separator
@login_required
def separator_list(request):
    separators = Separator.objects.all()
    return render(request, 'separator_list.html', {'separators': separators})

@login_required
def separator_detail(request, separator_id):
    separator = get_object_or_404(Separator, id=separator_id)
    return render(request, 'separator_detail.html', {'separator': separator})

@login_required
def separator_create(request):
    if request.method == 'POST':
        form = SeparatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('separator_list')
    else:
        form = SeparatorForm()
    return render(request, 'separator_form.html', {'form': form})

@login_required
def separator_update(request, separator_id):
    separator = get_object_or_404(Separator, id=separator_id)
    if request.method == 'POST':
        form = SeparatorForm(request.POST, instance=separator)
        if form.is_valid():
            form.save()
            return redirect('separator_list')
    else:
        form = SeparatorForm(instance=separator)
    return render(request, 'separator_form.html', {'form': form})

@login_required
def separator_delete(request, separator_id):
    separator = get_object_or_404(Separator, id=separator_id)
    if request.method == 'POST':
        separator.delete()
        return redirect('separator_list')
    return render(request, 'separator_confirm_delete.html', {'object': separator})

# CRUD для QualityControl
@login_required
def quality_control_list(request):
    quality_controls = QualityControl.objects.all()
    return render(request, 'quality_control_list.html', {'quality_controls': quality_controls})

@login_required
def quality_control_detail(request, quality_control_id):
    quality_control = get_object_or_404(QualityControl, id=quality_control_id)
    return render(request, 'quality_control_detail.html', {'quality_control': quality_control})

@login_required
def quality_control_create(request):
    if request.method == 'POST':
        form = QualityControlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control_list')
    else:
        form = QualityControlForm()
    return render(request, 'quality_control_form.html', {'form': form})

@login_required
def quality_control_update(request, quality_control_id):
    quality_control = get_object_or_404(QualityControl, id=quality_control_id)
    if request.method == 'POST':
        form = QualityControlForm(request.POST, instance=quality_control)
        if form.is_valid():
            form.save()
            return redirect('quality_control_list')
    else:
        form = QualityControlForm(instance=quality_control)
    return render(request, 'quality_control_form.html', {'form': form})

@login_required
def quality_control_delete(request, quality_control_id):
    quality_control = get_object_or_404(QualityControl, id=quality_control_id)
    if request.method == 'POST':
        quality_control.delete()
        return redirect('quality_control_list')
    return render(request, 'quality_control_confirm_delete.html', {'object': quality_control})

# CRUD для Report
@login_required
def report_list(request):
    reports = Report.objects.all()
    return render(request, 'report_list.html', {'reports': reports})

@login_required
def report_detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'report_detail.html', {'report': report})

@login_required
def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'report_form.html', {'form': form})

@login_required
def report_update(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm(instance=report)
    return render(request, 'report_form.html', {'form': form, 'object': report})

from django.shortcuts import render, get_object_or_404, redirect
from .models import System, Route
from .forms import SystemForm, RouteForm

# CRUD для System
@login_required
def system_list(request):
    systems = System.objects.all()
    return render(request, 'system_list.html', {'systems': systems})

@login_required
def system_detail(request, system_id):
    system = get_object_or_404(System, id=system_id)
    return render(request, 'system_detail.html', {'system': system})

@login_required
def system_create(request):
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('system_list')
    else:
        form = SystemForm()
    return render(request, 'system_form.html', {'form': form})

@login_required
def system_update(request, system_id):
    system = get_object_or_404(System, id=system_id)
    if request.method == 'POST':
        form = SystemForm(request.POST, instance=system)
        if form.is_valid():
            form.save()
            return redirect('system_list')
    else:
        form = SystemForm(instance=system)
    return render(request, 'system_form.html', {'form': form})

@login_required
def system_delete(request, system_id):
    system = get_object_or_404(System, id=system_id)
    if request.method == 'POST':
        system.delete()
        return redirect('system_list')
    return render(request, 'system_confirm_delete.html', {'object': system})

# CRUD для Route
@login_required
def route_list(request):
    routes = Route.objects.all()
    return render(request, 'route_list.html', {'routes': routes})

@login_required
def route_detail(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    return render(request, 'route_detail.html', {'route': route})

@login_required
def route_create(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm()
    return render(request, 'route_form.html', {'form': form})

@login_required
def route_update(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('route_list')
    else:
        form = RouteForm(instance=route)
    return render(request, 'route_form.html', {'form': form})

@login_required
def route_delete(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    if request.method == 'POST':
        route.delete()
        return redirect('route_list')
    return render(request, 'route_confirm_delete.html', {'object': route})

@login_required
def report_delete(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'report_confirm_delete.html', {'object': report})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Profile

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Перенаправление в зависимости от роли
            if user.profile.role == 'admin':
                return redirect('admin_dashboard')
            elif user.profile.role == 'operator':
                return redirect('operator_dashboard')
            elif user.profile.role == 'employee':
                return redirect('employee_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Неверные данные'})
    return render(request, 'login.html')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    if request.user.profile.role != 'admin':
        return redirect('home')  # Перенаправление, если не администратор
    return render(request, 'admin_dashboard.html')

@login_required
def operator_dashboard(request):
    if request.user.profile.role != 'operator':
        return redirect('home')  # Перенаправление, если не оператор
    return render(request, 'operator_dashboard.html')

@login_required
def employee_dashboard(request):
    if request.user.profile.role != 'employee':
        return redirect('home')  # Перенаправление, если не сотрудник
    return render(request, 'employee_dashboard.html')


@login_required
def some_view(request):
    if request.user.profile.role != 'admin':  # Проверка роли
        return redirect('home')  # Перенаправление, если роль не соответствует
    # Остальная логика