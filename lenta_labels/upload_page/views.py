from django.shortcuts import render


# Create your views here.
def upload_page(request):
    return render(request, 'upload_page.html')
