from django.shortcuts import render


# Create your views here.
def exibir_portfolio(request):
    return render(request, 'portfolios/exibir_portfolio.html', {})
