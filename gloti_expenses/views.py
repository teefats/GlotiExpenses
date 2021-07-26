from django.shortcuts import render

# Create your views here.
# urlpatterns = [
#     ('')
# ]
def index(request):
    return render(request, 'gloti_expenses/index.html')

def add_expense(request):
    return render(request, 'gloti_expenses/add_expense.html')