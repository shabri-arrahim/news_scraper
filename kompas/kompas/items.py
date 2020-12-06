from scrapy.item import Item, Field


class KompasItem(Item):
    # List of fields
    content = Field()
    title = Field()
    link = Field()
    images = Field()
    category = Field()
    date = Field()
    desc = Field()
