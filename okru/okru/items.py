# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GroupPostItem(scrapy.Item):
    url = scrapy.Field()
    user_id = scrapy.Field()
    text = scrapy.Field()
    publication_date = scrapy.Field()
    comments_count = scrapy.Field()
    likes_count = scrapy.Field()
    item_type = scrapy.Field()


class GroupProfileItem(scrapy.Item):
    url = scrapy.Field()
    group_name = scrapy.Field()
    group_id = scrapy.Field()
    description = scrapy.Field()
    members_count = scrapy.Field()
    posts_count = scrapy.Field()
    place = scrapy.Field()
    item_type = scrapy.Field()


# "url": str // ссылка на пост
# "user_id": str,
# "text": text,
# "publication_date": timestamp,
# "comments_count": int,
# "likes_count": int,
# “item_type”: “GroupPost”

# posts = response.css('.feed.js-video-scope.h-mod')
        # group_post = GroupPostItem()
        # for post in posts:
        #     url = post.css('a.media-text_a').xpath('@href').extract_first()
        #     publication_date = post.css('.feed_date::text').extract_first()
        #     text = post.css('.media-text-token::text').extract() + post.css('.media-text_cnt_tx::text').extract()
        #     group_id = post.css('.group-link.o').extract()
        #     reactions_count = [int(x) for x in post.css(".js-count::text").extract()]
        #     ln = len(reactions_count)
        #
        #     group_post['item_type'] = 'GroupPost'
        #     group_post['url'] = url
        #     group_post['text'] = text
        #     group_post['publication_date'] = publication_date
        #     group_post['user_id'] = group_id
        #     group_post['comments_count'] = reactions_count[0]  # if ln > 0 else 0
        #     group_post['likes_count'] = reactions_count[2]  # if ln > 2 else 0
        #     yield group_post
