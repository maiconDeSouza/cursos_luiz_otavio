from django.contrib import admin
from django.urls import path, include

import recipes
import recipes.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(recipes.urls)),
]
