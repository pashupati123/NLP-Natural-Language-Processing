import os
import grammar_check

tool=grammar_check.LanguageTool('en-GB')

def grammer_chek(sen):
	matches=tool.check(sen)
	if matches:
		print(sen,"Syntax_error")
		print("grammatic suggestion")
		print(grammar_check.correct(sen, matches))
	else:
		print(sen,"No_syntax_error")

