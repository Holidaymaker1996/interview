import requests
from pyquery import PyQuery as pq


def ip_url(url):
    r = requests.get(url)
    page = r.content
    e = pq(page)
    dd = e('pre')
    dd = str(dd)
    dd = dd.split('\n')
    allip = []
    for j in range(1, len(dd) - 1):
        temp = dd[j].split('\t')
        ziip = []
        ziip.append(temp[0])
        ziip.append(temp[1])
        allip.append(ziip)
    # print(allip)
    return allip


def binip(i):
    str1 = ''
    i = i.split(".")
    for j in range(len(i)):
        # print(int(i[j]))
        ele = bin(int(i[j]))
        # print(ele)  0b10101011
        str1 = str1 + ele[2:].zfill(8)
    str1 = int("0b" + str1, base=2)

    return str1


def translate(ips):
    for k in range(len(ips)):
        i = ips[k]
        i[0] = binip(i[0])
        i[1] = binip(i[1])
    return ips


def is_edu_id(ip: str) -> bool:
    """判断 ip 是否是教育网ip"""
    # 1. 从 http://ipcn.chacuo.net/view/i_CERNET 获取教育网ip列表
    url = 'http://ipcn.chacuo.net/down/t_txt=c_CERNET'
    ips = ip_url(url)
    ips = translate(ips)
    ip = binip(ip)
    for i in ips:
        if ip >= i[0] and ip <= i[1]:
            return True
    return False


if __name__ == '__main__':
    ip = "202.38.171.1"
    print(is_edu_id(ip))
    # 首先利用requests发送get请求拿到响应报文， 然后利用pyquey去解析页面中的元素， 由此拿到了所
    # 有的ip， 放到一个列表里面。 判断一个ip是否属于某个子网的话，看它是否在ip网段的范围内，根据
    # 爬下来的数据可以看到，每行数据，ip开始的地方，ip结束的地方，一共有多少个IP，把ip地址先转为
    # 32位的二进制的一个数，在转为十进制，再将传进来的ip也先转32位二进制再转为十进制，循环所有IP列表，
    # 判断是否在教育网IP的范围内。
