#!/usr/bin/env python
# coding: utf-8

# ## O que é uma API e porque é importante sabermos dela?
# 
# ### A API (Interface de Programação de Aplicações) é um conjunto de serviços/funções que foram implementadas em um programa de computador que são disponibilizados para que outros programas/aplicativos possam utiliza-los diretamente de forma simplificada; sem envolver-se em detalhes da implementação do programa de computador principal. A API é importante porque é através dela vamos disponibilizar os acessos as predições dos modelos de Machine Learning.

# In[1]:


from flask import Flask


# ## Criando uma API bem simples através da biblioteca Flask

# In[2]:


app = Flask("meu_app")

## Definindo a rota
@app.route('/')

def home():
    return "Minha primeira API"


# In[ ]:


app.run()

