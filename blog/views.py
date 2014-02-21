from django.shortcuts import render
from models import Artigo
from models import Book
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test


def latest_books(request):
    book_list = Book.objects.order_by('-pub_date')
    return render(request, 'latest_books.html', {'book_list': book_list})

def usuario_esta_logado(user):# Verifica se usuario esta logado
    return user.is_authenticated()

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/deslogado")

def artigo(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    if request.method == 'POST':
        artigo.link_qrcode = request.POST.get('link_qrcode', '')
        artigo.titulo = request.POST.get('titulo', '')
        artigo.tipo = request.POST.get('tipo', '')
        artigo.tema = request.POST.get('tema', '')
        artigo.link = request.POST.get('link', '')
        artigo.save()
        return HttpResponseRedirect('/')
    return render(request,'artigo.html', locals())

def artigo_add(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo', '')
        link= request.POST.get('link', '')
        tema= request.POST.get('tema', '')
        tipo= request.POST.get('tipo', '')
        artigo=Artigo(titulo=titulo, link=link, tema=tema, tipo=tipo)
        artigo.save()
        return HttpResponseRedirect('/')
    return render(request,'adicionar_conteudo.html')

def home_view(request):
    artigo = Artigo.objects.all()
    return render(request, 'artigo_archive.html', {'artigo':artigo})

def pagina_de_redirecionamento(request):
    return render(request, 'pagina_de_redirecionamento.html',)

def logon_sucesso(request):
    return render(request, 'logon_sucesso.html',)

def artigo_del(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    if request.method == 'POST':
        artigo.delete()
        return HttpResponseRedirect('/')

def artigo_redirect(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    return HttpResponseRedirect(artigo.link)


@user_passes_test(usuario_esta_logado)
def deslogado(request):
    return render(request,'deslogado.html')

@user_passes_test(usuario_esta_logado) #Executa usuario_esta_logado antes de home_view, e usuaio_esta_logado verifica se o usuario esta logado, so permitindo, assim, que home_view seja executada se usuario_esta_logado retornar true
def autorizado(request):
    return render(request, 'autorizado.html',)



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
