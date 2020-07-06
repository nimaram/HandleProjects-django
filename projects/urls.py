from django.urls import path
from . import views
app_name = 'project'
urlpatterns = [
    path('',views.home,name='home'),
    path('create',views.create,name='create'),
    path('detail/<slug:slug>',views.detail,name='detail'),
    path('delete/<int:user_id>/<slug:slug>',views.delete,name='delete'),
    path('edit/<slug:slug>/<int:user_id>',views.edit,name='edit'),
    path('addcontribution/<int:project>/<int:user_id>',views.addcont.as_view(),name='addContribution')
   ]
