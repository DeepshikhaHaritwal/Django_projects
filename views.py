from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from .models import income_details, expense_details
from django.views.generic import TemplateView
# Create your views here.
def homepage(request):
    return render(request,'MyExpenseTracker/registration.html')

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirm_password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        print('user created')
        return redirect('/login')

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/dashboard')
        else:
            print('user not found')
            return redirect('/login')
    else:
            return render(request,'MyExpenseTracker/Login.html')

def expense(request):
    if request.method=="POST":
        estimated_expenses = request.POST['estimated_expenses']
        expense_source = request.POST['category']
        expense_amount = request.POST['amount']
        expense_date = request.POST['date']

        expense_detail = expense_details(estimated_expenses=estimated_expenses, expense_source= expense_source, expense_amount=expense_amount, expense_date= expense_date)
        expense_detail.save()
        print("Expense details saved")
        return render(request, 'MyExpenseTracker/expense.html')
    else:
        return render(request, 'MyExpenseTracker/expense.html')


def income(request):
    if request.method=="POST":
        budget = request.POST['budget']
        income_source = request.POST['category']
        income_amount = request.POST['amount']
        income_date = request.POST['date']
        income_detail = income_details(budget=budget, income_source= income_source, income_amount=income_amount, income_date= income_date)
        income_detail.save()
        print("Income details saved")
        return render(request, 'MyExpenseTracker/income.html')
    else:
        return render(request, 'MyExpenseTracker/income.html')

def dashboard(request):
    return render(request, 'MyExpenseTracker/dashboard.html')

def report(request):
    return render(request, 'MyExpenseTracker/report_display.html')

class report_display(TemplateView):
    template_name = 'MyExpenseTracker/report_display.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incomes'] = income_details.objects.all()
        return context

def report_display1(request):
    labels= []
    data = []
    queryset = income_details.objects.order_by('-income_amount')[:4]
    for item in queryset:
        labels.append(item.income_source)
        data.append(item.income_amount)
    return render(request, 'MyExpenseTracker/report_display.html',{
        'labels':labels,
        'data':data,
    })

def report_options_income(request):
    labels = []
    data = []
    queryset = income_details.objects.order_by('-income_amount')[:4]
    for item in queryset:
        labels.append(item.income_source)
        data.append(item.income_amount)
    return render(request, 'MyExpenseTracker/report_display.html', {
        'labels': labels,
        'data': data,
    })