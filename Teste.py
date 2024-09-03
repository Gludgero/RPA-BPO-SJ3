import pyautogui as py, sys

empresa_atual = '1'
cliente_atual = '2'
serie_atual = '3'
data_atual = '4'
portador_atual = '5'
codigo_atual = '6'
valor_atual = '7'
obs_atual = '8'
bool = True


#
dict_lancamentos = [{'empresa': empresa_atual, 'cliente': cliente_atual, 'serie': serie_atual, 'data': data_atual, 'portador': portador_atual, 'codigo': codigo_atual, 'valor': valor_atual, 'obs': obs_atual}]

def receber_valores():

    empresa_atual = py.prompt("Digite o nome da próxima empresa")
    cliente_atual = py.prompt("Digite o nome do próximo cliente")
    serie_atual = py.prompt("Digite a próxima serie ")
    data_atual = py.prompt("Digite a data utilizada")
    portador_atual = py.prompt("Digite o codigo do portador")
    codigo_atual = py.prompt("Digite o codigo gerencial")
    valor_atual = py.prompt("Digite o valor")
    obs_atual = py.prompt("Digite a OBS")

    novo_lancamento = {'empresa': empresa_atual, 'cliente': cliente_atual, 'serie': serie_atual, 'data': data_atual, 'portador': portador_atual, 'codigo': codigo_atual, 'valor': valor_atual, 'obs': obs_atual}

    dict_lancamentos.append(novo_lancamento)


while bool == True:
    #receber_valores() 
    s_n = py.prompt('Adicionar novo lançamento a fila? S / N')
    if s_n == 'S' or s_n == 's':
        bool = True 
    else: 
        bool = False

#print(dict_lancamentos)




print(dict_lancamentos[0]['empresa'])

