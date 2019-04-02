import nltk
from nltk.corpus import stopwords
from nltk.stem import *

class Textes(object):
	def __init__(self,text_init, liste):
		self.text_init = text_init #string
		self.liste = liste
		self.liste_token = liste_token
		self.liste_removed = liste_removed
		self.liste_finale = liste_finale
	
	def lecture(self.texte_init):
		Fichier = open(text_init,"r")
		self.liste = Fichier.split()
		Fichier.close()
		for word in liste:
			word.lower()
		return self.liste

	def tokenization(self):
		list_carac=[".", ",", ";", ":", "!", "?", "(", ")", "[", "]", "{", "}", "+", "=", "/", "\\", "\"", "\'"]
		for word in self.liste:
			for car in list_carac:
				word.strip(car)
			liste_token.append(word)
		return self.liste_token

	def remove_stop_words(self):
		StopWords = set(stopwords.words('english'))
		for word in self.liste_token:
			if word not in StopWords:
				liste_removed.append(word)
		return self.liste_removed
	
	def lemmatization(self):
		for word in self.liste_removed:
			self.liste_finale.append(stemmer.stem(word))
		return liste_finale
