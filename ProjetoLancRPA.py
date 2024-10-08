import pyautogui as py ### Fazendo o código a partir da ideia do arquivo exe
import time as tm

empresa_atual = ''
cliente_atual = ''
serie_atual = ''
data_atual = ''
portador_atual = ''
codigo_atual = ''
valor_atual = ''
obs_atual = ''
cont = 0
global p_r

dict_lancamentos = [] #{'empresa': empresa_atual, 'cliente': cliente_atual, 'serie': serie_atual, 'data': data_atual, 'portador': portador_atual, 'codigo': codigo_atual, 'valor': valor_atual, 'obs': obs_atual}

def receber_valores():

    empresa_atual = py.prompt("1- Burguer  3- ACM  5- O Ludico  6- Holding Fabrica","Digite o nome da empresa ")
    cliente_atual = py.prompt("(Certifique-se que o nome escrito é exatamente como está cadastrado no sistema, caso contrário o Leo2D2 não irá encontrar)", "Digite o cliente" )
    serie_atual = py.prompt("RPA ou DRE?", "Digite a série")
    data_atual = py.prompt("Digite a data utilizada")
    portador_atual = py.prompt("4. Itaú  6. Satander  3. Banco do Brasil etc...", "Digite o codigo do portador")
    codigo_atual = py.prompt("Digite o codigo gerencial")
    valor_atual = py.prompt("Digite o valor")
    obs_atual = py.prompt("Digite a OBS")

    novo_lancamento = {'empresa': empresa_atual, 'cliente': cliente_atual, 'serie': serie_atual, 'data': data_atual, 'portador': portador_atual, 'codigo': codigo_atual, 'valor': valor_atual, 'obs': obs_atual}

    dict_lancamentos.append(novo_lancamento)

prompt = ""

def sleep1():
    tm.sleep(1)

def sleep2():
    tm.sleep(2)

def altTab():
    py.hotkey('alt', 'tab')

def fecharSistema():
    sleep2
    py.alert(text="Programa Finalizado")

def abrirCARdoMenu():
    ### Selecionar o CAR na primeira tela de menu
    sleep2()
    sleep2()
    py.click(922, 434)

def SelectLancTitulosCAR():
    ### Selecionar lançamentos, 
    sleep2()
    sleep2()
    py.click(65, 808)
    ### títulos a receber
    sleep2()
    py.click(71, 202)

def selectLancTitulosCAP():
    ### Selecionar lançamentos, 
    sleep2()
    sleep2()
    py.click(59, 778)
    ### títulos a pagar
    sleep2()
    py.click(104, 250)

def abrirPlanilha():
    ### A planilha precisa estar no primeiro "slot" da barra de ferramentas
    py.click(329, 1054)
    sleep1()

def abrirGoogle():
    ### Abrir google Duh!!! PRECISA ESTAR NO SEGUNDO SLOT DA BARRA DE FERRAMENTAS
    py.click(410, 1058)
    sleep2

def selectEmpresa():
    global cont
    sleep2()
    sleep2()
    py.doubleClick()
    py.press('backspace')
    sleep1
    py.write(dict_lancamentos[cont]['empresa'])
    sleep1
    py.press('enter')

def selectCliente():
    ### Selecionar o cliente
    global cont
    sleep1()
    py.press('tab')
    sleep1()
    py.write(dict_lancamentos[cont]['cliente'])
    sleep1()
    py.press('enter')
    sleep1()

def selectSerie():
     ### Selecionar a serie
    global cont
    sleep1()
    #py.press('tab')
    #sleep1()
    py.write(dict_lancamentos[cont]['serie'])
    sleep1()
    py.press('enter')
    sleep1()

def PrintDataTab():
    global cont
    sleep1()
    py.write(dict_lancamentos[cont]['data'])
    sleep1()
    py.press('tab')

def selectPortador():
    global cont
    # sleep1()
    # py.press('tab')
    sleep1()
    py.write(dict_lancamentos[cont]['portador'])
    sleep1()    
    py.press('enter')
    sleep1()

def selectConta():
    global cont
    ### Verificar a quantidade de tabs
    sleep1()
    py.press('tab')
    sleep1()
    py.write(dict_lancamentos[cont]['codigo'])
    sleep1()
    py.press('enter')
    sleep1()

def selectValor():
    global cont
    sleep1()
    py.write(dict_lancamentos[cont]['valor'])
    sleep1()

def selectParcelas():
    global cont
    sleep1()
    py.press('tab')
    sleep1()
    py.press('tab')
    sleep1()
    py.write("1")
    sleep1()
    py.press('enter')
    sleep1()

def selectObsRecebimentos():
    global cont
    i = 0
    while(i != 8):
        py.press('tab')
        sleep1()
        i = i + 1

    py.write(dict_lancamentos[cont]['obs'])
    sleep1()

def selectObsPagamentos():
    global cont
    i = 0
    while(i != 5):
        py.press('tab')
        sleep1()
        i = i + 1

    py.write(dict_lancamentos[cont]['obs'])
    sleep1()

def salvaLanc():
    global cont
    sleep1()
    #py.click(252, 209)
    sleep2()

def lancRecebimentos(): ### Adicionar algo pra limpar a caixa de condições de pagamento 

    SelectLancTitulosCAR() ### Selecionar "lançamentos" e "títulos"

    selectEmpresa() ### Selecionar a empresa

    selectCliente() ### Selecionar o cliente

    selectSerie()  ### Seleciona a serie

    PrintDataTab() ### Selecionar a data 2 vezes
    PrintDataTab()
    
    selectPortador() ### Selecionar o portador (banco)

    selectConta() ### Selecionar a conta gerencial 

    selectValor() ### Selecionar o valor 

    selectParcelas() ### Selecionar parcela 1

    PrintDataTab() ### colocar a mesma data que as outras (por enquanto)

    selectObsRecebimentos() ### Colocar a obs com o historico da planilha, sem lanc sj3

    prompt = py.prompt(text="Digite abaixo -salvar- para confirmar o lançamento?")

    if(prompt == "salvar"):
        salvaLanc() ### Salvar

def lancPagamentos(): #######

    selectLancTitulosCAP() ### Selecionar "lançamentos" e "títulos"

    selectEmpresa() ### Selecionar a empresa

    selectCliente() ### Selecionar o cliente

    selectSerie()  ### Seleciona a serie

    PrintDataTab() ### Selecionar a data 3 vezes
    PrintDataTab()
    PrintDataTab()
    py.press('tab')
    
    selectPortador() ### Selecionar o portador (banco)

    selectConta() ### Selecionar a conta gerencial 

    selectValor() ### Selecionar o valor 

    selectParcelas() ### Selecionar parcela 1

    PrintDataTab() ### colocar a mesma data que as outras (por enquanto)

    selectObsPagamentos() ### Colocar a obs com o historico da planilha, sem lanc sj3

    prompt = py.prompt(text="Digite abaixo -salvar- para confirmar o lançamento?")

    if(prompt == "salvar"):
        salvaLanc() ### Salvar

def minimizaVScode():
    sleep2
    py.click(1804, 17)
    sleep2

def prompt_P_R():
    global cont
    p_r = py.prompt('Os lançamentos são pagamentos ou recebimentos? P / R')
    return p_r 

def chama_func_P_R(p_r):
    global cont
    global quantidade_lancamentos
    if p_r == 'P' or p_r == 'p':
        lancPagamentos()
        avalia_se_acabou(quantidade_lancamentos, p_r)

    elif p_r == 'R' or p_r == 'r':
        lancRecebimentos()
        avalia_se_acabou(quantidade_lancamentos, p_r)

    else: 
        py.alert('Opção Inválida, escolha novamente')
        prompt_P_R()

def avalia_se_acabou(quantidade_lancamentos, p_r):
    global cont
    cont = cont + 1
    if cont == quantidade_lancamentos:
           fecharSistema()
    else: 
            chama_func_P_R(p_r)


def main():
    global cont
    global quantidade_lancamentos
    bool = True
    sleep1
    py.alert(text="Cuidado com seu mouse e Teclado, o programa vai rodar!")
    sleep1

    py.alert(text="Certifique-se que o everest HTML está aberto, e já está com o CAR ou no CAP aberto!")
    py.alert(text="Você confirmou na tesouraria se esses lançamentos já foram feitos ?" )  

    while bool == True:
        receber_valores() 
        s_n = py.prompt('Adicionar novo lançamento a fila? S / N')
        if s_n == 'S' or s_n == 's':
            bool = True 
        else: 
            bool = False

    quantidade_lancamentos = len(dict_lancamentos)
    print(quantidade_lancamentos)

    p_r = prompt_P_R() # talvez isso aqui funcione, não sei bem usar função

    chama_func_P_R(p_r)


###minimizaVScode()

main()



