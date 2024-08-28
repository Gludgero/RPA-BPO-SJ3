import pyautogui as py ### Fazendo o código a partir da ideia do arquivo exe
import time as tm

### (Fazer depois) Abrir o sistema, planilha

empresaAtual = "5" ### Lúdico

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





def main():
    py.alert(text="Cuidado com seu mouse e Teclado, o programa vai rodar!")
    sleep1

    abrirGoogle()

    ################## Sessão Contas A Receber

    #abrirCARdoMenu()

        ### Checar se os lançamentos da planilha já não estão lançados

        ### Selecionar "lançamentos" e "títulos"

    SelectLancTitulos()

        ### Selecionar a empresa

    selectEmpresa()

        ### Selecionar o cliente

        ### Selecionar a serie

        ### Selecionar a data

        ### Selecionar o portador (banco)

        ### Selecionar a conta gerencial 

        ### Selecionar o valor 

        ### Selecionar parcela 1

        ### colocar a mesma data que as outras (por enquanto)

        ### Colocar a obs com o historico da planilha, sem lanc sj3

        ### Salvar

        ### Pintar a planilha

        ### Ir para a próxima linha da planilha 

        ### reiniciar 

     





    fecharSistema()


main()



