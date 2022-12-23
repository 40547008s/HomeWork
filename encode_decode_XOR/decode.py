with open('enc.png','rb') as f:
    lines = f.readlines()
    key = [ord(i) for i in "5pyxf4m1ly"]
    cnt = 0
    res = []
    for line in lines:
        for i in line:
            #print(type(i),i)
            res.append(i^key[cnt%len(key)])
            cnt += 1
    res = bytearray(res)
    with open("dec.png","wb") as binary_file:
        binary_file.write(res)