from django.urls import path
from . import views

urlpatterns = [
    path('<int:carona_id>/', views.realizar_pagamento, name='realizar_pagamento'),
    path('comprovante/<int:pagamento_id>/', views.comprovante_pagamento, name='comprovante_pagamento'),
]