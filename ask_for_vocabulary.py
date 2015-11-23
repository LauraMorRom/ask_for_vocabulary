#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#El fichero de texto de vocabulario que se le pasa tiene que tener esta estructura: palabra en valenciano+tabulador+palabra en castellano

import codecs

print "Benvingut al assistent que pregunta vocabulari."
filename = 'vocabulary.txt'

list_of_pairs = []
with codecs.open(filename, 'r', 'utf-8') as f:
    for line in f.readlines():
        pairs = line.split("\t")
	pairs = (pairs[0].strip(), pairs[1].strip())
        list_of_pairs.append(pairs)
print(list_of_pairs)

def choose_random_line(list):
	import random
	random_line=random.choice(list)
	return random_line
	
#pedir lengua en que desea que le pregunten
language=raw_input(u'En quina llengua vols que et pregunte? Escriu C per a castella i V per a valencia: ')
while language!="C" and language!="V":
	print u"Escriu un caracter valid, per favor: C o V"
	language=raw_input(u'En quina llengua vols que et pregunte? Escriu C per a castella i V per a valencia: ')

user_answer=""
while language=="C" and user_answer!=u"Adeu siau":
	print u"Quan vulgues aturar el programa, escriu 'Adeu siau'."
	random_line = choose_random_line(list_of_pairs)
	question=random_line[1]
	answer=random_line[0]
	user_answer=raw_input(u'Com es diu en valencia ' + question + u'? ')

	if user_answer==answer:
		print u"Resposta correcta!"
	else:
		if user_answer==u"Adeu siau":
			print u"Fins a la proxima!"
		else:
			for turn in range(1,4):
				if turn>=3:
					print u"La resposta correcta era: " + answer + u"."
				else:
					print u"Resposta incorrecta. Tens tres oportunitats per encertar"
					user_answer=raw_input(u'Com es diu en valencia ' + question + u'? ')
					if user_answer==answer:
						print u"Resposta correcta!"
						break
				turn=turn+1
		

#if valencia

while language==u"V" and user_answer!=u"Adeu siau":
	print u"Quan vulgues aturar el programa, escriu 'Adeu siau'."
	random_line = choose_random_line(list_of_pairs)
	question=random_line[0]
	answer=random_line[1]
	user_answer=raw_input(u'Com es diu en castella ' + question + u'? ')

	if user_answer==answer:
		print u"Resposta correcta!"
	else:
		if user_answer==u"Adeu siau":
			print u"Fins a la proxima!"
		else:
			for turn in range(1,4):
				if turn>=3:
					print u"La resposta correcta era: " + answer + u"."
				else:
					print u"Resposta incorrecta. Tens tres oportunitats per encertar"
					user_answer=raw_input(u'Com es diu en castella ' + question + u'? ')
					if user_answer==answer:
						print u"Resposta correcta!"
						break
				turn=turn+1

