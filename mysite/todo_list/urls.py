from django.urls import path, include

app_name = 'todo_list'
urlpatterns = [
    path("accounts/", include('django.contrib.auth.urls')),
]
