from django.shortcuts import render

# Create your views here.
def dzordzulator_view(request):
    return render(request,'index.html')
