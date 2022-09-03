from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
                
                path('',views.base,name='base'),
                path('index',views.index,name='index'),
                path('update_centr/<int:pk>',views.update_centr,name='update_centr'),
                path('centr/<int:pk>',views.centr,name='centr'),
                path('costcentr',views.costcentr,name='costcentr'),
                path('group',views.group,name='group'),
                path('grp_alter/<int:pk>',views.grp_alter,name="grp_alter"),
                path('grp/<int:pk>',views.grp,name='grp'),
]