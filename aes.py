# TARUN KUMAR SURYAVANSHI
# 2019163

# STRING TO BITS-STRING
def createbits(msg):
    print(msg)
    res = ''.join(format(ord(i), '08b') for i in msg)
    return res   

# GENERATE SUBNIB WITH S-BOX
def subnib(w):
    w = str(w)
    if w == "0000": return "1001"
    if w == "0001": return "0100"
    if w == "0010": return "1010"
    if w == "0011": return "1011"
    if w == "0100": return "1101"
    if w == "0101": return "0001"
    if w == "0110": return "1000"
    if w == "0111": return "0101"
    if w == "1000": return "0110"
    if w == "1001": return "0010"
    if w == "1010": return "0000"
    if w == "1011": return "0011"
    if w == "1100": return "1100"
    if w == "1101": return "1110"
    if w == "1110": return "1111"
    if w == "1111": return "0111"

# GENERATE SUBNIB WITH INVERSE S-BOX
def isubnib(w):
    w = str(w)
    if w == "0000": return "1010"
    if w == "0001": return "0101"
    if w == "0010": return "1001"
    if w == "0011": return "1011"
    if w == "0100": return "0001"
    if w == "0101": return "0111"
    if w == "0110": return "1000"
    if w == "0111": return "1111"
    if w == "1000": return "0110"
    if w == "1001": return "0000"
    if w == "1010": return "0010"
    if w == "1011": return "0011"
    if w == "1100": return "1100"
    if w == "1101": return "0100"
    if w == "1110": return "1101"
    if w == "1111": return "1110"    

# XOR OR THREE BITS STRING
def xor(s1,s2,s3):
    s = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s,s3))

# MIX COLUMN FUNCTION FOR ENCREAPTION
def mixcolumn(m):
    m = m[:4]+m[8:12]+m[4:8]+m[12:16]
    pt = ''
    pt = pt + str(int(m[0])^int(m[10])) + str(int(m[1])^int(m[4])^int(m[7])) + str(int(m[2])^int(m[4])^int(m[5])) +str(int(m[3])^int(m[5]))
    pt = pt + str(int(m[8])^int(m[14])) + str(int(m[9])^int(m[12])^int(m[15])) + str(int(m[10])^int(m[12])^int(m[13])) +str(int(m[11])^int(m[13]))
    pt = pt + str(int(m[2])^int(m[4])) + str(int(m[0])^int(m[3])^int(m[5])) + str(int(m[0])^int(m[1])^int(m[6])) +str(int(m[1])^int(m[7]))
    pt = pt + str(int(m[10])^int(m[12])) + str(int(m[8])^int(m[11])^int(m[13])) + str(int(m[8])^int(m[9])^int(m[14])) +str(int(m[9])^int(m[15]))
    pt = pt[:4]+pt[8:12]+pt[4:8]+pt[12:16]
    return pt

# MIX COLUMN FUNCTION FOR DECREAPTION
def imixcolumn(m):
    m = m[12:16]+m[4:8]+m[8:12]+m[0:4]
    pt = ''
    pt = pt + str(int(m[0])^int(m[10])) + str(int(m[1])^int(m[4])^int(m[7])) + str(int(m[2])^int(m[4])^int(m[5])) +str(int(m[3])^int(m[5]))
    pt = pt + str(int(m[8])^int(m[14])) + str(int(m[9])^int(m[12])^int(m[15])) + str(int(m[10])^int(m[12])^int(m[13])) +str(int(m[11])^int(m[13]))
    pt = pt + str(int(m[2])^int(m[4])) + str(int(m[0])^int(m[3])^int(m[5])) + str(int(m[0])^int(m[1])^int(m[6])) +str(int(m[1])^int(m[7]))
    pt = pt + str(int(m[10])^int(m[12])) + str(int(m[8])^int(m[11])^int(m[13])) + str(int(m[8])^int(m[9])^int(m[14])) +str(int(m[9])^int(m[15]))
    pt = pt[12:16]+pt[4:8]+pt[8:12]+pt[0:4]
    return pt    