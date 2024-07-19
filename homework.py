from multiprocessing import Pool


class WarehouseManager:

    data = {}

    def process_request(self, request):
        product, operation, amount = request
        if operation == 'receipt':
            if product not in WarehouseManager.data:
                WarehouseManager.data.update({product: amount})
            else:
                WarehouseManager.data[product] += amount
            print(f'На склад привезен "{product}" в размере {amount} единиц.')
        elif operation == 'shipment':
            if product in WarehouseManager.data:
                if amount > WarehouseManager.data[product]:
                    print('Недостаточно товара на складе!')
                else:
                    WarehouseManager.data[product] -= amount
                    print(f'Со склада отгружен "{product}" в размере {amount} единиц.')
            else:
                print('Такого товара на складе нет!')

    def run(self, requests):
        print(requests)
        amount_requests = len(requests)
        processes = []

        with Pool(processes=1) as pool:
            pool.map(self.process_request, requests)
        # for request in requests:
        #     self.process_request(request)
        #     processes.append(Process(target=self.process_request, args=(request,)))
        #
        # for process in processes:
        #     process.start()
        #     process.join()


if __name__ == '__main__':
    manager = WarehouseManager()

    requests = [
        ('potato', 'receipt', 10),
        ('bananas', 'receipt', 10),
        ('potato', 'shipment', 5)
    ]

    manager.run(requests)

    print(manager.data)