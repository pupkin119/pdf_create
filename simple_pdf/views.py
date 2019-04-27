# from django.shortcuts import render
import json

# from rest_framework_jwt.serializers import jwt_payload_handler
# import jwt
# from django.contrib.auth.hashers import Argon2PasswordHasher
#
# from rest_framework.decorators import api_view, schema

# import numpy as np

# import django_rq
from datetime import timedelta
# from django.utils import timezone

import django_rq
scheduler = django_rq.get_scheduler('default')


# from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
# from django.urls import reverse

# read env
import environ
from simple_pdf.tasks import delete_later_pdf

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env('.env')

# Create your views here.

# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.generics import RetrieveUpdateAPIView
# from rest_framework.decorators import permission_classes

# MAILER
# from django.core.mail import EmailMultiAlternatives
# from django.contrib.auth.tokens import PasswordResetTokenGenerator

# from django.core.mail import EmailMessage
# Create your views here.

from urllib.request import urlopen
import urllib.request
import io
import numpy as np
from PIL import ImageFont, ImageDraw, Image

import pandas as pd
import requests
from django.views.decorators.csrf import csrf_exempt

def transform_name(name):
    if len(name) >= 21:
        name_list = name.split()
        name = name_list[0] + " " +name_list[1] + " \n" + name_list[2]
        return name
    else:
        return name

def transform_nameV2(s, n):
    l = s.split()
    for i in range(1, len(l)+1):
        if sum(map(len, l[:i])) + i - 1 > n:
            return ' '.join(l[:i-1]) + " \n" + ' '.join(l[i-1:])
    return s

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

@csrf_exempt
def start(request):
    if request.method == 'GET':
        # URL = 'https://s3.eu-central-1.amazonaws.com/cdn.facetoapp.com/media/faces/2019-01-16_121717.7474150000.jpg'
        #
        # with urllib.request.urlopen(URL) as url:
        #     f = io.BytesIO(url.read())
        #
        # img = Image.open(f)
        #
        # FONT_PATH = 'https://mdn.mozillademos.org/files/2468/VeraSeBd.ttf'
        #
        # with urllib.request.urlopen(FONT_PATH) as url:
        #     f1 = io.BytesIO(url.read())
        #
        # ImageFont.truetype(f1, 13)
        #
        # return render(request, 'pdf_create/login.html')
        return render(request, 'pdf_create/signin.html')

@csrf_exempt
def generate_pdf(request):
    if request.is_ajax() and request.POST:
        #open IMG
        URL_IMG = 'https://s3.eu-central-1.amazonaws.com/cdn.facetoapp.com/media/faces/2019-01-16_121717.7474150000.jpg'

        with urllib.request.urlopen(URL_IMG) as url:
            f = io.BytesIO(url.read())

        img = Image.open(f)

        #open FONT
        URL_FONT = 'https://mdn.mozillademos.org/files/2468/VeraSeBd.ttf'

        with urllib.request.urlopen(URL_FONT) as url:
            font_byte = io.BytesIO(url.read())

        #open CSV
        url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
        s = requests.get(url).content
        data_csv = pd.read_csv(io.StringIO(s.decode('utf-8')))

        draw = ImageDraw.Draw(img)

        # # use a bitmap font
        # font = ImageFont.load("arial.pil")

        # draw.text((10, 10), "hello", font=font)

        # use a truetype font
        font = ImageFont.truetype(font_byte, 13)

        draw.text((10, 10), data_csv['Country'][0], font=font, fill=(0, 0, 0, 255))
        img.save('imgs/123.jpg', format='jpeg')



        # msg = EmailMessage('Subject of the Email', 'Body of the email', 'from@email.com', ['to@email.com'])
        # msg.content_subtype = "html"
        # msg.attach_file('pdfs/Instructions.pdf')
        # msg.send()

        # subject, from_email, to = 'confirm your email', 'faceappmailer@gmail.com', 'pupkin11999@gmail.com'
        # text_content = 'Confirmation of registration'
        # html_content = 'Confirm Registretion'
        # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        # msg.attach_alternative(html_content, "text/html")
        # msg.attach_file('123.jpg')
        # msg.send()

        return render(request, 'pdf_create/start.html')

@csrf_exempt
def login(request):
    if request.method == "POST":
        # return HttpResponseRedirect(reverse('simple_pdf:login'))
        return render(request, 'pdf_create/index.html')
    if request.method == "GET":
        # return HttpResponseRedirect(reverse('simple_pdf:login'))
        return render(request, 'pdf_create/index.html')

@csrf_exempt
def cutaway(request):
    if request.method == "GET":
        # return render(request, 'pdf_create/carousel.html')
        return render(request, 'pdf_create/choose.html')
        # return HttpResponseRedirect(reverse('simple_pdf:cau')
from textwrap import wrap
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image
draw = Drawing()
from PIL import Image as PILImage

import uuid
import pathlib
import shutil



@csrf_exempt
def manual_pdf(request):
    if request.is_ajax() and request.POST:
        names = request.POST.getlist("names[]")
        courses = request.POST.getlist("courses[]")
        town = request.POST['town']

        page_images = []
        rand_uuid = uuid.uuid4()

        pathlib.Path('imgs/'+ str(rand_uuid)).mkdir(parents=True, exist_ok=True)
        pathlib.Path('pdfs/'+ str(rand_uuid)).mkdir(parents=True, exist_ok=True)
        for i in np.arange(len(courses)):
            draw = Drawing()
            with Image(filename='imgs/sertf20.jpg') as image:
                draw.font = 'open-sans/Montserrat/Montserrat-Bold.ttf'
                draw.font_size = 186
                draw.fill_color = Color('#333333')
                # name = transform_name(names[i])
                name = transform_nameV2(names[i], 21)
                draw.text(340, 2385, name)
                draw.text(340, 3173, courses[i])
                draw.font = 'open-sans/Montserrat/Montserrat-Regular.ttf'
                draw.font_size = 100
                draw.text(684, 5105, town)


                # draw.viewbox(340, 2385, 340 + 2300, 2385 + 400)
                draw(image)

                image.save(filename='imgs/'+str(rand_uuid)+'/img_' + str(i) + '.jpg')

        im1 = PILImage.open("imgs/" + str(rand_uuid) + "/img_0.jpg")

        for i in np.arange(1, len(names)):
            im2 = PILImage.open("imgs/"+str(rand_uuid)+"/img_" + str(i) +".jpg")
            page_images.append(im2)

        shutil.rmtree('imgs/' + str(rand_uuid))

        pdf1_filename = "pdfs/" + str(rand_uuid) + "/cutway.pdf"

        im1.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=page_images)

        # scheduler.enqueue_in(timedelta(days=1), delete_later_pdf, str(rand_uuid))
        scheduler.enqueue_in(timedelta(minutes=1), delete_later_pdf, str(rand_uuid))

        data = json.dumps({'success': str(rand_uuid), 'error': None, 'description': None})

        return HttpResponse(data, content_type='application/json')

@csrf_exempt
def manual(request):
    if request.method == "GET":
        return render(request, 'pdf_create/manual.html')
        # return HttpResponseRedirect(reverse('simple_pdf:cau')

@csrf_exempt
def exel(request):
    if request.method == "GET":
        return render(request, 'pdf_create/exel.html')
        # return HttpResponseRedirect(reverse('simple_pdf:cau')

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

@csrf_exempt
def upload_exel(request):
    if request.method == 'POST' and request.FILES['file']:

        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        # town = request.POST['town']
        # print(request.POST['town'])
        # uploaded_file_url = fs.url(filename)
        # print(uploaded_file_url)

        rand_uuid = uuid.uuid4()
        pathlib.Path('imgs/'+ str(rand_uuid)).mkdir(parents=True, exist_ok=True)
        pathlib.Path('pdfs/'+ str(rand_uuid)).mkdir(parents=True, exist_ok=True)

        data = pd.read_csv(myfile.name)

        for i in np.arange(data.count()[0]):

            name = data[data.columns[0]][i]
            course = data[data.columns[1]][i]
            town = data[data.columns[2]][i]

            draw = Drawing()
            with Image(filename='imgs/sertf20.jpg') as image:
                draw.font = 'open-sans/Montserrat/Montserrat-Bold.ttf'
                draw.font_size = 186
                draw.fill_color = Color('#333333')
                # name = transform_name(name)
                name = transform_nameV2(name, 21)
                course = transform_nameV2(course, 21)
                draw.text(340, 2385, name)
                draw.text(340, 3173, course)
                draw.font_size = 100
                draw.font = 'open-sans/Montserrat/Montserrat-Regular.ttf'
                draw.text(684, 5105, town)
                draw(image)

                image.save(filename='imgs/' + str(rand_uuid) +'/img_' + str(i) + '.jpg')

        page_images = []
        for i in np.arange(1, data.count()[0]):
            im2 = PILImage.open("imgs/" + str(rand_uuid) + "/img_" + str(i) + ".jpg")
            page_images.append(im2)

        pdf1_filename = "pdfs/" + str(rand_uuid) + "/cutway.pdf"

        im1 = PILImage.open("imgs/" + str(rand_uuid) + "/img_0.jpg")

        im1.save(pdf1_filename, "PDF", resolution=100.0, save_all=True, append_images=page_images)

        shutil.rmtree('imgs/' + str(rand_uuid))
        os.remove(myfile.name)

        # scheduler.enqueue_in(timedelta(days=1), delete_later_pdf, str(rand_uuid))
        scheduler.enqueue_in(timedelta(minutes=1), delete_later_pdf, str(rand_uuid))

        data = json.dumps({'success': str(rand_uuid), 'error': None, 'description': None})

        # data = json.dumps({'success': uploaded_file_url})
        return HttpResponse(data, content_type='application/json')


@csrf_exempt
def preview(request, prev_uuid):
    if request.method == "GET":
        return render(request, 'pdf_create/preview.html', {"prev_uuid": prev_uuid})
