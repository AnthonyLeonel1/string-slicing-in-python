# https://www.101computing.net/string-slicing-in-python/
# This program will run and test all cases at once.

examples =["07jFox_S", "09kJohnson_S","a16", "11rTaylor_S", "00pJones_T", "00jOliver_A"]

def test(username):
	errors, role = [], ""
	print("Results for %s:" % (username))

	firstName = username[3:username.find("_")]
	lastName = username[2].upper()
	year = username[:2]

	if len(username) < 6:
		errors.append("Username is less than 6 characters")
	if "_" not in username:
		errors.append("Username invalid missing _.")
	
	if username[-2:] == "_S":
		role = "Student"
	elif username[-2:] == "_T":
		role = "Teacher"
	elif username[-2:] == "_A":
		role = "Admin"


	if len(errors)==0:
		print("Details: \n- Name: %s. %s \n- Role: %s \n- Year: %s" % (lastName,firstName,role,year), end="\n\n")
	else:
		print("- Invalid Username, check below")
		for e in errors:
			print("\t- Error: " + e)
		print("\n")

for e in examples:
	test(e)
	