"""定义 learning_logs 的 URL 模式"""

from django.conf.urls import path

from . import views

urlpatterns  = [
    #主页
    path ('',views.index, name='index'),
]