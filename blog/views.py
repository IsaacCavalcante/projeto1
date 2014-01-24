from django.shortcuts import render
from models import Artigo
from models import Book

def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render(request, 'latest_books.html', {'book_list': book_list})

def home_view(request):
	artigo = Artigo.objects.all()[0]
	return render(request, 'artigo_archive.html', {'artigo':artigo})
	
def pagina_de_redirecionamento(request):
	return render(request, 'pagina_de_redirecionamento.html',)

def pagina_logon(request):
	return render(request, 'teste.html',)

# Create your views here.
