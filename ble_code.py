i = 1.0
j = 7.0
verifica = False
vetor = [1.0 , 2.0 , 3.0]
texto = "Ola mundo"
nome = ""
print(str("O valor de texto eh: ") + str(texto))
print("Insira seu nome: ")
nome = input()
if nome == "Thaty" or nome == "Thatyana":
	print(str(nome) + str(", insira um novo valor para texto: "))
	
else:
	print("Insira um novo valor para texto: ")
	
texto = input()
for i in range(1,11,1):
	print(str(i) + str(str(": ") + str(texto)))
	
