#Setando as variáveis
t = 0
XseM = 0
YseM = 0
XidM = 0
YidM = 0

#Iniciando o loop de imagens, contendo no máximo 100 imagens
while t<100:
    try:
        #Inserindo as coordenadas de cada nova imagem
        Xse, Yse, Xid, Yid = map(int,input().split())
        #Listando a primeira imagem
        if t == 0:
            XseM = Xse
            YseM = Yse
            XidM = Xid
            YidM = Yid
            t +=1
        #Comparando as demais imagens com o mosaico vigente
        else:
            if Xse<XseM:
                XseM = Xse
            if Yse>YseM:
                YseM = Yse
            if Xid>XidM:
                XidM = Xid
            if Yid<YidM:
                YidM = Yid
            t +=1
    #Exceções
    except ValueError:
        pass
    except EOFError:
        break
#Printando o resultado
print("1")
print(f"({XseM},{YseM}), ({XidM},{YidM})")



