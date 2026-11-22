from decimal import Decimal
from django.shortcuts import render, get_object_or_404, redirect
from busca_match.models import Carona
from .models import Pagamento


def realizar_pagamento(request, carona_id):
    carona = get_object_or_404(Carona, id=carona_id)
    valor_padrao = Decimal('15.00')

    if request.method == 'POST':
        metodo = request.POST.get('metodo', 'PIX')
        nome_pagador = request.POST.get('nome_pagador', '').strip()

        if not nome_pagador and request.user.is_authenticated:
            nome_pagador = request.user.get_full_name() or request.user.username
        elif not nome_pagador:
            nome_pagador = 'Passageiro Universitário'

        status_inicial = 'PENDENTE' if metodo == 'DINHEIRO' else 'PAGO'

        pagamento = Pagamento.objects.create(
            carona=carona,
            passageiro=request.user if request.user.is_authenticated else None,
            nome_pagador=nome_pagador,
            valor=valor_padrao,
            metodo=metodo,
            status=status_inicial,
        )

        return redirect('comprovante_pagamento', pagamento_id=pagamento.id)

    nome_sugerido = ''
    if request.user.is_authenticated:
        nome_sugerido = request.user.get_full_name() or request.user.username

    return render(request, 'pagamento/pagamento.html', {
        'carona': carona,
        'valor': valor_padrao,
        'nome_sugerido': nome_sugerido,
    })


def comprovante_pagamento(request, pagamento_id):
    pagamento = get_object_or_404(Pagamento, id=pagamento_id)
    return render(request, 'pagamento/comprovante.html', {
        'pagamento': pagamento,
    })