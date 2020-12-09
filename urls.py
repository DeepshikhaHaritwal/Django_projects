from django.urls import path
from . import views
from .views import report_display
urlpatterns = [
    path('',views.homepage,name='home-page'),
    path('register', views.register, name='registration-page'),
    path('login', views.login, name='login-page'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('income', views.income, name='income-page'),
    path('expense', views.expense, name='expense-page'),
    path('report_display', views.report, name='report-display'),
    path('report_display1', report_display.as_view(), name='generating-reports'),
    path('report_display2', views.report_display1, name='report'),
    path('report_options_income',views.report_options_income, name='reporting'),
]