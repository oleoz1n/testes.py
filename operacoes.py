def pergunta():
	print("Quer reiniciar?")
	resp = input('''[s]Se sim
[n]Se não
:''')
	if(resp == 's'):
		operacoes()
	elif(resp == 'n'):
		return
	else:
		return pergunta()
def operacoes():
	esc1 = input("Primeiro número: ")
	esc2 = input("Segundo número: ")
	print('''--------------------------------
	Qual operação desejada?
	+ = adição
	- = subtração
	* = multiplicação
	/ = divisão
	** = potência
-------------------------------------
''')
	ope = input("\nEscolha: ")
	if(ope == '+'):
		result = int(esc1) + int(esc2)
	elif(ope == '-'):
		result = int(esc1) - int(esc2)
	elif(ope == '*'):
		result = int(esc1) * int(esc2)
	elif(ope == '/'):
		result = int(esc1) / int(esc2)
	elif(ope == '**'):
		result = int(esc1) ** int(esc2)
	else:
		print('caractere inválido')
		return operacoes()
	print('\n O resultado é',result,'\n')
	pergunta()
operacoes()