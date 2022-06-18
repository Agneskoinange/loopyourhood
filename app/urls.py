from django.urls import path
from . import views


urlpatterns=[
  path('',views.home_page,name='home_page'),
  path('join/hood/<hood_id>',views.join_hood,name='join_hood'),
  path('hood/emergency-services',views.e_services,name='e_services'),
  path('hood/businesses',views.hood_bs,name='hood_bs'),
  path('hood/posts',views.hood_posts,name='hood_posts'),
  path('hood/myprofile',views.my_profile,name='my_profile'),
  path('hood/search/business',views.search_business,name='search_business')
]