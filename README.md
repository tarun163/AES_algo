# AES_algo

# this Web Socket App for communication one client with server, it will share 16bits of 2 word with 2 round of AES Variant.

first run the server.py then run client.py, go to the server.py file inter data then enter data on client.py

we have 3 .py files 
aes.py : containing functions for create bits, create SubNib for both encryption and decryption, xor of three bit string, mix colomn for both encryption and decryption.

# server.py : 
 - importing socket for socket functins
 - importing aes.py file for AES functions
 - creating socket listening port 1024 for same devies
 - enter prime number p, q then enter public key e between 1 and       phin and compute private key d. 
 - sending public key to client by receiving one msg
 - receiving data as ciphertext, encrypted_secret_key,          client_signature, client_public_key.
 - decrepting secret key
 - convert secret key to bit string
 - create 3 keys 
 - add round 2 key
 - Shift Row round 2
 - Nibble Substitution round 2
 - Add Round 1 Key
 - Mix Columns round 1
 - Shift Row round 1
 - Nibble Substitution round 1
 - add round 0 key
 - converting binary msg to word
 - creating digest of hash msg
 - create client signature from hash code and varifie it

# client.py : 
 - importing socket for socket functins
 - importing aes.py file for AES functions
 - creating socket listening port 1024 for same devies
 - enter prime number p, q then enter public key e between 1 and       phin and compute private key d.
 - sending some msg to server for server public key
 - enter 16bits(2 words) massege for server
 - generating signature of massege
 - enter secret key as 16bits number
 - encrypting secret key
 - creating bits of msg and key
 - create 3 keys 
 - add round 0 key
 - Nibble Substitution round 1
 - Shift Row round 1
 - Mix Columns round 1
 - add round 1 key
 - Nibble Substitution round 2
 - Shift Row round 2
 - add round 2 key
 - sending ciphertext, encrypted_secret_key, client_signature,    client_public_key as a string.

Some problems during inverse mix column so may be it will provid wrong data.
