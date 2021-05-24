import time
import random
import matplotlib.pyplot as plt

class Leaky(object):
    """docstring for Leaky"""
    water = 0
    pretime = 0

    #container 总容量
    #rate      1s流出量
    #addNum    每次注入量
    def main(self,container,rate,addNum):
        #当前时间
        nowTime = int(time.time())
        #上次到目前流出去的水
        curWater = self.water-( ( nowTime-self.pretime) * rate )
        #水不能为负
        if curWater<0:
            curWater = 0
        #更新本次注入时间
        self.pretime = nowTime
        #水流出了一部分，不是上一次的水了，更新下，注入再更新，不注入则当前水量
        self.water = curWater
        if (curWater+addNum)<=container :
            #通过，注水后更新水量
            self.water = curWater+addNum
            if curWater+addNum<container:
                bucket_left.append(curWater+addNum)
            else:
                bucket_left.append(container)
            return True
        else:
            self.water = container
            if curWater + addNum < container:
                bucket_left.append(curWater + addNum)
            else:
                bucket_left.append(container)
            return False

flowin=[]
bucket_left=[]
trans=[]

#测试
l = Leaky()
for i in range(1,50):
    time.sleep(0.1)
    a=random.random()*4
    flowin.append(a)
    res = l.main(4,20,a)
    if res==True:
        trans.append(1)
    else:
        trans.append(0)

print(flowin)
print(bucket_left)
#plot graph
plt.plot(flowin,label='data')
plt.plot(bucket_left,label='bucket')
plt.title('Leaky Bucket Algorithm')
plt.ylabel('token_num')
plt.xlabel('time')
plt.legend() # 显示图例
plt.savefig('1.jpg')
plt.show()

plt.plot(trans,label='True=1/False=0')
plt.title('Leaky Bucket Algorithm')
plt.ylabel('True or False')
plt.xlabel('time')
plt.legend() # 显示图例
plt.savefig('2.jpg')
plt.show()