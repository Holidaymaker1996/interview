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





if __name__ == '__main__':

    # xingyun(3.14159265358979)
    xingyun(0.5000000000000000)
    



