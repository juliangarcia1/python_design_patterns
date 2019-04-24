

class Subject(object):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except:
            pass
    
    def notify(self, modifier=None):
        for observer in self._observers:
            if observer != modifier:
                observer.update(self)

class Core(Subject):
    def __init__(self, name=''):
        Subject.__init__(self)
        self._name = name
        self._temp= 0
    
    @property
    def temp(self):
        return self._temp

    @temp.setter 
    def temp(self, temp):
        self._temp = temp
        self.notify(self)

class TempViewer1:
    def update(self, subject):
        print('{}: {} {}'.format(self.__class__.__name__, subject._name, subject._temp))

class TempViewer2:
    def update(self, subject):
        print('{}: {} {}'.format(self.__class__.__name__, subject._name, subject._temp))

c1 = Core('Core 1')
c2 = Core('Core 2')

v1 =  TempViewer1()
v2 =  TempViewer2()

c1.attach(v1)
c1.attach(v2)

# c1.new_message('Loking for roomie')
# c2.new_message('Bed for sale')

c1.temp = 100
c1.temp = 55
