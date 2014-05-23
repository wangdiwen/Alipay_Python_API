#!/usr/bin/env python

# import python env
import os
import sys

# import django env
from django.http import HttpResponse
# from django.shortcuts import render_to_response

def home(request):
    msg = 'This is Home Test !!!'
    return HttpResponse(msg)

def test(request):
    msg = 'This is Test!'
    return HttpResponse(msg)
