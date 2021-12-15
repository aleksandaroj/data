class Klasa:
    @classmethod
    def class_method(cls, param):
        print('1 ' + param)

    @staticmethod
    def static_method(param):
        print('2 ' + param)


obj = Klasa()
obj.class_method('Hi')
Klasa.static_method('Yo')

Klasa.class_method('Hi')
obj.static_method('Yo')
