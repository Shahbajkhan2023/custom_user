from django.shortcuts import render
from django.contrib.auth.models import User
from .models import AdminUser


def admin_dashboard(request):
    admins = AdminUser.objects.filter(is_active_administrator=True)
    return render(request, 'admin_dashboard.html', {'admins': admins})
