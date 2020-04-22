import sys
'''''''''
 * 小明是个强迫症卖家，有10000台设备，卖的均价要求最接近D元，输出卖出的台数N，总售价M
 * 输入 0<D<10，精确到小数点后12位   ；   输出 M N
 *
 * 思路：
 * 均价与D相接近，初始化M，N为1。然后计算均价M/N。
 * 如果均价 > 幸运数D，则台数(分母)增加。
 * 如果均价 <= 幸运数D，则总售价（分子）增加。
 * 直到 M N 超出循环，其中取台数最小的一个
 */
'''''''''
import datetime
def xingyun(D):
    start = datetime.datetime.now()

    n, m = 1, 1
    # 正负无穷  float("inf"), float("-inf")
    diff = float('inf')
    while m <= 10000 and n <= 10000:
        if abs(m / n - D) < diff:
            tmp_m, tmp_n = m, n
            diff = abs(m / n - D)
        if m / n - D > 0:
            n += 1
        elif m / n - D <= 0:
            m += 1
    end = datetime.datetime.now()
    print(tmp_m, tmp_n)
    print(end - start)
    return


#装饰器单例模式
def singleton(cls):
    instances = {}
    def _singleton(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton


@singleton
class Server(object):
    pass


'''
输入年-月-周-星期
输出年-月-日
eg 2020-4-4-1(第四周周一)————2020-4-20
若输入不合法，输出0
'2020 4 4 1'  n = input().split()
int(n[0]) int(n[1]) int(n[2]) int(n[3])
'''
# 判断是否为闰年
def isLeapYear(year):
    return (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)





# 判断一个月有多少天
def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 \
            or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        return 30



# 判断确定年月的某月一号是一年中第几天
def dayOfyear(year, month):
    s = []
    for i in range(1, month):
        s.append(daysInMonth(year, i))
    print(s, sum(s)+1)
    return sum(s) + 1

# 判断确定年月的某月一号到2018/1/1相隔几天
def dayOveryear(year, month):
    s = []
    for i in range(2018, year):
        print(i, '进入循环的年份')
        if isLeapYear(i) == True:
            s.append(366)
        else:
            s.append(365)
    s2 = sum(s) + dayOfyear(year, month)
    print(s, s2)
    return s2


# 判断确定年月的某月一号是星期几
def whichday(year, month):
    s = dayOveryear(year, month)
    print(s)
    s1 = (s) % 7
    print(s1)
    if s1 == 0:
        s1 = 7
    return s1

# 判断异常
import os
def panduan(year, month, week, day):
    d = whichday(year, month)
    # 这个月一号是星期几
    print('这个月第一天是星期{}'.format(d))
    days = daysInMonth(year, month)
    # 这个月有几天
    print('这个月共有{}天'.format(days))
    p = days % 7
    d_last = (p - 1 + d) % 7
    print('这个月最后一天判断前是星期{}'.format(d_last))
    if d_last == 0:
        d_last = 7
    # 这个月最后一天是星期几
    print('这个月最后一天是星期{}'.format(d_last))
    if day == 7 and days >= 30:
        week_max = 6
    elif day == 6 and days == 31:
        week_max = 6
    elif day == 1 and days == 28:
        week_max = 4
    else:
        week_max = 5
    print('这个月最多有{}周'.format(week_max))
    if week == week_max and day > d_last:
        print('非法输入')
        os._exit(0)
    if week > week_max:
        print('非法输入')
        os._exit(0)
    if week == 1 and day < d:
        print('非法输入')
        os._exit(0)
    if month > 12 or day > 7:
        print('非法输入')
        os._exit(0)


# 把周数星期转换成真正日期
def date(year, month, week, day):
    d = whichday(year, month)
    # # 这个月一号是星期几
    # print('这个月第一天是星期{}'.format(d))
    days = daysInMonth(year, month)
    # # 这个月有几天
    # print('这个月共有{}天'.format(days))
    # p = days % 7
    # d_last = (p - 1 + d) % 7
    # if d_last == 0:
    #     d_last == 7
    # # 这个月最后一天是星期几
    # print('这个月最后一天是星期{}'.format(d_last))
    # if day == 7 and days >= 30:
    #     week_max = 6
    # elif day == 6 and days == 31:
    #     week_max = 6
    # elif day == 1 and days == 28:
    #     week_max = 4
    # else:
    #     week_max = 5
    # print('这个月最多有{}周'.format(week_max))
    # if week == week_max and day > d_last:
    #     print('非法输入')
    #     return
    # if week > week_max:
    #     print('非法输入')
    #     return
    # if week == 1 and day < d:
    #     print('非法输入')
    #     return
    # if month > 12 or day > 7:
    #     print('非法输入')
    #     return
    panduan(year, month, week, day)
    if week == 1 and day >= d:
        d1 = day - d + 1
        print('日期为{}-{}-{}'.format(year, month, d1))
    if week == 2:
        d1 = 7 - d + 1
        d1 += day
        print('日期为{}-{}-{}'.format(year, month, d1))
    if week > 2:
        d1 = 7 - d + 1 + (week - 2) * 7 + day
        if d1 > days:
            print('非法输入')
            return
        print('日期为{}-{}-{}'.format(year, month, d1))
    return






if __name__ == '__main__':
    # dayOfyear(2020, 2)
    # dayOveryear(2019, 1)
    # isLeapYear(2018)
    # whichday(2020, 12)
    date(2020, 5, 5, 1)