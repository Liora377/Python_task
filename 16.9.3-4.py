class Client:
    def __init__(self, name, lastname, city, balance):
        self.name = name
        self.lastname = lastname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.lastname}. {self.city}. Баланс: {self.balance}'

    def OnlyName(self):
        return f'{self.name} {self.lastname}. {self.city}'

client_1 = Client('Иван','Петров', 'Москва', 50)
client_2 = Client('Анна', 'Смирнова', 'Люберцы', 100)
client_3 = Client('Екатерина', 'Липкина', 'Тверь', 67)

print(client_1)

clients = [client_1, client_2, client_3]
for person in clients:
   print(person.OnlyName())