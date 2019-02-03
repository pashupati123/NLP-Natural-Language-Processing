import os
import nltk
import speeling_check_module as spellcheck
import gramar_check_module as grammarcheck

print("enter the number of sentence")
n=raw_input()
n=int(n)
for i in range(0,n):
	print("enter the sentence")
	sen=raw_input()
	tokens=nltk.word_tokenize(sen)
	spellcheck.spell_check(tokens)
	grammarcheck.grammer_chek(sen)
    

