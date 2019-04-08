from django.shortcuts import render
from .models import DadosPessoais

# Create your views here.
def exibir_portfolio(request):
    pessoa = DadosPessoais.objects.all()
    context = {'pessoa':pessoa}
    return render(request, 'portfolios/exibir_portfolio.html', context)
