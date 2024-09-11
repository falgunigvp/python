months={ 
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
dob=input("Enter DOB e.g DD/MM/YY :- ")
if len(dob)  == 8:
    if dob[3:5] in months.keys():
        print(months[dob[3:5]])
else:
    print("enter in valid formate")