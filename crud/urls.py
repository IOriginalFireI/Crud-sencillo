
from django.contrib import admin
from django.urls import path
from cursos import views
from cursos.views import editar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="inicio"),
    path('editar/<int:pk>', editar.as_view(), name="editar"),
    path('eliminar/<int:curso_id>', views.eliminar, name="eliminar")
]
