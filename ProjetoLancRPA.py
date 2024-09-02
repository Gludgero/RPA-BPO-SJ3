import pyautogui as py ### Fazendo o código a partir da ideia do arquivo exe
import time as tm

### (Fazer depois) Abrir o sistema, planilha   

empresaAtual = "3" ### 

#clienteAtual = py.prompt(text="Qual o cliente atual?") ##################################
clienteAtual = "MEGA"

#serieAtual = "DRE" 
serieAtual = 'DPA'

dataAtual = "30082024"

portadorAtual = "4"

#contaAtual = py.prompt(text="Qual a conta atual?") ##############################
contaAtual = "99"

#valorAtual = py.prompt(text="Qual o valor atual?") ########################
valorAtual = "2591,50"

#obs = py.prompt(text="Qual a obs atual?") ########################################
obs = "NOVA MEGA G ATACADISTA DE A"

nLinhas = 0
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
    sleep2()
    sleep2()
    py.doubleClick()
    py.press('backspace')
    sleep1
    py.write(empresaAtual)
    sleep1
    py.press('enter')

def selectCliente():
    ### Selecionar o cliente
    sleep1()
    py.press('tab')
    sleep1()
    py.write(clienteAtual)
    sleep1()
    py.press('enter')
    sleep1()

def selectSerie():
     ### Selecionar a serie
    sleep1()
    #py.press('tab')
    #sleep1()
    py.write(serieAtual)
    sleep1()
    py.press('enter')
    sleep1()

def PrintDataTab():
    sleep1()
    py.write(dataAtual)
    sleep1()
    py.press('tab')

def selectPortador():
    # sleep1()
    # py.press('tab')
    sleep1()
    py.write(portadorAtual)
    sleep1()    
    py.press('enter')
    sleep1()

def selectConta():
    ### Verificar a quantidade de tabs
    sleep1()
    py.press('tab')
    sleep1()
    py.write(contaAtual)
    sleep1()
    py.press('enter')
    sleep1()

def selectValor():
    sleep1()
    py.write(valorAtual)
    sleep1()

def selectParcelas():
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
    i = 0
    while(i != 8):
        py.press('tab')
        sleep1()
        i = i + 1

    py.write(obs)
    sleep1()

def selectObsPagamentos():
    i = 0
    while(i != 5):
        py.press('tab')
        sleep1()
        i = i + 1

    py.write(obs)
    sleep1()

def salvaLanc():
    sleep1()
    py.click()
    sleep2()

def lancRecebimentos():

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

def receberValores():
    sleep1()
    nLinhas = py.prompt(text="Qual o número de lançamentos você quer fazer?")

def main():

    sleep1
    py.alert(text="Cuidado com seu mouse e Teclado, o programa vai rodar!")
    sleep1

    minimizaVScode()

    #abrirCARdoMenu()

    #py.alert(text="Você confirmou se alguns dos lançamentos já foram feitos?" )  

    #lancRecebimentos()

    lancPagamentos() ### Adicionar algo pra limpar a caixa de condições de pagamento 

    fecharSistema() 

main()



