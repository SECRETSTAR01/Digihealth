# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pytesseract as tess
from PIL import Image

# Create your views here.
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        tess.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
        img = Image.open(myfile)
        text = tess.image_to_string(img)

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload-doc.html', {
            'uploaded_file_url': uploaded_file_url,
            'uploaded_file_text': text
        })
    return render(request, 'upload-doc.html')

