import pyautogui as py ### Fazendo o código a partir da ideia do arquivo exe
import time as tm

### (Fazer depois) Abrir o sistema, planilha

empresaAtual = "5" ### Lúdico
clienteAtual = "xxx"
serieAtual = "DRE"
dataAtual = "28082024"
portadorAtual = "6"
contaAtual = 'x'
valorAtual = 'xxxx'
obs = 'x'

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
    py.click(922, 434)

def SelectLancTitulos():
    ### Selecionar lançamentos, 
    sleep2()
    py.click(65, 808)
    ### títulos a receber
    sleep2()
    py.click(71, 202)

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
    py.press('tab')
    sleep1()
    py.write(serieAtual)
    sleep1()
    py.press('enter')
    sleep1()

def tabPrintData():
    sleep1()
    py.press('tab')
    sleep1()
    py.write(dataAtual)

def selectPortador():
    sleep1()
    py.press('tab')
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
def selectValor():
    sleep1()
    py.press('tab')
    sleep1()
    py.write(valorAtual)
    sleep1()
def selectParcelas():
    sleep1()
    py.press('tab')
    sleep1()
    py.write("1")
    sleep1()
def selectOBS():
    sleep1()
    py.press('tab')
    sleep1()
    py.write(obs)
    sleep1()

def salvaLanc():
    sleep1()
    py.cick(alguma coisaaaaaaaa)
    sleep2()




def main():
    py.alert(text="Cuidado com seu mouse e Teclado, o programa vai rodar!")
    sleep1

    abrirGoogle()

    ################## Sessão Contas A Receber

    abrirCARdoMenu()

        ### Checar se os lançamentos da planilha já não estão lançados

    SelectLancTitulos() ### Selecionar "lançamentos" e "títulos"

    selectEmpresa() ### Selecionar a empresa

    selectCliente() ### Selecionar o cliente

    selectSerie()  ### Seleciona a serie

    tabPrintData()    ### Selecionar a data 2 vezes
    tabPrintData()
    
    selectPortador() ### Selecionar o portador (banco)

    selectConta() ### Selecionar a conta gerencial 

    selectValor() ### Selecionar o valor 

    selectParcelas() ### Selecionar parcela 1

    tabPrintData() ### colocar a mesma data que as outras (por enquanto)

    selectOBS() ### Colocar a obs com o historico da planilha, sem lanc sj3

    salvaLanc() ### Salvar

        ### Pintar a planilha

        ### Ir para a próxima linha da planilha 

        ### reiniciar 

     





    fecharSistema()


main()



