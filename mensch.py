#!/usr/bin/python3
import random

class Mensch(object):
	''' der sstandard mitarbeiteter '''
	nummer = 0 #Klassenattribut gehoert der gesamten Menschheit
	## Listen als Klassenattribute
	
	def __init__(self):
		''' konstruktoirorr oder so'''
		self.geschlecht=random.choice(['m','w'])
		self.haarfarbe=random.choice(['blau','blond','schwarz','weiss','braun','rot'])
		self.groesse=random.randint(150,210)
		self.gewicht=random.randint(50,150)
		Mensch.nummer+=1
		self.nummer=Mensch.nummer

	def schrumpf(self, factor=0.9):
		''' schrumpf mit fuctor'''
		self.groesse *= factor
		self.gewicht *= factor
	def wachsen(self, factor=1.1):
		''' wachsen wir die ski '''
		self.groesse *= factor
		self.gewicht *= factor

class Menschheit(object):
    menschen={}



while True:

    menschling=Mensch()
    #print(menschling.nummer)
    Menschheit.menschen[menschling.nummer]=menschling

    print(menschling.__dict__)

    eingabe=input()
    if eingabe=="q":
        break
    


    
    