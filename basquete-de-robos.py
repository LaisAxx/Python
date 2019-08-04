#http://olimpiada.ic.unicamp.br/pratique/pj/2018/f1/basquete/resultado/#
#Lais Alves#

# criei uma variavel com nomeclatura snake_case, usada no Python#
distancia_str = input()
# os valores na função input são do tipo string então é necessario converter para o tipo inteiro com a função int() #
D = int(distancia_str)
#Condição que compara o valor digitado pelo usuario se D precisa se maior ou igual a zero e menor ou igual a 800 #
if(D>=0 and D<=800):
	print("1") #Se a condição for verdadeira então imprimi 1#
else:# se a condição for false então irá testar as outras condições# 
	if(D>800 and D<=1400): #Se a entrada for maior que 800 e menor ou igual a 1400 então irá imprimir 2#
		print("2")
	elif(D>1400 and D<=2000): # e se a entrada for maior que 1400 e menor ou igual a 2000 então irá imprimir o valor 3#
		print("3")
	else:
		print("Esse não é um valor válido")	 # se nenhuma das condições forem verdadeiras então iria imprimir uma mensagem de erro#