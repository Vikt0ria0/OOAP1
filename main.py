# # # # # import tkinter as tk
# # # # #
# # # # # # Поставщики с заданными ценами на продукцию
# # # # # suppliers = {
# # # # #     "Поставщик 1": {"мука": 10, "яйца": 20, "сахар": 15},
# # # # #     "Поставщик 2": {"мука": 12, "яйца": 40},
# # # # #     "Поставщик 3": {"мука": 8, "сахар": 20}
# # # # # }
# # # # #
# # # # # # Интерфейс для ввода суточной потребности
# # # # # class ConfectionerySystemGUI:
# # # # #     def __init__(self, master):
# # # # #         self.master = master
# # # # #         self.master.title("Confectionery Supply System")
# # # # #
# # # # #         self.label = tk.Label(master, text="Enter daily demand for each product:")
# # # # #         self.label.pack()
# # # # #
# # # # #         self.flour_demand_label = tk.Label(master, text="Daily flour demand:")
# # # # #         self.flour_demand_entry = tk.Entry(master)
# # # # #         self.flour_demand_label.pack()
# # # # #         self.flour_demand_entry.pack()
# # # # #
# # # # #         self.eggs_demand_label = tk.Label(master, text="Daily eggs demand:")
# # # # #         self.eggs_demand_entry = tk.Entry(master)
# # # # #         self.eggs_demand_label.pack()
# # # # #         self.eggs_demand_entry.pack()
# # # # #
# # # # #         self.sugar_demand_label = tk.Label(master, text="Daily sugar demand:")
# # # # #         self.sugar_demand_entry = tk.Entry(master)
# # # # #         self.sugar_demand_label.pack()
# # # # #         self.sugar_demand_entry.pack()
# # # # #
# # # # #         # Кнопка для расчета оптимального плана
# # # # #         self.calculate_button = tk.Button(master, text="Calculate Plan", command=self.calculate_optimal_plan)
# # # # #         self.calculate_button.pack()
# # # # #
# # # # #     def calculate_optimal_plan(self):
# # # # #         # Получение введенных данных
# # # # #         flour_demand = int(self.flour_demand_entry.get())
# # # # #         eggs_demand = int(self.eggs_demand_entry.get())
# # # # #         sugar_demand = int(self.sugar_demand_entry.get())
# # # # #
# # # # #         # Расчет оптимального плана поставок
# # # # #         total_costs = []
# # # # #         for supplier, prices in suppliers.items():
# # # # #             total_cost = prices['flour_price'] * flour_demand + prices['eggs_price'] * eggs_demand + prices['sugar_price'] * sugar_demand
# # # # #             total_costs.append((supplier, total_cost))
# # # # #
# # # # #         # Нахождение минимальной стоимости и поставщика с оптимальным планом
# # # # #         min_cost_supplier, min_cost = min(total_costs, key=lambda x: x[1])
# # # # #
# # # # #         # Вывод результата
# # # # #         result_label = tk.Label(self.master, text=f"Optimal supplier: {min_cost_supplier}, Total cost: {min_cost}")
# # # # #         result_label.pack()
# # # # #
# # # # # # Создание графического интерфейса
# # # # # root = tk.Tk()
# # # # # app = ConfectionerySystemGUI(root)
# # # # # root.mainloop()
# # import tkinter as tk
# #
# # # Абстрактная фабрика поставщиков
# # class SupplierFactory:
# #     def get_flour_price(self):
# #         pass
# #
# #     def get_eggs_price(self):
# #         pass
# #
# #     def get_sugar_price(self):
# #         pass
# #
# # # Конкретные фабрики для каждого поставщика
# # class Supplier1Factory(SupplierFactory):
# #     def get_flour_price(self):
# #         return 60
# #
# #     def get_eggs_price(self):
# #         return 20
# #
# #     def get_sugar_price(self):
# #         return 70
# #
# # class Supplier2Factory(SupplierFactory):
# #     def get_flour_price(self):
# #         return 62
# #
# #     def get_eggs_price(self):
# #         return 10
# #
# #     def get_sugar_price(self):
# #         return None
# #
# # class Supplier3Factory(SupplierFactory):
# #     def get_flour_price(self):
# #         return 61
# #
# #     def get_eggs_price(self):
# #         return None
# #
# #     def get_sugar_price(self):
# #         return 20
# #
# # # Интерфейс для ввода суточной потребности
# # class ConfectionerySystemGUI:
# #     def __init__(self, master):
# #         self.master = master
# #         self.master.title("Кондитерская кампания")
# #
# #         self.label = tk.Label(master, text="Введите суточный спрос на каждый продукт: ")
# #         self.label.pack()
# #
# #         self.flour_demand_label = tk.Label(master, text="Суточная потребность в муке:")
# #         self.flour_demand_entry = tk.Entry(master)
# #         self.flour_demand_label.pack()
# #         self.flour_demand_entry.pack()
# #
# #         self.eggs_demand_label = tk.Label(master, text="Суточная потребность в яйцах:")
# #         self.eggs_demand_entry = tk.Entry(master)
# #         self.eggs_demand_label.pack()
# #         self.eggs_demand_entry.pack()
# #
# #         self.sugar_demand_label = tk.Label(master, text="Суточная потребность в сахаре:")
# #         self.sugar_demand_entry = tk.Entry(master)
# #         self.sugar_demand_label.pack()
# #         self.sugar_demand_entry.pack()
# #
# #         # Кнопка для расчета оптимального плана
# #         self.calculate_button = tk.Button(master, text="Расчет плана", command=self.calculate_optimal_plan)
# #         self.calculate_button.pack()
# #
# #     def calculate_optimal_plan(self):
# #         # Получение введенных данных
# #         flour_demand = int(self.flour_demand_entry.get())
# #         eggs_demand = int(self.eggs_demand_entry.get())
# #         sugar_demand = int(self.sugar_demand_entry.get())
# #
# #         # Создание фабрик для каждого поставщика
# #         supplier1 = Supplier1Factory()
# #         supplier2 = Supplier2Factory()
# #         supplier3 = Supplier3Factory()
# #
# #         # Расчет оптимального плана поставок
# #         total_costs = []
# #         for supplier in [supplier1, supplier2, supplier3]:
# #             total_cost = supplier.get_flour_price() * flour_demand + supplier.get_eggs_price() * eggs_demand + supplier.get_sugar_price() * sugar_demand
# #             total_costs.append((supplier.__class__.__name__, total_cost))
# #
# #         # Нахождение минимальной стоимости и поставщика с оптимальным планом
# #         min_cost_supplier, min_cost = min(total_costs, key=lambda x: x[1])
# #
# #         # Вывод результата
# #         result_label = tk.Label(self.master, text=f"Лучший поставщик: {min_cost_supplier}, Цена: {min_cost}")
# #         result_label.pack()
# #
# # # Создание графического интерфейса
# # root = tk.Tk()
# # app = ConfectionerySystemGUI(root)
# # root.mainloop()
# #
# #
# import tkinter as tk
#
#
# # Абстрактная фабрика поставщиков
# class SupplierFactory:
#     def get_flour_price(self):
#         pass
#
#     def get_eggs_price(self):
#         pass
#
#     def get_sugar_price(self):
#         pass
#
#
# # Конкретные фабрики для каждого поставщика
# class Supplier1Factory(SupplierFactory):
#     def get_flour_price(self):
#         return 60
#
#     def get_eggs_price(self):
#         return 20
#
#     def get_sugar_price(self):
#         return 70
#
#
# class Supplier2Factory(SupplierFactory):
#     def get_flour_price(self):
#         return 62
#
#     def get_eggs_price(self):
#         return 10
#
#     def get_sugar_price(self):
#         return None
#
#
# class Supplier3Factory(SupplierFactory):
#     def get_flour_price(self):
#         return 61
#
#     def get_eggs_price(self):
#         return None
#
#     def get_sugar_price(self):
#         return 20
#
#
# # Интерфейс для ввода суточной потребности
# class ConfectionerySystemGUI:
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Confectionery Supply System")
#
#         self.label = tk.Label(master, text="Enter daily demand for each product:")
#         self.label.pack()
#
#         self.flour_demand_label = tk.Label(master, text="Daily flour demand:")
#         self.flour_demand_entry = tk.Entry(master)
#         self.flour_demand_label.pack()
#         self.flour_demand_entry.pack()
#
#         self.eggs_demand_label = tk.Label(master, text="Daily eggs demand:")
#         self.eggs_demand_entry = tk.Entry(master)
#         self.eggs_demand_label.pack()
#         self.eggs_demand_entry.pack()
#
#         self.sugar_demand_label = tk.Label(master, text="Daily sugar demand:")
#         self.sugar_demand_entry = tk.Entry(master)
#         self.sugar_demand_label.pack()
#         self.sugar_demand_entry.pack()
#
#         # Кнопка для расчета оптимального плана
#         self.calculate_button = tk.Button(master, text="Calculate Plan", command=self.calculate_optimal_plan)
#         self.calculate_button.pack()
#
#     def calculate_optimal_plan(self):
#         # Получение введенных данных
#         flour_demand = int(self.flour_demand_entry.get())
#         eggs_demand = int(self.eggs_demand_entry.get())
#         sugar_demand = int(self.sugar_demand_entry.get())
#
#         # Создание фабрик для каждого поставщика
#         supplier1 = Supplier1Factory()
#         supplier2 = Supplier2Factory()
#         supplier3 = Supplier3Factory()
#
#         # Расчет оптимального плана поставок
#         total_costs = []
#         for supplier in [supplier1, supplier2, supplier3]:
#             flour_price = supplier.get_flour_price()
#             eggs_price = supplier.get_eggs_price()
#             sugar_price = supplier.get_sugar_price()
#
#             total_cost = 0
#             if eggs_price is not None:
#                 total_cost += eggs_price * eggs_demand
#             else:
#                 total_cost += 1000  # Сделаем стоимость высокой, чтобы исключить такого поставщика
#             if sugar_price is not None:
#                 total_cost += sugar_price * sugar_demand
#             else:
#                 total_cost += 1000  # Сделаем стоимость высокой, чтобы исключить такого поставщика
#
#             total_cost += flour_price * flour_demand
#             total_costs.append((supplier.__class__.__name__, total_cost))
#
#         # Нахождение двух наименее дорогих поставщиков
#         total_costs.sort(key=lambda x: x[1])
#         best_suppliers = total_costs[:2]
#
#         # Вывод результата
#         result_label = tk.Label(self.master,
#                                 text=f"Optimal suppliers: {best_suppliers[0][0]}, {best_suppliers[1][0]}, Total cost: {best_suppliers[0][1]}")
#         result_label.pack()
#
#
# # Создание графического интерфейса
# root = tk.Tk()
# app = ConfectionerySystemGUI(root)
# root.mainloop()
import tkinter as tk


# Абстрактная фабрика поставщиков
class SupplierFactory:
    def get_product(self, product_name):
        pass


# Абстрактный класс продукта
class Product:
    def __init__(self, price, max_supply):
        self.price = price
        self.max_supply = max_supply


# Конкретные фабрики для каждого поставщика
class Supplier1Factory(SupplierFactory):
    def get_product(self, product_name):
        if product_name == 'мука':
            return Product(60, 100)
        elif product_name == 'яйца':
            return Product(20, 50)
        elif product_name == 'сахар':
            return Product(70, 80)
        else:
            return None


class Supplier2Factory(SupplierFactory):
    def get_product(self, product_name):
        if product_name == 'мука':
            return Product(62, 110)
        elif product_name == 'яйца':
            return Product(10, 40)
        else:
            return None


class Supplier3Factory(SupplierFactory):
    def get_product(self, product_name):
        if product_name == 'мука':
            return Product(61, 90)
        elif product_name == 'сахар':
            return Product(20, 100)
        else:
            return None


def calculate_optimal_plan(daily_demand, suppliers):
    supplier_factories = {
        'Поставщик 1': Supplier1Factory(),
        'Поставщик 2': Supplier2Factory(),
        'Поставщик 3': Supplier3Factory()
    }

    total_cost = 0
    total_supply = {}

    for supplier_name, products in suppliers.items():
        factory = supplier_factories[supplier_name]
        for product_name, info in products.items():
            factory_product = factory.get_product(product_name)
            if factory_product is not None and product_name in daily_demand:
                demand = daily_demand[product_name]
                if demand > 0:
                    max_supply = min(factory_product.max_supply, demand)
                    cost = max_supply * factory_product.price
                    total_cost += cost
                    total_supply.setdefault(supplier_name, {})[product_name] = max_supply
                    daily_demand[product_name] -= max_supply

    return total_cost, total_supply


def on_submit():
    daily_demand = {
        'мука': int(flour_entry.get()),
        'яйца': int(eggs_entry.get()),
        'сахар': int(sugar_entry.get())
    }

    total_cost, total_supply = calculate_optimal_plan(daily_demand, suppliers)

    result_text.set("Оптимальный план поставок:\n")
    for supplier, products in total_supply.items():
        result_text.set(result_text.get() + f"{supplier}:\n")
        for product, quantity in products.items():
            result_text.set(result_text.get() + f" - {product}: {quantity}\n")

    result_text.set(result_text.get() + f"Общая стоимость: {total_cost} рублей")


# Создание графического интерфейса
root = tk.Tk()
root.title("Optimal Supply Plan")

flour_label = tk.Label(root, text="Введите суточную потребность в муке (кг):")
flour_label.pack()
flour_entry = tk.Entry(root)
flour_entry.pack()

eggs_label = tk.Label(root, text="Введите суточную потребность в яйцах (шт):")
eggs_label.pack()
eggs_entry = tk.Entry(root)
eggs_entry.pack()

sugar_label = tk.Label(root, text="Введите суточную потребность в сахаре (кг):")
sugar_label.pack()
sugar_entry = tk.Entry(root)
sugar_entry.pack()

submit_button = tk.Button(root, text="Рассчитать", command=on_submit)
submit_button.pack()

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=400)
result_label.pack()

suppliers = {
    'Поставщик 1': {
        'мука': {'цена': 60, 'макс_поставка': 100},
        'яйца': {'цена': 20, 'макс_поставка': 50},
        'сахар': {'цена': 70, 'макс_поставка': 80}
    },
    'Поставщик 2': {
        'мука': {'цена': 62, 'макс_поставка': 110},
        'яйца': {'цена': 10, 'макс_поставка': 40},
    },
    'Поставщик 3': {
        'мука': {'цена': 61, 'макс_поставка': 90},
        'сахар': {'цена': 20, 'макс_поставка': 100}
    }
}

root.mainloop()