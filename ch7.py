import re
#re1
#---------------------------------------------------------------------
'''regex1 = r"([0-9]{2})[^0-9]([0-9]{3})"               
regex2 = r"([a-z])\d{3}([a-z])\d{4}"  
print re.search(regex1, 'a1b22c333d4444').groups()
print re.search(regex2, 'a1b22c333d4444').groups()'''

#re2
#--------------------------------------------------------------------

'''regex = r"[a-z]{1,3}\d+"
print re.search(regex, 'a123').group()
print re.search(regex, 'zb42a').group()'''

#re3
#---------------------------------------------------------------------

'''def validate(passwd):
	if len(passwd) < 6 or len(passwd) > 8:
		return "Invalid password."
	elif re.match(r"[0-9]+[a-z]+",passwd):
		return "Valid password."
	else:
		return "Invalid password."

if __name__ == "__main__":
	pwd = raw_input("Enter Password : ")
	print validate(pwd)'''

#re4
#---------------------------------------------------------------------

def validate(email):
	if re.match(r"[a-z]+\.?[0-9a-z]*@[a-z]+[\.(org|edu|com)]+",email):
		return "Valid email."
	else:
		return "Invalid email."

if __name__ == "__main__":
	mail = raw_input("Enter Email : ")
	print validate(mail)
