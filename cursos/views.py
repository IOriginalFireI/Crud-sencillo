from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from .forms import *
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import *


# Create your views here.


def index(request):
    
    cursos = curso.objects.all()
    curso_formulario = formulario_curso()
    if request.method == "GET":
        return render (request, 'index.html', {"cursos": cursos, "formulario_cursos": curso_formulario})
    else:
        curso_formulario = formulario_curso(request.POST)
        if curso_formulario.is_valid():
            curso_formulario.save()
            messages.success(request, "Curso guardado.")
            return redirect('inicio')
    
    return render (request, 'index.html', {"cursos": cursos, "formulario_cursos": curso_formulario})   

class editar(UpdateView):
    
    model = curso
    form_class = formulario_curso
    template_name = 'editar.html'
    success_url = reverse_lazy('inicio')
    pass    

def eliminar(request, curso_id):
    
    if request.method == "GET":
        eliminar_curso = get_object_or_404(curso, pk=curso_id)
        eliminar_curso.delete()
        return redirect('inicio')