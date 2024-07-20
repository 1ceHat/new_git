from multiprocessing import Process, Pool, Manager


class WarehouseManager:

    def __init__(self):
        self.data = Manager().dict()

    def process_request(self, request):
        product, operation, amount = request
        if operation == 'receipt':
            if product not in self.data:
                self.data.update({product: amount})
            else:
                self.data[product] += amount
            print(f'На склад привезен "{product}" в размере {amount} единиц.')
        elif operation == 'shipment':
            if product in self.data:
                if amount > self.data[product]:
                    print('Недостаточно товара на складе!')
                else:
                    self.data[product] -= amount
                    print(f'Со склада отгружен "{product}" в размере {amount} единиц.')
            else:
                print('Такого товара на складе нет!')

    def run(self, requests):
        amount_requests = len(requests)
        processes = []
        for request in requests:
            processes.append(Process(target=self.process_request, args=(request,)))

        for process in processes:
            process.start()
            process.join()


if __name__ == '__main__':
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)

    print(manager.data)