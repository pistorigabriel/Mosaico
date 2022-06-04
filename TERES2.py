t = 0
mainframe = []

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
    except ValueError or EOFError:
        break
#Printando o resultado
print("1")
print(f"({XseM},{YseM}), ({XidM},{YidM})")


