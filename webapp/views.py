# Módulos Para Mostrar o Resultado na Intrerface Web

# Imports
import pickle
import pandas as pd
from django.shortcuts import render
from django.views import View

# Classe
class HomeView(View):

    # Método Get
    def get(self, request, *args, **kwargs): 
        return render(request, "index.html")

    # Método Post
    def post(self, request, *args, **kwargs):
        
        # Obtém os dados do formulário
        indice_bolsa_sp = int(request.POST.get("indice_bolsa_sp"))
        inflacao_alta = int(request.POST.get("inflacao_alta"))
        taxa_desemprego = int(request.POST.get("taxa_desemprego"))
        taxa_juros = int(request.POST.get("taxa_juros"))

        # Carrega o modelo
        pickle_in = open("webapp/modelos/modelo_v1.pickle", "rb")
        linear = pickle.load(pickle_in)

        # Faz as previsões
        prediction = linear.predict(pd.DataFrame([[indice_bolsa_sp, inflacao_alta, taxa_desemprego, taxa_juros]], columns = ["indice_bolsa_sp", "inflacao_alta", "taxa_desemprego", "taxa_juros"]))
        prediction_point = prediction[0]

        # Classificação (cut-off)
        if prediction_point >= 1.35:
            predict = "A Tendência do Mercado é de Alta!"
        else:
            predict = "A Tendência do Mercado é de Baixa!"
        
        # Passando o resultado para o arquivo html
        context = {"prediction_point":prediction_point, "predict":predict}

        return render(request, "resultado.html", context)


        