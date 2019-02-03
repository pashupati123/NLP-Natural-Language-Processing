import enchant
import nltk 

def spell_check(words):
	check_spelling=enchant.Dict("en_US")
	for word in words:
		if check_spelling.check(word) is False:
			suggest_spell=check_spelling.suggest(word)
			print(word,"spelling Error","suggestion->",suggest_spell)
			


