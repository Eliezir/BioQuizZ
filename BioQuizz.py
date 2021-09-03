###

import pygame
import random
import webbrowser
import time


pygame.init()
    #Tamanhos

largura= 1280
altura = 720

    # CORES
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
cinza = (47, 79, 79)
verde = (0, 128, 0)
azul = (0, 0, 255)
amarelo = (255, 255, 0)
roxo = (128, 0, 128)
ciano = (0, 255, 255)
rosa = (255, 20, 147)

    #Inicialização
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('BioQuizz')

    #imagens
fundo = pygame.image.load("menu.png")
fcredito = pygame.image.load("fundo_creditos.png")
setapng = pygame.image.load("seta beta.png")
caixamudo = pygame.image.load("mudo2.png")
caixasom = pygame.image.load("som2.png")
dicasoff = pygame.image.load("dicasoff.png")
fEnd = pygame.image.load("fim de jogo.png")
fWin = pygame.image.load("telaVitoria.png")
    #Botões cinzas
botaoA = pygame.image.load("botaoA.png")
botaoB = pygame.image.load("botaoB.png")
botaoC = pygame.image.load("botaoC.png")
botaoD = pygame.image.load("botaoD.png")

    #musica
acerto = pygame.mixer.Sound("Love Alarm Heart Notification Sound.mp3")
erro = pygame.mixer.Sound("SOM ERRO DE WINDOWS   PARA EDIÇÃO.mp3")
_songs = ["musica1.mp3","musica2.mp3","musica3.mp3","musica4.mp3","musica5.mp3","musica6.mp3","musica7.mp3","musica8.mp3","musica9.mp3","musica10.mp3","musica11.mp3"]
_currently_playing_song = None_currently_playing_song = None
# FPS
relogio = pygame.time.Clock()
FPS = 60
    #MENUDICAS
tuto1 = pygame.image.load("menu t1.jpg")
tuto2 = pygame.image.load("menu t2.jpg")
tuto3 = pygame.image.load("menu t3.jpg")
tutorial = ['',tuto1,tuto2,tuto3]
    #PERGUNTAS
pg1 = pygame.image.load("pg01.jpg")
pg2 = pygame.image.load("pg02.jpg")
pg3 = pygame.image.load("pg03.jpg")
pg4 = pygame.image.load("pg04.jpg")
pg5 = pygame.image.load("pg05.jpg")
pg6 = pygame.image.load("pg06.jpg")
pg7 = pygame.image.load("pg07.jpg")
pg8 = pygame.image.load("pg08.jpg")
pg9 = pygame.image.load("pg09.jpg")
pg10 = pygame.image.load("pg10.jpg")
pg11 = pygame.image.load("pg11.jpg")
pg12 = pygame.image.load("pg12.jpg")
pg13 = pygame.image.load("pg13.jpg")
pg14 = pygame.image.load("pg14.jpg")
pg15 = pygame.image.load("pg15.jpg")
pg16 = pygame.image.load("pg16.jpg")
pg17 = pygame.image.load("pg17.jpg")
pg18 = pygame.image.load("pg18.jpg")
pg19 = pygame.image.load("pg19.jpg")
pg20 = pygame.image.load("pg20.jpg")
pg21 = pygame.image.load("pg21.jpg")
pg22 = pygame.image.load("pg22.jpg")
pg23 = pygame.image.load("pg23.jpg")
pg24 = pygame.image.load("pg24.jpg")
    #bonus
bn1 = pygame.image.load("bonus01.png")
bn2 = pygame.image.load("bonus02.png")
bn3 = pygame.image.load("bonus03.png")
bn4 = pygame.image.load("bonus04.png")
perguntas = ['',pg1,pg2,pg3,pg4,pg5,bn1,pg6,pg7,pg8,pg9,pg10,bn2,pg11,pg12,pg13,pg14,pg15,bn3,pg16,pg17,pg18,pg19,pg20,bn4,pg21,pg22,pg23,pg24,fWin]
pgbonus = ['',bn1,bn2,bn3,bn4]

    #VideoAulas
aula = ['0','https://www.youtube.com/watch?v=Zsw1FAUcgkw','https://youtu.be/iE1J4slMWzo?t=56','https://www.youtube.com/watch?v=qmpd44TxYpg','https://youtu.be/08LPYpObAxw','https://youtu.be/yGvKVuWR7cY?t=64','bn1','https://www.youtube.com/watch?v=mnZV05we49Q','https://youtu.be/oUzBsQUODuI','https://youtu.be/emucgjvtdw0','https://youtu.be/lcRU_q2B-hY?t=249','https://www.youtube.com/watch?v=Wawh1EfNSwU','bn2','https://youtu.be/PGvkQL2Q6OU','https://youtu.be/UGj4x0uAuio','https://youtu.be/Zsw1FAUcgkw','https://www.youtube.com/watch?v=4dtyvpswmhE&t=78s','https://youtu.be/6-pmW3vob28?t=22','bn3','https://www.youtube.com/watch?v=ny5-QYxNuh8','https://youtu.be/4bBRq0sY7Do','https://youtu.be/asDzvBZ-Q2o?t=23','https://youtu.be/qrBQ_ELTESk','https://youtu.be/SO2arCfdtG4?t=30','bn4','https://www.youtube.com/playlist?list=PLsutL2TqSEP_sMrC0ABWb6QK7wq9i8Q4A','https://youtu.be/eh6WqQn7B8w?t=279','https://www.youtube.com/watch?v=4dtyvpswmhE&t=78s','https://youtu.be/3SmyPBbmRmQ']
sair = False
def video(link):
    webbrowser.open(link)
fila = random.randint(0,10)
def song():
    if pygame.mixer.music.get_busy() == False and sair == False:
        global _songs
        _songs = _songs[1:] + [_songs[0]]
        pygame.mixer.music.load(_songs[fila])
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.8)

    # Mensagem -
def texto(msg, cor, tamanho, x, y):
    fonte = pygame.font.SysFont("Source Sans Pro Black",tamanho)
    txt1 = fonte.render(msg, True, cor)
    janela.blit(txt1, [x, y])

def menu():
    janela.blit(fundo, (0, 0))
def creditos():
    janela.blit(fcredito,(0, 0))
def seta():
    janela.blit(setapng,(1195, 63))
def tela(pagina):
    janela.blit(pagina,(0, 0))
def perdeu():
    janela.blit(fEnd,(0, 0))
def ganhou():
    janela.blit(fWin,(0, 0))
def pontos(msg,cor,x,y):
    texto(msg,cor, 35, x,y)
    pygame.display.update()
    time.sleep(1.5)
SONG_END = pygame.USEREVENT + 1
def jogo():
    #Chaves
    sair = False
    inicio = True
    credit = False
    dicas = False
    start = True
    som = True
    resposta  = False
    jogar = False
    rodada = False
    fim = False
    win = False
    cortes = []
    #Variaveis
    aba = 1
    fase = 1
    ajuda = 1
    vidas = 2
    while start == True and sair == False:
        #ABA DO MENU INICIAL
        while inicio == True:
            menu()
            if som == True:
                janela.blit(caixasom,(37,43))
                pygame.mixer.music.unpause()
                song()
            elif som == False:
                janela.blit(caixamudo,(39,43))
                pygame.mixer.music.pause()
            pygame.display.update()
            for event in pygame.event.get():
                #saida
                if event.type == pygame.QUIT:
                    sair = True
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        #botões
                        if x > 37 and x < 90 and y > 43 and y < 103:
                            if som == False:
                                som = True
                            elif som == True:
                                som = False

                        elif x > 480 and x < 825 and y >336 and y < 423:
                            inicio = False
                            jogar = True
                        elif x > 260 and x < 630 and y > 425 and y < 535:
                            inicio = False
                            dicas = True
                        elif x>650 and x <1010 and y>425 and y < 535:
                            inicio = False
                            credit = True
        #ABA DO QUIZZ
        while jogar == True and vidas > 0:
            if som == True:
                song()
            vidatexto = 'x' + str(vidas)
            # Lista Respostas
            resp = ['','A','A','C','B','C','Z','D','C','B','A','D','C','D','B','D','D','C','C','B','A','A','A','C','B','B','A','A','A']
            tela(perguntas[fase])
            texto(vidatexto,preto,45,1012,25)
            if ajuda == 0 or fase == 6 or fase == 12 or fase == 18 or fase == 24:
                janela.blit(dicasoff, (913, 30))
            if rodada == fase:
                if "A" in cortes:
                    janela.blit(botaoA,(101,476))
                if "B"in cortes:
                    janela.blit(botaoB,(646,477))
                if "C" in cortes:
                    janela.blit(botaoC,(106,582))
                if "D" in cortes:
                    janela.blit(botaoD,(642,577))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if x > 110 and x < 620 and y > 480 and y <570 and "A" not in cortes:
                            resposta = 'A'
                        elif x > 650 and x < 1160 and y > 480 and y < 570 and "B" not in cortes:
                            resposta  = 'B'
                        elif x > 109 and x < 613 and y > 586 and y < 670 and "C" not in cortes:
                            resposta  = 'C'
                        elif x > 650 and x <1160 and y > 585 and y <671 and "D" not in cortes:
                            resposta  ='D'
                        if x > 915 and x < 985 and y > 30 and y < 80:
                                if ajuda == 1 and fase != 6 and fase != 12 and fase != 18 and fase != 24:
                                    ajuda = 0
                                    rodada = fase
                                    if rodada == fase:
                                        while True:
                                            chave = ['A','B','C','D']
                                            cortes = random.choices(chave, k=2)
                                            if resp[fase] not in cortes and cortes[0] != cortes[1]:
                                               break
                        if x > 1012 and x < 1034 and y > 47 and y < 68 and fase == 6:
                            vidas += 1
                            acerto.play()
                            pontos("+1",verde,1135,36)
                            fase +=1
                        if rodada != fase:
                            cortes = []
            if resposta  == 'A' or resposta  == 'B' or resposta  == 'C' or resposta  == 'D':
                if resposta == resp[fase]:
                    acerto.play()
                    pontos("+1",verde,767,32)
                    if fase == 28:
                        jogar = False
                        fim = True
                        win = True
                    else:
                        fase += 1
                        resposta = False
                elif fase == 6 or fase == 12 or fase == 18 or fase == 24:
                    vidas+=1
                    fase += 1
                    resposta= False
                elif resp != resp[fase]:
                    resposta = False
                    if fase != 6 and fase != 12 and fase != 18 and fase != 24:
                        erro.play()
                        pontos("-1",vermelho,1135,36)
                        vidas -= 1
                    else:
                        erro.play()
                        pontos("Errou",vermelho,767,32)
                        fase += 1
                    if vidas < 1:
                        jogar = False
                        fim = True
                if fase == 22 or fase == 8:
                    ajuda = 1
            # saida
            if event.type == pygame.QUIT:
                sair = True
                pygame.quit()
        #Fim De Jogo
        while fim == True:
            if som == True:
                song()
            if win == True:
                ganhou()
                pygame.display.update()
            elif vidas == 0:
                perdeu()
                pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        if x > 110 and x < 620 and y > 360 and y < 565:
                            inicio = True
                            credit = False
                            dicas = False
                            start = True
                            resposta = False
                            jogar = False
                            rodada = False
                            fim = False
                            win = False
                            if som == True:
                                som = True
                            else:
                                som = False
                            # Variaveis
                            fase = 1
                            ajuda = 1
                            vidas = 2
                        elif x > 650 and x < 1160 and y > 360 and y < 565:
                            sair = True
                            pygame.quit()
                        elif x > 880 and x < 1065 and y > 220 and y < 410 and vidas == 0:
                            video(aula[fase])

                if event.type == pygame.QUIT:
                    sair = True
                    pygame.quit()
        #ABA DAS DICAS
        while dicas == True:
            if som == True:
                song()
            tela(tutorial[aba])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        #retorno
                        if x > 35 and x < 685 and y > 670 and y < 702:
                            aba -= 1
                        elif x >1165 and x <1240 and y > 670 and y < 702:
                            aba += 1
                        if aba ==3:
                            if x > 283 and x <480 and y > 570 and y < 625:
                                webbrowser.open('https://www.youtube.com/playlist?list=PLsutL2TqSEP-2wLH-5iybbeATcF9Hx1JG')
                            elif x >  540 and x <740 and y > 570 and y < 625:
                                webbrowser.open("https://www.youtube.com/playlist?list=PLsutL2TqSEP_grAls-piP0A5yMIYmXnq3")
                            elif x > 800 and x < 995 and y > 570 and y < 625:
                                    webbrowser.open('https://www.youtube.com/playlist?list=PLsutL2TqSEP_Drs46QKGeo8EIubak-TYj')
                        if aba == 0 or aba == 4:
                            inicio = True
                            dicas = False
                            aba = 1
                # saida
                if event.type == pygame.QUIT:
                    sair = True
                    pygame.quit()
        #ABA DOS CREDITOS
        while credit == True:
            if som == True:
                song()
            creditos()
            seta()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x = pygame.mouse.get_pos()[0]
                        y = pygame.mouse.get_pos()[1]
                        #retorno
                        if x > 1205 and x <1245 and y > 85 and y < 105:
                            inicio = True
                            credit = False
                            dicas = False
                        elif x > 355 and x < 425 and y > 582 and y < 635:
                            webbrowser.open('https://www.youtube.com/playlist?list=PLsutL2TqSEP_G0gjOJFUMtPWB2rg8L7Vf')
                            #saida
                if event.type == pygame.QUIT:
                        sair = True
                        pygame.quit()
jogo()

