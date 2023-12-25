
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
	user = input("Enter date: ").capitalize()

	if user.count("/") == 2:
		try:
			m, d, y = user.split("/")
			if int(m) > 12 or int(d) > 31:
				continue
			newdate = f"{int(y):04}-{int(m):02}-{int(d):02}"
			break
		except:
			continue
	elif user.count(",") == 1:
		try:

			md, y = user.split(",")
			m, d = md.split()
			if int(d) > 31:
				continue
			m = months.index(m) + 1
			newdate = f"{int(y):04}-{m:02}-{int(d):02}"
			break
		except:
			continue
	else:
		continue


print(newdate)
