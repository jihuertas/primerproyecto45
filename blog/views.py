from django.shortcuts import render
from .models import Post,Autor, Categoria

# Create your views here.
def principal(request):
    posts = Post.objects.filter(titulo__icontains='entrada')
    categorias = Categoria.objects.all()

    contexto = {'posts':posts,'categorias':categorias}
    return render(request, 'blog/principal.html', contexto)

def detalle_post(request, pk):
    post= Post.objects.get(id=pk)

    return render(request, 'blog/detalle_post.html', {'post':post})


def ji(request):
    return render(request, 'blog/ji.html')

def alumnado(request):
    return render(request, 'blog/alumnado/javier.html')

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'blog/autores.html', {'autores':autores})

def autor(request, pk):
    autor= Autor.objects.get(id=pk)
    posts= Post.objects.filter(autor=pk)


    return render(request, 'blog/autor.html', {"posts":posts, "autor":autor})

def categoria(request, pk):
    categoria= Categoria.objects.get(pk=pk)
    return render(request, 'blog/categoria.html', {"categoria":categoria})