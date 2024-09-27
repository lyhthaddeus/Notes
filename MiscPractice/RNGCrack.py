from randcrack import RandCrack
import random
from pwn import *

def crack():
    rc = RandCrack()

    server = remote('cs2107-challs.nusgreyhats.org', 5051)

    for i in range(624):
        random_guess = random.getrandbits(32)
        question = server.recvline()
        server.sendline(str(random_guess).encode())
        response = server.recvline().decode().strip()
        number_received = response.split(": ")[1]
        rc.submit(number_received)

    predicted = rc.predict_randrange(0, 4294967295)
    print(f"Predicted next number: {predicted}")

    question_final = server.recvline()
    server.sendline(str(predicted).encode())
    final_response = server.recvline().decode().strip()
    print(f"Final response from server: {final_response}")

    server.close()

if __name__ == '__main__':
    crack()
