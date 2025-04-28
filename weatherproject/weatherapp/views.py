from django.shortcuts import render,HttpResponse
import requests
import datetime

# Create your views here.
def home(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='Indore'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=cca4deb1644d68964c57be835c0728ea'
    PARAMS={'units':'metric'}
    data=requests.get(url,PARAMS).json()
    if data.get('cod') != 200:
        # City not found or wrong city
        message = "Data is not available. Please check the city name."
        return render(request, 'index.html', {'message': message})
    description=data['weather'][0]['description']
    icon=data['weather'][0]['icon']
    temp=data['main']['temp']
    day=datetime.date.today()
    return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})