import socket
import math

HOST = '127.0.0.1'
PORT = 5000

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d
    return None

d = mod_inverse(e, phi)

def decrypt_message(encrypted_message):
    encrypted_numbers = encrypted_message.split()
    decrypted = ""

    for number in encrypted_numbers:
        value = pow(int(number), d, n)
        decrypted += chr(value)

    return decrypted

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("====================================")
print("       RSA SERVER")
print("====================================")
print("Server started...")
print("Waiting for client connection...")

conn, address = server.accept()

print("Client connected:", address)
print("Public Key  :", (e, n))
print("Private Key :", (d, n))
print("------------------------------------")

while True:
    encrypted_message = conn.recv(4096).decode()

    if not encrypted_message:
        break

    if encrypted_message == "exit":
        print("Client disconnected.")
        break

    print("Encrypted Data :", encrypted_message)

    decrypted_message = decrypt_message(encrypted_message)

    print("Decrypted Data :", decrypted_message)
    print("------------------------------------")

    if decrypted_message.lower() == "exit":
        break

conn.close()
server.close()