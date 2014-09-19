from django.shortcuts import render, redirect,render_to_response

import json
from django.http.response import HttpResponse

from django.http import Http404
from django.template import RequestContext


def home(request):
    return render_to_response('eg.html')