from django.shortcuts import render
from django.http import HttpResponse

from lenta_labels.settings import UPLOAD_DIR
from upload_page.forms import UploadFileForm
import os


def upload_page(request):
    return render(request, 'upload_page.html')


def handle_uploaded_file(f):
    with open(os.path.join(UPLOAD_DIR, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse('File uploaded successfully')
    else:
        form = UploadFileForm()
    return render(request, 'upload_page.html', {'form': form})
