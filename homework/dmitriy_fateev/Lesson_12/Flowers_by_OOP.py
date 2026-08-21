import random


class Flower:
    def __init__(self, name, life_time, price, freshness,
                 color, stem_length):
        self.name = name
        self.life_time = life_time
        self.price = price
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length

    def __str__(self):
        return (f"{self.name} (Lifetime: {self.life_time} days, Price: {self.price} rub, "
                f"Freshness: {self.freshness}, "
                f"Color: {self.color}, Stem length: {self.stem_length})")


class Rose(Flower):
    def __init__(self, name="Rose", life_time=14, price=500):
        super().__init__(name, life_time, price, freshness=random.randint(1, 5),
                         color=random.choice(("White", "Red", "Yellow")),
                         stem_length=random.choice((10, 40)))


class Pion(Flower):
    def __init__(self, name="Pion", life_time=10, price=600):
        super().__init__(name, life_time, price, freshness=random.randint(1, 5),
                         color=random.choice(("White", "Red", "Yellow")),
                         stem_length=random.choice((10, 40)))


class Harper(Flower):
    def __init__(self, name="Harper", life_time=20, price=350):
        super().__init__(name, life_time, price, freshness=random.randint(1, 5),
                         color=random.choice(("White", "Red", "Yellow")),
                         stem_length=random.randint(10, 40))


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def __str__(self):
        return "\n".join(str(flower) for flower in self.flowers)

    def price(self):
        return sum(flower.price for flower in self.flowers)

    def lifetime(self):
        if not self.flowers:
            return 0
        return sum(flower.life_time for flower in self.flowers) // len(self.flowers)

    def lifetime_sort(self):
        return sorted(self.flowers, key=lambda flower: flower.life_time, reverse=True)

    def freshness_sort(self):
        return sorted(self.flowers, key=lambda flower: flower.freshness, reverse=True)

    def length_sort(self):
        return sorted(self.flowers, key=lambda flower: flower.stem_length, reverse=True)

    def price_sort(self):
        return sorted(self.flowers, key=lambda flower: flower.price)

    def color_search(self, color):
        return [flower for flower in self.flowers if flower.color.lower() == color.lower()]

    def lifetime_search(self, min_lifetime, max_lifetime):
        return [flower for flower in self.flowers if min_lifetime <= flower.life_time <= max_lifetime]

    def freshness_search(self, freshness):
        return [flower for flower in self.flowers if flower.freshness == freshness]

    def print_lifetime_sort(self):
        print(" СОРТИРОВКА ПО ВРЕМЕНИ ЖИЗНИ (убывание) ")
        for flower in bouquet.lifetime_sort():
            print(f"  {flower.name} - {flower.life_time} дней")

    def print_freshness_sort(self):
        print("\n СОРТИРОВКА ПО СВЕЖЕСТИ (убывание) ")
        for flower in bouquet.freshness_sort():
            print(f"  {flower.name} - свежесть: {flower.freshness}")

    def print_length_sort(self):
        print("\n СОРТИРОВКА ПО ДЛИНЕ СТЕБЛЯ (убывание) ")
        for flower in bouquet.length_sort():
            print(f"  {flower.name} - длина: {flower.stem_length} см")

    def print_price_sort(self):
        print("\n СОРТИРОВКА ПО ЦЕНЕ (возрастание) ")
        for flower in bouquet.price_sort():
            print(f"  {flower.name} - {flower.price} руб.")

    def print_color_search(self, color):
        print("\n ПОИСК ПО ЦВЕТУ ")
        colored_flowers = bouquet.color_search(color)
        if colored_flowers:
            for flower in colored_flowers:
                print(f"  {flower.name} - {flower.color}")
        else:
            print("Таких цветов нет")

    def print_lifetime_search(self, min_lifetime, max_lifetime):
        print("\nПОИСК ПО ВРЕМЕНИ ЖИЗНИ")
        lifetime_flowers = bouquet.lifetime_search(min_lifetime, max_lifetime)
        if lifetime_flowers:
            for flower in lifetime_flowers:
                print(f"  {flower.name} - {flower.life_time} дней")
        else:
            print("  Цветов в этом диапазоне нет")

    def print_freshness_search(self, freshness):
        print("\n ПОИСК ПО СВЕЖЕСТИ ")
        fresh_flowers = bouquet.freshness_search(freshness)
        if fresh_flowers:
            for flower in fresh_flowers:
                print(f"  {flower.name} - свежесть: {flower.freshness}")
        else:
            print("  Цветов этой свежести нет")


rose = Rose()
pion = Pion()
harper = Harper()

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(pion)
bouquet.add_flower(harper)

print(" СОСТАВ БУКЕТА ")
print(f"{bouquet}\n")

print(f"Общая стоимость букета: {bouquet.price()} руб.")
print(f"Время увядания букета: {bouquet.lifetime()} дней\n")

bouquet.print_lifetime_sort()
bouquet.print_freshness_sort()
bouquet.print_price_sort()
bouquet.print_length_sort()
bouquet.print_color_search("red")
bouquet.print_lifetime_search(10, 15)
bouquet.print_freshness_search(5)
