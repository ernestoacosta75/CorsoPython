from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def hello(request):
	return HttpResponse('hello')
	
def whoami(request):
	'''Returns a response composed by a string that
	include the request parameters.'''
	sex = request.GET['sex']
	name = request.GET['name']	
	response = 'You are ' + name + ' and of sex ' + sex
	return HttpResponse(response)	
	
def time(request):
	return HttpResponse(datetime.datetime.now())	
	
def bmi(request):
	'''To calcolate the BMI given height and mass as request parameters.'''
	height = request.GET['height']
	mass = request.GET['mass']
	bmi_index = int(mass)/float(height)**2
	return HttpResponse(bmi_index)	