from django import forms
from django.shortcuts import render,redirect
from django.views.generic.base import View
from .forms import personaForm
from .models import Persona
from django.views.generic import CreateView,DeleteView,ListView,UpdateView 




