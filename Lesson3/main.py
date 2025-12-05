class Passport:

    def __init__(self,name,surname,birthdate):

        self.name = name
        self.surname = surname
        self.birthdate = birthdate


    def show(self):
        print(
            '------------Pasport------------\n'
            f'Name: {self.name}\nSurname: {self.surname}\n'
            f'Birthdate: {self.birthdate}\n'
            '-------------------------------'
        )


class ForeignPassport(Passport):
    def __init__(self, name, surname, birthdate,foreign_number):
        super().__init__(name, surname, birthdate)
        self.foreign_number = foreign_number
        self.visas = []

    def add_visa(self,visa):
        self.visas.append(visa)

    def del_visa(self,visa):
        if(visa in self.visas):
            self.visas.remove(visa)

    def show(self):
        visas_list = ", ".join(self.visas) if self.visas else "No visas"
        print (
            f"------ Foreign Passport ------\n"
            f"Name: {self.name}\n"
            f"Surname: {self.surname}\n"
            f"Birthdate: {self.birthdate}\n"
            f"Foreign passport number: {self.foreign_number}\n"
            f"Visas: {visas_list}\n"
            '-------------------------------'
        )


man1 = Passport("Maksum","Rubel","24.04.2009")
man1.show()

print()
print()

man2 = ForeignPassport("Maksum", "Rubel", "24.04.2009", "FP001122")
man2.add_visa("USA")
man2.add_visa("Poland")
man2.show()




class Tempclass():
    conversion_count = 0
    @staticmethod
    def fromСtoF(cel):
        Tempclass.conversion_count += 1
        return cel * 1.8 + 32
    @staticmethod
    def fromFtoC(fel):
        Tempclass.conversion_count += 1
        return (fel - 32) / 1.8
    @staticmethod
    def get_count():
        return Tempclass.conversion_count
    
print("----------------Temp------------------")
print(Tempclass.fromFtoC(32))
print(Tempclass.fromСtoF(0))
print(Tempclass.get_count())
print("--------------------------------------")

