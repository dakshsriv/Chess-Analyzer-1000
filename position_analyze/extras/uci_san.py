def uci_san(uci, fen):
    fensplit1 = fen.split()
    fensplitmain = fensplit1[0].split("/")
    fensplit = fensplitmain + (fensplit1[1:])
    procfen = list()
    for i in range(0, 7):
        row = fensplit[i]
        frow = str()
        for z in row:
            if z.isalpha():
                frow = frow + z
            else:
                frow = frow + (int(z) * "0")
        procfen.append(frow)
    procfen.extend(fensplit[8:])
    sq1 = uci[:2]
    sq2 = uci[2:]
    alphalist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    sq1c = [alphalist.index(sq1[1]), int(sq1[1])-1]
    sq2c = [alphalist.index(sq2[1]), int(sq2[1])-1]
    
