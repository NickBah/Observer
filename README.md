Наблюдатель (англ. Observer) — поведенческий шаблон проектирования. Также известен как «подчинённые» (Dependents). Реализует у класса механизм, который позволяет объекту этого класса получать оповещения об изменении состояния других объектов, и тем самым наблюдать за ними.

Определяет зависимость типа «один ко многим» между объектами таким образом, что при изменении состояния одного объекта все зависящие от него оповещаются об этом событии.

Шаблон «наблюдатель» применяется в тех случаях, когда система обладает следующими свойствами:

 существует, как минимум, один объект, рассылающий сообщения;
 имеется не менее одного получателя сообщений, причём их количество и состав могут изменяться во время работы приложения;
 нет надобности очень сильно связывать взаимодействующие объекты, что полезно для повторного использования.

Данный шаблон часто применяют в ситуациях, в которых отправителя сообщений не интересует, что делают получатели с предоставленной им информацией.
