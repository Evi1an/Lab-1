# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Kitty:
    def __init__(self, age: int, type: str):
        """
        Создание и подготовка объекта "Kitty"

        :param age: возраст кота
        :param type: порода кота

        Пример:
        >>> tomas = Kitty(3, "Британец") #инициализация экземпляра класса
        """
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        if not isinstance(age, int):
            raise TypeError("Нужно ввести целое число")

        self.age = age
        self.type = type

    def eat(self, food_product: str):
        """
        Метод описывает процесс питания.

        :param food_product: что кушает котик
        :return: описание процесса

        Пример:
        >>> kotik_tomas = Kitty(2, "Шотландец")
        >>> kotik_tomas.eat("рыбку")
        'Котик съел рыбку.'
        """

        return "Котик съел " + food_product + "."

    def sleep(self, hour: int):
        """
        Метод описывает сон.

        :param hour: сколько часов спал кот
        :return: описание процесса

        Пример:
        >>> kotik_tomas = Kitty(2, "Шотландец")
        >>> kotik_tomas.sleep(4)
        'Котик спит 4 часа'
        """

        return "Котик спит " + str(hour) + " часа"

class Printer:
    def __init__(self, model: str, year_of_issue: int):
        """
        Создание и подготовка объекта "Printer"
        :param model: модель принтера
        :param year_of_issue: год выпуска

        Пример:
        >>> printer = Printer("EPSON L382", 2010) #инициализация экземпляра класса
        """
        if year_of_issue < 1953 or year_of_issue > 2025:
            raise ValueError("Год выпуска должен наодиться в диапазоне 1953-2025")

        self.model = model
        self.year_of_issue = year_of_issue

    def turn_on(self):
        """
        Метод описывает процесс включения принтера.

        :return: описание включения

        Пример:
        >>> printer = Printer("EPSON L382", 2010)
        >>> printer.turn_on()
        'Принтер EPSON L382 включен'
        """

        return "Принтер " + self.model + " включен"

    def turn_of(self):
        """
        Метод описывает процесс выключения принтера.

        :return: описание выключения

        Пример:
        >>> printer = Printer("EPSON L382", 2010)
        >>> printer.turn_of()
        'Принтер EPSON L382 выключен'
        """

        return "Принтер " + self.model + " выключен"

class Sobriety:
    def __init__(self, name: str, as_much_as_needed: int, how_much_did_you_drink: int):
        """
         Создание и подготовка объекта "Sobriety"

        :param name: имя человека
        :param as_much_as_needed: сколько надо выпить, чтобы стать не трезвым
        :param how_much_did_you_drink: сколько человек выпил

        Пример:
        >>> tom = Sobriety("Tom", 10, 5) #инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str.")
        if not isinstance(as_much_as_needed, int):
            raise TypeError("Сколько надо должно быть типа int")
        if not isinstance(how_much_did_you_drink, int):
            raise TypeError("Сколько надо выпить должно быть типа int")

        self.name = name
        self.as_much_as_needed = as_much_as_needed
        self.how_much_did_you_drink = how_much_did_you_drink

    def state(self):
        """
        Метод описывает состояние человека. (Примечание: чрезмерное употребление алкоголя вредит вашему здоровью)

        :return: показывает что делать дальше

        Пример:
        >>> tom = Sobriety("Том", 10, 12)
        >>> tom.state()
        'Том, идите спать, Вы пьяны!'
        """
        if self.how_much_did_you_drink >= self.as_much_as_needed:
            return self.name + ", идите спать, Вы пьяны!"
        else:
            return self.name + ", дискотека продолжается!"

    def additive (self, aperitif: int):
        """
        Метод показывает стоит веселиться дальше или уже хватит и нужно идти домой.

        :param aperitif: показывает сколько ещё выпито
        :return: показывает стоит ли продолжать веселиться

        Пример:
        >>> tom = Sobriety("Том", 10, 2)
        >>> tom.additive(3)
        'Том, можно продолжать веселиться ;)'
        """

        if self.how_much_did_you_drink + aperitif >= self.as_much_as_needed:
            return self.name + ", уже хватит, иди домой!"
        else:
            return self.name + ", можно продолжать веселиться ;)"


if __name__ == "__task1__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
