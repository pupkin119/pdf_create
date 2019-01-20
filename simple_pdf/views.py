from django.shortcuts import render

from rest_framework_jwt.serializers import jwt_payload_handler
import jwt
from django.contrib.auth.hashers import Argon2PasswordHasher

from rest_framework.decorators import api_view, schema

import numpy as np

from django.http import HttpResponse

# read env
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env('.env')

# Create your views here.

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.decorators import permission_classes

# MAILER
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.core.mail import EmailMessage
# Create your views here.

from urllib.request import urlopen
import urllib.request
import io
import numpy as np
from PIL import ImageFont, ImageDraw, Image

import pandas as pd
import requests

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

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
        return render(request, 'pdf_create/start.html')

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
        img.save('123.jpg', format='jpeg')



        # msg = EmailMessage('Subject of the Email', 'Body of the email', 'from@email.com', ['to@email.com'])
        # msg.content_subtype = "html"
        # msg.attach_file('pdfs/Instructions.pdf')
        # msg.send()

        subject, from_email, to = 'confirm your email', 'faceappmailer@gmail.com', 'pupkin11999@gmail.com'
        text_content = 'Confirmation of registration'
        html_content = 'Confirm Registretion'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.attach_file('123.jpg')
        msg.send()

        return render(request, 'pdf_create/start.html')