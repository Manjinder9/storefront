from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return render(request,
                  template_name = 'hello.html', 
                  context = {'name': 'Mani'}
                  )

