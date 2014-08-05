from django.shortcuts import render
from django.http import HttpResponse
from natch import nltk_utils
import json

# JSON APIs to get synonyms and so on

def get_synonyms(request):
    word = request.GET['w']
    syns = nltk_utils.get_synonyms(word)
    return HttpResponse(json.dumps(list(syns)))
    
def get_hyponyms(request):
    word = request.GET['w']
    syns = nltk_utils.get_hyponyms(word)
    return HttpResponse(json.dumps(list(syns)))
    
def get_hypernyms(request):
    word = request.GET['w']
    syns = nltk_utils.get_hypernyms(word)
    return HttpResponse(json.dumps(list(syns)))