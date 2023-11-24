class Conferense:
    def __init__(self, name: str = "", people_num: int = 0, price: float = 0.0, location: str = ""):
        self.__name = name
        self.__people_num = people_num
        self.__price = price
        self.__location = location
    
    def get_name(self):
        return self.__name

    def get_people_num(self):
        return self.__people_num

    def get_price(self):
        return self.__price

    def get_location(self):
        return self.__location

    def __str__(self):
        return f"Конференція: Назва - {self.__name}, Кількість людей - {self.__people_num}, Ціна - {self.__price} Грн, Місце проведення - {self.__location}"

    def __repr__(self):
        return f'Конференція({self.__name!r}, {self.__people_num!r}, {self.__price!r}, {self.__location!r})'

def main():
    conferense_1 = Conferense("Назва 1", 10, 100, "Кабінет №1")
    conferense_2 = Conferense("Назва 2", 40, 30, "Кабінет №2" )
    conferense_3 = Conferense("Назва 3", 70, 10, "Кабінет №3")

    print(conferense_1)
    print(conferense_2)
    print(conferense_3)

main()