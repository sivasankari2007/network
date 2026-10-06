import socket

HOST = '127.0.0.1'
PORT = 5000

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17

def encrypt_message(message):
    encrypted = []

    for character in message:
        value = ord(character)
        encrypted_value = pow(value, e, n)
        encrypted.append(str(encrypted_value))

    return " ".join(encrypted)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("====================================")
print("       RSA CLIENT")
print("====================================")
print("Connected to server.")
print("Public Key :", (e, n))
print("------------------------------------")

while True:
    message = input("Enter message: ")

    encrypted_message = encrypt_message(message)

    print("Encrypted Data :", encrypted_message)

    client.send(encrypted_message.encode())

    if message.lower() == "exit":
        break

client.close()