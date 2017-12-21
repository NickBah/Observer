from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, message: str) -> None:
        pass

class Observable(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.observers = []     # инициализация списка наблюдателей

    def register(self, observer: Observer) -> None:
        self.observers.append(observer)

    def notify_observers(self, message: str) -> None:
        for observer in self.observers:
            observer.update(message)

class Engine(Observable):

    def add_news(self, news: str) -> None:
        self.notify_observers(news)

class Var(Observer):

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print('{} узнал следующее: {}'.format(self.name, message))

if __name__ == '__main__':
    engine = Engine()
    engine.register(Var('var_1'))
    engine.register(Var('var_2'))

    engine.add_news('Переменным пора изменить значение!')