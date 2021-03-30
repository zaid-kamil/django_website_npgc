from django.shortcuts import render

# Create your views here.
def index(request):
    ctx = {'title':'Home page'} # data for html page
    return render(request, 'index.html',context=ctx)

def show_data(request):
    ctx = {'title':'Show Data'}
    return render(request, 'data.html', context=ctx)