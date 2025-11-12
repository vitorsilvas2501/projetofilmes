from django.shortcuts import render, redirect,get_object_or_404
from .models import Filme

# Create your views here.
def home(request):
    return render(request, 'filmes/home.html')
def cadastro(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        comentario = request.POST.get('comentario')
        nota = request.POST.get('nota')
        imagem_url = request.POST.get('imagem_url')

        Filme.objects.create(
            titulo = titulo,
            comentario = comentario,
            nota = nota,
            imagem_url=imagem_url
    
        )
        return redirect('lista')
    return render(request, 'filmes/cadastro.html')
def lista(request):
    filmes = Filme.objects.all()
    context = {'filmes': filmes }
    return render(request, 'filmes/lista.html', context)
    
def detalhes(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    context = {'filme': filme}
    return render(request, 'filmes/detalhes.html', context)


def deletar(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    filme.delete()
    return redirect('lista')

def atualizar(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        filme.titulo = request.POST.get('titulo')
        filme.comentario = request.POST.get('comentario')
        filme.nota = request.POST.get('nota')
        filme.imagem_url = request.POST.get('imagem_url')
        filme.save()
        return redirect('detalhes', filme_id=filme.id)
    
    context = {'filme': filme}
    return render(request, 'filmes/atualizar.html', context)
        
    


   