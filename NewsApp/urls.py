from django.conf.urls import url
from .views import index,TechRadar, techcrunch, wired ,theverge, thenextweb, engadget 

urlpatterns = [
url('', index, name = 'index'),
url('TechRadar/', TechRadar, name = 'TechRadar'),
url('techcrunch/', techcrunch, name = 'techcrunch'),
url('wired/', wired, name = 'wired'),
url('theverge/', theverge, name = 'theverge'),
url('thenextweb/', thenextweb, name = 'thenextweb'),
url('engadget/', engadget, name = 'engadget'),

]
