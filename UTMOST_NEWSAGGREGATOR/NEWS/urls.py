from django.urls import path
from NEWS.views import scrape, news_list, register, login, home
from django.conf.urls import url


urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('scrape/', scrape, name="scrape"),
    path('', news_list, name="news"),
    url(r'^home/$',home,name='home'),
]