from django.shortcuts import render

# Create your views here.
def principal(request):
    return render(request, 'blog/principal.html')

def ji(request):
    return render(request, 'blog/ji.html')