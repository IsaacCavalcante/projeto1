from django.shortcuts import render
from models import Artigo
from models import Book
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test


def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render(request, 'latest_books.html', {'book_list': book_list})

def usuario_esta_logado(user):# Verifica se usuario esta logado
    return user.is_authenticated()

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/deslogado")

@user_passes_test(usuario_esta_logado) #Executa usuario_esta_logado antes de home_view, e usuaio_esta_logado verifica se o usuario esta logado, so permitindo, assim, que home_view seja executada se usuario_esta_logado retornar true
def home_view(request):
	artigo = Artigo.objects.all()[0]
	return render(request, 'artigo_archive.html', {'artigo':artigo})
	
def pagina_de_redirecionamento(request):
	return render(request, 'pagina_de_redirecionamento.html',)

def logon_sucesso(request):
	return render(request, 'logon_sucesso.html',)

@user_passes_test(usuario_esta_logado)
def deslogado(request):
    return render(request,'deslogado.html')



def pagina_logon(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name",'')#variavel que recebe o valor do input de usario no HTML
        password = request.POST.get("password",'')#variael que recebe o valor do input de senha no HTML
        user = auth.authenticate(username = user_name, password = password)#Procura para voce, o usuario e senha correspondente no banco de dados ja default do django, se os resultados nao condizerem com os do banco, entao o retorno para user eh None

        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/logonsucesso')
        else:
            return HttpResponseRedirect('/logon')


    return render(request, 'teste.html',)





# Create your views here.
