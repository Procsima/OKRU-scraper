import requests

def print_hi(name):
    print(f'Hi, {name}')


def my_sum(a: int, b: int):
    return a + b


def selector(a):
    return a % 2 == 0


class A:
    def __init__(self, a, s, t=0):
        self.a = a
        self.s = s
        self.t = t


if __name__ == '__main__':
    # str2 = '05000a0003000000000000000000000000000000000000000000000000000000000000000000000a03010000018485e400bb'
    # str3 = '05001300010000000000000000000000000000000000000a03010000018389836a64'
    # str4 = '05001d0003000000000000000000000000000000000000000000000000000000000000000000000a0301000001828860a1d7'
    # str5 = '0500270003000000000000000000000000000000000000000000000000000000000000000000000a0301000001804c0f6009'
    # str6 = '0500310003000000000000000000000000000000000000000000000000000000000000000000000a03010000017ca409c24a'
    # str7 = '05003b0003000000000000000000000000000000000000000000000000000000000000000000000a03010000017bc0544997'
    # str8 = '05004500010000000000000000000000000000000000000a03010000017a3e6f0052'
    # str9 = '05004f0003000000000000000000000000000000000000000000000000000000000000000000000a030100000179b3bdb7ba'
    # str10 = '0500590003000000000000000000000000000000000000000000000000000000000000000000000a030100000179424400a6'
    # str11 = '05006300010000000000000000000000000000000000000a030100000178b5e54906'
    # str12 = '05006d0003000000000000000000000000000000000000000000000000000000000000000000000a030100000177f7f9d229'
    # str13 = '0500770003000000000000000000000000000000000000000000000000000000000000000000000a03010000017588994ca7'
    # str14 = '0500810003000000000000000000000000000000000000000000000000000000000000000000000a030100000174c067c66c'
    # str15 = '0500880003000000000000000000000000000000000000000000000000000000000000000000000a0301000001745416a165'
    # str16 = '0500920003000000000000000000000000000000000000000000000000000000000000000000000a030100000173e70a4606'
    # str17 = '05009c0003000000000000000000000000000000000000000000000000000000000000000000000a030100000172c8174589'
    # str18 = '0500a50003000000000000000000000000000000000000000000000000000000000000000000000a03010000017270223334'
    # str19 = '0500ae0003000000000000000000000000000000000000000000000000000000000000000000000a03010000017232c4ece3'
    # str20 = '0500b80003000000000000000000000000000000000000000000000000000000000000000000000a030100000171eab1e81c'
    #
    # print(len(str2))
    # print(len(str3))

    s = '<span st.markerb="123"></span>'
    s2 = '<span></span>'

    print(s.split('st.markerb="')[1].split('"')[0])
    print(s2.split('st.markerb="'))

    # url = "https://ok.ru/53078495854752?cmd=AltGroupMainFeedsNewRB&gwt.requested=99041577T1676896504730&st.cmd=altGroupMain&st.groupId=53078495854752&st.visitType=GROUP&"
    #
    # payload = 'st.markerB=&fetch=false&st.page=2'
    # headers = {
    #     # 'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    #     # 'cache-control': 'no-cache',
    #     'content-type': 'application/x-www-form-urlencoded',
    #     'content-length': str(len(payload))
    #     # 'msver': 'V1',
    #     # 'ok-screen': 'altGroupMain',
    #     # 'origin': 'https://ok.ru',
    #     # 'pragma': 'no-cache',
    #     # 'referer': 'https://ok.ru/group/56522708811814',
    #     # 'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    #     # 'sec-ch-ua-mobile': '?0',
    #     # 'sec-ch-ua-platform': '"Windows"',
    #     # 'sec-fetch-dest': 'empty',
    #     # 'sec-fetch-mode': 'cors',
    #     # 'sec-fetch-site': 'same-origin',
    #     # 'strd': 'true',
    #     # 'strv': 'V3',
    #     # 'Cookie': '_statid=c700d2d8-f2b4-4dbd-a275-e9e0d5564de8; bci=8487369636051174221'
    #     # 99041577T1677662206216
    #     # 99041577T1676896504730
    # }
    #
    # response = requests.request("POST", url, headers=headers, data=payload)
    #
    # print(response.text)
    # print(len(payload))

    # nums = [1, 2, 3, 4, 5]
    # even_nums = []
    # for i in nums:
    #     if selector(i):
    #         even_nums.append(i)
    # print(even_nums)
    #
    # l = [int(x) for x in input('Enter nums: ').split()]
    # print(l)

    # li = input().split(' ')
    # s = 0
    # for i in range(0, len(li)):
    #     li[i] = int(li[i])
    #     s += li[i]
    # print(s)
    # print(li)
