from django.urls import path
from . import views

app_name = 'tools_lst'

urlpatterns = [
    path('', views.tools, name='tool_list')
]