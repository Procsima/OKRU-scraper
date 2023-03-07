import scrapy
import json
import requests
from ..items import GroupPostItem
from ..items import GroupProfileItem


class OkruSpider(scrapy.Spider):
    name = 'okru'
    start_urls = [
        'https://ok.ru/group/56522708811814']  # , 'https://ok.ru/group/56522708811814', 'https://ok.ru/oklive']

    page = 1

    def construct_request(self, group_id, response):
        url = f'https://ok.ru/{group_id}?cmd=AltGroupMainFeedsNewRB&gwt.requested=99041577T1677662206216&st.cmd' \
              f'=altGroupMain&st.groupId={group_id}&st.visitType=GROUP&'

        # response.css('span.invisible').xpath('@st.markerb').extract_first()

        markerB = response.css('span.invisible').extract_first()
        if markerB is not None and len(markerB.split('st.markerb="')) >= 2:
            markerB = markerB.split('st.markerb="')[1].split('"')[0] if self.page != 1 else ''
            print(f'Page: {self.page} {markerB}')
        else:
            print(f'Page: {self.page} END!!!')
            return None

        headers = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        body = {'st.markerB': markerB,
                'fetch': 'false',
                'st.page': str(self.page)}

        self.page += 1

        request = scrapy.FormRequest(
            url,
            callback=self.parse_api,
            headers=headers,
            formdata=body,
            method='POST'
        )

        request.cb_kwargs['group_id'] = str(group_id)

        return request

    def parse(self, response, **kwargs):
        # Group profile
        group_profile = GroupProfileItem()
        group_name = response.css('.group-name_h::text').extract_first()
        group_id = int(response.css('.ellip-i').css('div').xpath('@data-url').extract_first().split('groupId=')[1])
        description_text = response.css('.group-info_desc::text').extract()
        description_link = response.css('.group-info_desc a::text').extract()
        # description_list = []
        description = ''
        for i in range(0, len(description_link)):
            description += description_text[i]
            description += description_link[i]
            # description_list.append(description_text[i])
            # description_list.append(description_link[i])

        for i in range(len(description_link), len(description_text)):
            description += description_text[i]
            # description_list.append(description_text[i])
        #
        #
        # for s in description_list:
        #     description += s

        members_count_strings = response.css('.portlet_h_count::text').extract_first().split('\xa0')
        members_count = int("".join(members_count_strings))
        # for i in range(0, len(members_count_strings)):
        #     members_count += int(members_count_strings[i]) * 1000 ** (len(members_count_strings) - 1 - i)

        posts_count = int(response.css('.mctc_navMenuSec span::text').extract_first())

        place = response.css('.__address div::text').extract_first()
        if place == '':
            place += '-'

        group_profile['item_type'] = "GroupProfile"
        group_profile['group_name'] = group_name
        group_profile['description'] = description
        group_profile['members_count'] = members_count
        group_profile['posts_count'] = posts_count
        group_profile['place'] = place
        group_profile['group_id'] = group_id
        # .u-menu_tx.ellip-i.lp response.css('span .invisible ::attr(st.markerB)').extract()

        yield group_profile

        # Posts

        yield self.construct_request(group_id, response)
        yield self.construct_request(group_id, response)

    def parse_api(self, response, group_id):
        posts = response.css('.feed.js-video-scope.h-mod')
        if posts == None:
            return
        group_post = GroupPostItem()
        for post in posts:
            url = post.css('a.media-text_a').xpath('@href').extract_first()
            publication_date = post.css('.feed_date::text').extract_first()
            text = post.css('.media-text-token::text').extract() + post.css('.media-text_cnt_tx::text').extract()
            user_id = post.css('.group-link.o').extract()
            reactions_count = [int(x) for x in post.css(".js-count::text").extract()]
            ln = len(reactions_count)

            group_post['item_type'] = 'GroupPost'
            group_post['url'] = url
            group_post['text'] = text
            group_post['publication_date'] = publication_date
            # group_post['user_id'] = group_id
            group_post['comments_count'] = reactions_count[0]  # if ln > 0 else 0
            group_post['likes_count'] = reactions_count[2]  # if ln > 2 else 0
            yield group_post
        if self.page != 2:
            self.construct_request(group_id, response)

    # AltGroupMainFeedsNewRB
