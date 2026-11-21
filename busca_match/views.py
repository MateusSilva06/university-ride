from django.shortcuts import render, redirect, get_object_or_404
from .models import Carona

def busca_carona(request):
    caronas = None
    
    # Se a URL tiver os parâmetros de busca (quando o usuário clica em Buscar)
    if request.method == 'GET' and 'data' in request.GET:
        origem_busca = request.GET.get('origem')
        destino_busca = request.GET.get('destino')
        data_busca = request.GET.get('data')

        # Filtra no banco as caronas que batem com a pesquisa e têm vaga
        caronas = Carona.objects.filter(
            origem__icontains=origem_busca,
            destino__icontains=destino_busca,
            data=data_busca,
            vagas_disponiveis__gt=0
        )

    return render(request, 'busca_match/busca.html', {'caronas': caronas})

def confirmar_match(request, carona_id):
    if request.method == 'POST':
        carona = get_object_or_404(Carona, id=carona_id)
        
        if carona.vagas_disponiveis > 0:
            # Subtrai a vaga
            carona.vagas_disponiveis -= 1
            
            # Como o Dev 1 ainda não fez o Login, adicionamos o usuário apenas se ele estiver logado (ex: o superuser)
            if request.user.is_authenticated:
                carona.passageiros.add(request.user)
                
            carona.save()
            
            # Simula o envio para a tela do Dev 3 (Pagamento)
            return redirect('/pagamento-mockado/') 
            
    return redirect('busca_carona')