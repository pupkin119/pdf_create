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

# Create your views here.

from urllib.request import urlopen
import urllib.request
import io
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def start(request):
    if request.method == 'GET':
        URL = 'https://s3.eu-central-1.amazonaws.com/cdn.facetoapp.com/media/faces/2019-01-16_121717.7474150000.jpg'

        with urllib.request.urlopen(URL) as url:
            f = io.BytesIO(url.read())

        img = Image.open(f)
        
        FONT_PATH = 'https://mdn.mozillademos.org/files/2468/VeraSeBd.ttf'
        
        with urllib.request.urlopen(FONT_PATH) as url:
            f1 = io.BytesIO(url.read())

        ImageFont.truetype(f1, 13)
            
        return render(request, 'pdf_create/start.html')
