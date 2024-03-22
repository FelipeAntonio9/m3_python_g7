import sys
import time

print(sys.argv)  # ['dia7/bomba.py', '8']
i = (sys.argv[0])
i = (sys.argv[1])

i = sys.argv[1]

while i > 0:
    print(f"El valor de i {i}")
    time.sleep(1)  # tiempo de espera 1 segundo
    i -= 1  # decremento (restando 1)

print("BOOOOOOOOOOOMMM!!!")
