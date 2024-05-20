import re


with open("input.txt", "r") as file:
    
    ukuran_input_pertama = file.readline().rstrip().split()
    n = int(ukuran_input_pertama[0])
    m = int(ukuran_input_pertama[1])

    
    matriks = [file.readline().rstrip() for _ in range(n)]


hasil_dekode = ""
for i in range(m):
    for j in range(n):
        try:
            hasil_dekode += matriks[j][i]
        except IndexError:
            pass


pola = r'(?<=[\w])[^\w]+(?=[\w])'
cocokan = re.findall(pola, hasil_dekode)

for x in cocokan:
    hasil_dekode = hasil_dekode.replace(x, ' ', 1)

print(hasil_dekode)