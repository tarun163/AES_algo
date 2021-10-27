# TARUN KUMAR SURYAVANSHI
# 2019163
import socket
from aes import *

#CREATING CONNECTION FOR SAME DEVICE
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#CONNECTING WITH PORT NO 1024
s.bind((socket.gethostname(), 1024))
s.listen(1)
# reveiving data
clt, adr = s.accept()
print(f'connect {adr}')

# public-private key generation
p = int(input("enter the value of p :"))
q = int(input("enter the value of q :"))
n = p * q
phin = (p-1)*(q-1)
e = int(input("enter the value of e (1 < e <= {phin} ) :"))
d = pow(e, -1, phin)

#send public key to the client
msg = clt.recv(1024)
msg = msg.decode()
print(msg)
reply = str(e)
clt.send(reply.encode())

#receving data from server
data = clt.recv(50000)
data = data.decode()
myArray = data.split('$')
print(myArray)
ciphertext = myArray[0]
encrypted_secret_key = int(myArray[1])
client_signature = int(myArray[2])
client_public_key = int(myArray[3])

# decrepting secret key
secret_key = pow(encrypted_secret_key, d, n)
print('secret key :', secret_key)

    # decreption 
key = createbits(str(secret_key))
print("key is in bits", key)

    #key generation
w0 = key[:8]
w1 = key[8:]    
w2 = xor((w0), '10000000', subnib((w1[4:]))+subnib((w1[:4])))
w3 = xor(w2, (w1), '00000000')
w4 = xor(w2, '00110000', subnib((w3[4:]))+subnib((w3[:4])))
w5 = xor(w4, w3, '00000000')

    #sub-keys are
key1 = key
key2 = w2+w3
key3 = w4+w5
print('keys :', key1, key2, key3)

    # add round 2 key
ciphertext = xor(ciphertext, key3, '0000000000000000') 
print('round key 2 add ropund', ciphertext) 

    # Shift Row round 2
ciphertext = (ciphertext[:4])+(ciphertext[12:16])+(ciphertext[8:12])+(ciphertext[4:8])
print('round 2 shift row', ciphertext)   

    # Nibble Substitution round 2
ciphertext = isubnib(ciphertext[:4])+isubnib(ciphertext[4:8])+isubnib(ciphertext[8:12])+isubnib(ciphertext[12:16])
print('round 2 nibble sub', ciphertext)

    # Add Round 1 Key
ciphertext = xor(ciphertext, key2, '0000000000000000') 
print('add round 1 key', ciphertext)   

    # Mix Columns round 1
ciphertext = imixcolumn(ciphertext)
print('round 1 mix column ', ciphertext)

    # Shift Row round 1
ciphertext = (ciphertext[:4])+(ciphertext[12:16])+(ciphertext[8:12])+(ciphertext[4:8])
print('round 1 shift row', ciphertext)

    # Nibble Substitution round 1
ciphertext = isubnib(ciphertext[:4])+isubnib(ciphertext[4:8])+isubnib(ciphertext[8:12])+isubnib(ciphertext[12:16])
print('round 1 nibble sub ', ciphertext)

    # add round 0 key 
plaintext = xor(ciphertext, key1, '0000000000000000') 

# plaintext = createmsg(plaintext)
print('message is binary', plaintext) 
p1 = int(plaintext[:8], 2)
p1 = chr(97 + p1%26)
p2 = int(plaintext[8:], 2)
p2 = chr(97 + p2%26)
print('message is decrypted', p1, p2) 
msg = p1+p2

# for msg hash digest and client signature
msg_hash = hash(msg)
print('msg digest', msg_hash) 
client_signature = pow(msg_hash, client_public_key, n)
print('client signature :', client_signature)

