import inspect
import pprint


class Newclass:
    def __init__(self, value, count):
        self.value = value
        self.count = count

    def cost(self):
        return self.value * self.count


def introspection_info(obj):
    dict_ = {}
    try:
        dict_['Имя объекта'] = obj.__name__
    except AttributeError:
        dict_['Имя объекта'] = 'Нет имени'
    dict_['Тип объекта'] = type(obj)
    try:
        dict_['Атрибуты объекта'] = [method for method in dir(obj) if not callable(getattr(obj, method))]
    except AttributeError:
        dict_['Атрибуты объекта'] = 'Нет атрибутов'
    dict_['Методы объекта'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    dict_['Модуль'] = obj.__class__.__module__
    dict_['Наличие атрибута cost'] = hasattr(obj, 'cost')
    dict_['Наличие атрибута count'] = hasattr(obj, 'count')
    return dict_


apple = Newclass(100, 2)
pprint.pprint(introspection_info(apple))
# pprint.pprint(introspection_info(Newclass))

# a = 27
# pprint.pprint(introspection_info(a))


