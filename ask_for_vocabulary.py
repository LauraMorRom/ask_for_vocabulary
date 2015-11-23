#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#El fichero de texto de vocabulario que se le pasa tiene que tener esta estructura: palabra en valenciano+tabulador+palabra en castellano

print "Benvingut al assistent que pregunta vocabulari."
f=file("vocabulary.txt", "r")
content=f.read().splitlines()

list_of_pairs=[]
for line in content:
	pairs=line.split("\t")
	list_of_pairs.append(pairs)

def choose_random_line(list):
	import random
	random_line=random.choice(list)
	return random_line
	
#pedir lengua en que desea que le pregunten
language=raw_input('En quina llengua vols que et pregunte? Escriu C per a castella i V per a valencia: ')
while language!="C" and language!="V":
	print "Escriu un caracter valid, per favor: C o V"
	language=raw_input('En quina llengua vols que et pregunte? Escriu C per a castella i V per a valencia: ')

user_answer=""
while language=="C" and user_answer!="Adeu siau":
	print "Quan vulgues aturar el programa, escriu 'Adeu siau'."
	random_line = choose_random_line(list_of_pairs)
	question=random_line[1]
	answer=random_line[0]
	user_answer=raw_input('Com es diu en valencia '+question+'? ')

	if user_answer==answer:
		print "Resposta correcta!"
	else:
		if user_answer=="Adeu siau":
			print "Fins a la proxima!"
		else:
			for turn in range(1,4):
				if turn>=3:
					print "La resposta correcta era: "+answer+"."
				else:
					print "Resposta incorrecta. Tens tres oportunitats per encertar"
					user_answer=raw_input('Com es diu en valencia '+question+'? ')
					if user_answer==answer:
						print "Resposta correcta!"
						break
				turn=turn+1
		

#if valencia

while language=="V" and user_answer!="Adeu siau":
	print "Quan vulgues aturar el programa, escriu 'Adeu siau'."
	random_line = choose_random_line(list_of_pairs)
	question=random_line[0]
	answer=random_line[1]
	user_answer=raw_input('Com es diu en castella '+question+'? ')

	if user_answer==answer:
		print "Resposta correcta!"
	else:
		if user_answer=="Adeu siau":
			print "Fins a la proxima!"
		else:
			for turn in range(1,4):
				if turn>=3:
					print "La resposta correcta era: "+answer+"."
				else:
					print "Resposta incorrecta. Tens tres oportunitats per encertar"
					user_answer=raw_input('Com es diu en castella '+question+'? ')
					if user_answer==answer:
						print "Resposta correcta!"
						break
				turn=turn+1
