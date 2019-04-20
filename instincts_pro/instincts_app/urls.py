#from django.urls import path
from . import views

urlpatterns=[
    ('',views.hello)
    ]

# Import your view from your app directory
# In url patterns , we have to give the view. function name
# we have declared the function name as "index" , hence it was declared as "views.index"
#    path('',views.index,name='index')
