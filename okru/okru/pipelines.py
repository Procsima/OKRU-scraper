# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import dateparser

begin = dateparser.parse('2021-04-22 00:00:00')
end = dateparser.parse('2022-06-22 00:00:00')


class DatePipeline:
    def process_item(self, item, spider):
        if item['item_type'] == 'GroupPost':
            date = dateparser.parse(item['publication_date'])
            if date < begin or date > end:
                # checking data
                raise DropItem()
        return item

class TextPipeline:
    def process_item(self, item, spider):
        if item['text'] == 'GroupPost':
            if item['text'] is None:
                raise DropItem()
        return item

class PlacePipeline:
    def process_item(self, item, spider):
        if item['item_type'] == 'GroupProfile':
            if item['place'] is None:
                raise DropItem()
        return item
