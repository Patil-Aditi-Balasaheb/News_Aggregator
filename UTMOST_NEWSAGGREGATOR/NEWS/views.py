import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from NEWS.models import Headline, Users

def scrape(request):
    session = requests.Session()
    session.headers = {"User-Agent":"Googlebot/2.1(+http://www/google.com/bot.html)"}
    url = "https://www.theonion.com/"
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    News = soup.find_all('div',{"class":"curation-module__item"})
    for article in News:
        main = article.find_all('a')[0]
        link = main['href']
        image_src = str(main.find('img')['srcset']).split(" ")[-4]
        title = main['title']
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = image_src
        new_headline.save()
    return redirect("../")

def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "NEWS/home.html", context)


def register(request):
    if request.method=='POST':
        if request.POST.get('topnews')=='on':
            topnews=True
        else:
            topnews=False
        if request.POST.get('business')=='on':
            business=True
        else:
            business=False
        if request.POST.get('technology')=='on':
            technology=True
        else:
            technology=False
        if request.POST.get('entertainment')=='on':
            entertainment=True
        else:
            entertainment=False
        if request.POST.get('sports')=='on':
            sports=True
        else:
            sports=False
        if request.POST.get('science')=='on':
            science=True
        else:
            science=False
        if request.POST.get('health')=='on':
            health=True
        else:
            health=False
        if request.POST.get('phno_2')=='':
            alternate_contact = 0
        # user = Users(email=request.POST['email'],password=request.POST['pwd'],firstname=request.POST['fname'],lastname=request.POST['lname'],gender=request.POST['gender'],topnews=request.POST['topnews'],business=request.POST['business'],technology=request.POST['technology'],entertainment=request.POST['entertainment'],sports=request.POST['sports'],science=request.POST['science'],health=request.POST['health'])
        user = Users(email=request.POST['email'],password=request.POST['pwd'],firstname=request.POST['fname'],lastname=request.POST['lname'],gender=request.POST['gender'],contact=request.POST['phno'],alternate_contact=alternate_contact,topnews=topnews,business=business,technology=technology,entertainment=entertainment,sports=sports,science=science,health=health)
        user.save()
        context={'msg':'You have successfully Signed Up! Login to your Account', 'class':'text-success'}
        return render(request,'NEWS/login.html',context)
    else:
        return render(request,'NEWS/register.html')
    
def login(request):
    return render(request,'NEWS/login.html')

def home(request):
    if request.method=='POST':
        if Users.objects.filter(email=request.POST['email'],password=request.POST['pwd']).exists():
            member=Users.objects.get(email=request.POST['email'],password=request.POST['pwd'])
            return render(request,'NEWS/home.html',{'member':member,'msg':'Successfully logged in!'})
        else:
            context={'msg':'Invalid username or password', 'class':'text-danger'}
            return render(request,'NEWS/login.html',context)
            