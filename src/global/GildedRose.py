from AgedBrie import AgedBrie
from ConjuredItem import ConjuredItem
import Item
import NormalItem
import Sulfuras


class GildedRose():

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # lo que hacemos aquí es llamar a item, que contendrá una clase con su propio método update_quality
            # lo que significa que cada clase llamará a un método que se llama igual, pero que varía su comportamiento
            # polimorfismo.
            item.update_quality()

    @staticmethod
    def create_item(name, sell_in, quality):
        item_types = {'normal': NormalItem, 'conjured': ConjuredItem, 'aged brie': AgedBrie, 'sulfuras': Sulfuras,
                      'backstage': Backstage}
        type = name.split()
        item_class = item_types.get(type[0].lower())
        if item_class:
            return item_class(name, sell_in, quality)
        else:
            item_class = item_types.get((type[0] + ' ' + type[1]).lower())
            if item_class:
                return item_class(name, sell_in, quality)
            else:
                raise ValueError(f"Tipo de item inválido {name}")


if __name__ == "__main__":

    def currentItems():
        items = [
            NormalItem(name="+5 Dexterity Vest", sell_in=10, quality=20),
            AgedBrie(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            ConjuredItem(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
        ]

        return items


    def newItems():
        afterItems = [
            NormalItem(name="+5 Dexterity Vest", sell_in=8, quality=18),
            AgedBrie(name="Aged Brie", sell_in=0, quality=3),
            Item(name="Elixir of the Mongoose", sell_in=3, quality=5),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=-2, quality=80),
            Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=-3, quality=80),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=13, quality=22),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=54),
            Backstage(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=55),
            ConjuredItem(name="Conjured Mana Cake", sell_in=2, quality=2),  # <-- :O
        ]
        return afterItems


    def test_gilded_rose(items, afterItems):
        dias = 2
        for dia in range(dias):

            print("-------- día %s --------" % dia)
            print("name, sellIn, quality")
            for item in items:
                print(item)
            print("")
            GildedRose(items).update_quality()

        assert items == afterItems


    test_gilded_rose(currentItems(), newItems())
