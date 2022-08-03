from write import write as csv

def record()->None:
    family = input("\nФамилия:  ")
    csv(field = family + ";",path = "phonebook",filename = "phonebook.csv")
    name = input("\nИмя: ")
    csv(field = name + ";",path = "phonebook",filename = "phonebook.csv")
    fathername = input("\nОтчество: ")
    csv(field = fathername + ";",path = "phonebook",filename = "phonebook.csv")
    phone = input("\nТелефон: ")
    csv(field = phone + ";",path = "phonebook",filename = "phonebook.csv")
    csv(field = "\n" + ";",path = "phonebook",filename = "phonebook.csv")