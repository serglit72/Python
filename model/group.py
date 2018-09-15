from sys import maxsize

class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

#эта функция выдает значение данных в нормальном виде
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

#это сравнение логическое двух значений по смыслу
    def __eq__(self, other):
        return self.id is None or other.id is None or self.id == other.id and self.name == other.name


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

