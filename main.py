#Project of Portscanner created by @cvinicius369
#Lang: Python

#Imports
import      time
import    socket
import  datetime
import  colorama

from colorama  import Fore, Style

#Function for dercoration of aplication
def logo():
    print('                    .,-;;//;=,')
    print('                . :H@@MM@M#H/ .,+@;,')
    print('             ,/X+ +M@@M@MM%=,-%HMMM@X/,')
    print('           -+@MM; $M@@MH+-, ;XMMMM@MMMM@+-')
    print('          ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.')
    print('        ,%MM@@MH ,@%=            .---=-=:=,.')
    print('        =@#@@MX  .,              -%HX$$%%%+;')
    print('       =-./@M@M$                  .;@MMMM@MM:')
    print('       X@/ -$MM/                    .+MM@@@M$')
    print('      ,@M@H: :@:                    . =XH@@@@-')
    print('      ,@@MMX,  .                    /H- ;@M@M=')
    print('      .H@@@@M@+,                    %MM+..%#$.')
    print('       /MMMM@MMH/.                  XM@MH; =;')
    print('        /%+%$XHH@$=               , .H@@@MX,  ')
    print('         .=--------.            -%H.,@@@@@MX,')
    print('         .%MM@@@HHHXX$$$%+-  .:$MMX =M@@MM%.')
    print('           =XMMM@MM@MM#H; ,-+HMM@M+ /MMMX=')
    print('             =%@M@M#@$-. =$@MM@@@M; %M%=')
    print('               ,:+$+-,/H#MMMMMMMM@= =,')
    print('                     =++%%%%+/:-')

#Colors in texts
colorama.init()
#call of the logo()
logo()

#main class of the aplication, this is the principal tool of the aplication
class WhiteDragonKit:
    def port_scan():
        #Title with function of blue color
        title = '/////////////P O R T   S C A N N E R ///////////////////'
        print(Fore.BLUE + Style.BRIGHT + title + Fore.RESET)

        #Ports and Objetive definition
        ports = [20, 21, 23, 25, 80, 110, 135, 443, 3306]
        inforalvo = 'Informe o alvo abaixo'
        print(Fore.YELLOW + Style.BRIGHT + inforalvo + Fore.RESET)

        alvo = input('->')
        print('---------------------------------------------------')
        abertas = []

        #Porting Tests 
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5)
            code = client.connect_ex((alvo, port))
            
            portaaberta = '===| Porta Aberta '
            portafechada = '==| Porta Fechada'
            
            #Conditional Estructure
            if code == 0:
                time.sleep(0.4)
                
                print(f'Porta: {port}')
                print(Fore.GREEN + Style.BRIGHT + portaaberta + Fore.RESET)
                print(f'Codigo {code}')
                print('-------------------------------------------------------')
                abertas(code)
                
            else:
                time.sleep(0.4)
                
                print(f'Porta: {port}')
                print(Fore.RED + Style.BRIGHT + portafechada + Fore.RESET)
                print(f'Codigo {code}')
                print('-------------------------------------------------------')

#menu class, this is for organization and decoration of the aplication
class Menu:
    def m1():
        hoje = datetime.datetime.now()
        print(hoje)
        print("[1]-Port Scanner\n[2]-DNS Brute\n[3]-Remote Conection Client\n[4]-Remote Conection Server")
        action = int(input("-> "))

        if (action == 1):
            print("< Iniciando > ")
            cont = 3
            while (cont > 1):
                print(cont)
                cont -= 1
            try:
                wdtk.port_scan()
            except:
                print("Erro ao executar função")
        else:
            print("I N V A L I D !")

#Object instancied and calling the Menu class
wdtk = WhiteDragonKit()
Menu.m1()