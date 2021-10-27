# TARUN KUMAR SURYAVANSHI
# 2019163
import socket
from aes import *

#CREATING CONNECTION FOR SAME DEVICE
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#CONNECTING WITH PORT NO 1024
s.connect((socket.gethostname(), 1024))

# ENTER P,Q,E VALUE AS SERVER FIRST
# public-private key generation
p = int(input("enter the value of p :"))
q = int(input("enter the value of q :"))
n = p * q
phin = (p-1)*(q-1)
e = int(input("enter the value of e (1 < e <= {} ) :".format(phin)))
d = pow(e, -1, phin)
server_public_key = 0

# requesting for server public key
msg = input(str("request for server public key:"))
s.send(bytes(msg, "utf-8"))
msg = s.recv(1024)
msg = msg.decode("utf-8")
print("from server public key is: ", msg)
server_public_key = int(msg)

# for msg hash digest 
message = input(("enter message to server :"))
msg_hash = hash(message)

#generating client signature
client_signature = pow(msg_hash, d, n)
varification = pow(client_signature, e, n)
print('client signature is :', client_signature)

# encrypeted secret key generation
secret_key = int(input(("enter secret key as number: ")))
encrypted_secret_key = pow(secret_key, server_public_key, n)
print("encrypetd secret key is :", encrypted_secret_key)

# AES Variant for creating ciphertext
# creating bits of msg and key
msg = createbits(message)
print('message is in binary :', msg)
key = createbits(str(secret_key))
print("key is in binary", key)

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

   #Encryption
   # add round 0 key
plaintext = msg
plaintext = xor(plaintext, key1, '0000000000000000') 
print('reound 0 key', plaintext)   
   #round 1
   # Nibble Substitution round 1
plaintext = subnib(plaintext[:4])+subnib(plaintext[4:8])+subnib(plaintext[8:12])+subnib(plaintext[12:16])
print('round 1 nibble sub ', plaintext)

   # Shift Row round 1
plaintext = (plaintext[:4])+(plaintext[12:16])+(plaintext[8:12])+(plaintext[4:8])
print('ound 1 shift row ',plaintext) 

   # Mix Columns round 1
plaintext = mixcolumn(plaintext)
print('round 1 mix column ', plaintext)

    # add round 1 key
plaintext = xor(plaintext, key2, '0000000000000000') 
print('add round 1 key ', plaintext)

    #final round
    # Nibble Substitution round 2
plaintext = subnib(plaintext[:4])+subnib(plaintext[4:8])+subnib(plaintext[8:12])+subnib(plaintext[12:16])
print('round 2 nibble sub ', plaintext)

    # Shift Row round 2
plaintext = (plaintext[:4])+(plaintext[12:16])+(plaintext[8:12])+(plaintext[4:8])
print('ound 2 shift row ',plaintext) 

    # add round 2 key
plaintext = xor(plaintext, key3, '0000000000000000') 
print('add round 2 key ', plaintext)

ciphertext = plaintext
print('cipher text :', ciphertext)
print('digest :', msg_hash)
print('digital signature :', client_signature)
tuple_to_send = str(ciphertext)+'$'+str(encrypted_secret_key)+'$'+str(client_signature)+'$'+str(e)
s.send((tuple_to_send).encode())

