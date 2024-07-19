import queue
from time import sleep
from threading import Thread


class Table:

    def __init__(self, number: int, is_busy: bool = False):
        self.number = number
        self.is_busy = is_busy


class Cafe:

    def __init__(self, tables: list):
        self.__queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        self.__queue.maxsize = 20
        for i in range(1, self.__queue.maxsize+1):
            print(f'Посетитель номер {i} прибыл.')
            self.serve_customer(Customer(i))
            sleep(1)

        while not self.__queue.empty():
            sleep(10)
            self.serve_customer(self.__queue.get())


    def serve_customer(self, customer):
        free_table = 0
        for table in self.tables:
            if not table.is_busy:
                free_table = table.number
                break

        if not free_table:
            print(f'⌛Посетитель {customer.number} ожидает свободного столика')
            self.__queue.put(customer)
        else:
            if self.__queue.empty():
                customer.cafe, customer.table = self, self.tables[free_table-1]
                customer.start()
            else:
                print(f'⌛Посетитель {customer.number} ожидает свободного столика\n')
                change_customer = self.__queue.get()
                self.__queue.put(customer)
                change_customer.cafe, change_customer.table = self, self.tables[free_table - 1]
                change_customer.start()


class Customer(Thread):

    def __init__(self, number, cafe=None, table=None):
        super().__init__()
        self.number = number
        self.table = table
        self.cafe = cafe


    def run(self):
        print(f"✅✅Посетитель {self.number} сел за стол {self.table.number}")
        self.cafe.tables[self.table.number-1].is_busy = True
        sleep(5)
        self.cafe.tables[self.table.number - 1].is_busy = False
        print(f'Посетитель {self.number} покушал и ушёл')


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

customer_arrival_thread.join()
