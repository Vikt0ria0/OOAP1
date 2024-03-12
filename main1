# daily_demand = {
#     'мука': int(input("Введите суточную потребность в муке (кг): ")),
#     'яйца': int(input("Введите суточную потребность в яйцах (шт): ")),
#     'сахар': int(input(" суточную потребность в сахаре (кг): "))
# }
#
# suppliers = {
#     'Поставщик 1': {
#         'мука': {'цена': 60, 'макс_поставка': 100},
#         'яйца': {'цена': 20, 'макс_поставка': 50},
#         'сахар': {'цена': 70, 'макс_поставка': 80}
#     },
#     'Поставщик 2': {
#         'мука': {'цена': 62, 'макс_поставка': 110},
#         'яйца': {'цена': 10, 'макс_поставка': 40},
#
#     },
#     'Поставщик 3': {
#         'мука': {'цена': 61, 'макс_поставка': 90},
#         'сахар': {'цена': 20, 'макс_поставка': 100}
#     }
# }
#
# # Расчет оптимального плана поставок
# total_cost = 0
# total_supply = {}
#
# for supplier, products in suppliers.items():
#     for product, info in products.items():
#         if product in daily_demand:
#             demand = daily_demand[product]
#             if demand > 0:
#                 max_supply = min(info['макс_поставка'], demand)
#                 cost = max_supply * info['цена']
#                 total_cost += cost
#                 total_supply.setdefault(supplier, {})[product] = max_supply
#                 daily_demand[product] -= max_supply
#
# # Вывод результатов
# print("Оптимальный план поставок:")
# for supplier, products in total_supply.items():
#     print(f"{supplier}:")
#     for product, quantity in products.items():
#         print(f" - {product}: {quantity}")
# print(f"Общая стоимость: {total_cost} рублей")
import tkinter as tk


# Конкретные классы продуктов и поставщиков
class Product:
    def __init__(self, price, max_supply):
        self.price = price
        self.max_supply = max_supply


# Функция для расчета оптимального плана поставок
def calculate_optimal_plan(daily_demand, suppliers):
    total_cost = 0
    total_supply = {}

    for supplier_name, products in suppliers.items():
        for product_name, info in products.items():
            if product_name in daily_demand:
                demand = daily_demand[product_name]
                if demand > 0:
                    max_supply = min(info.get('макс_поставка', float('inf')), demand)
                    cost = max_supply * info['цена']
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

# Данные поставщиков
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
