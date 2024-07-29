from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'helloapp/hello_world.html', {})

def login_view(request):
    return render(request, 'helloapp/login.html')