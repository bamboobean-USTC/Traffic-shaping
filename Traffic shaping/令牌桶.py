"""An implementation of the token bucket algorithm.
"""
import time
from threading import RLock
from random import random
import matplotlib.pyplot as plt

__all__ = ("TokenBucket", )

class TokenBucket(object):

    def __init__(self, capacity, fill_rate, is_lock=False):
        """
        :param capacity: 10  The total tokens in the bucket.
        :param fill_rate: 1  The rate in tokens/second that the bucket will be refilled
        """
        self._capacity = float(capacity)
        self._tokens = 0
        self._fill_rate = float(fill_rate)
        self._last_time = time.time()
        self._is_lock = is_lock
        self._lock = RLock()

    def _get_cur_tokens(self):
        if self._tokens < self._capacity:
            now = time.time()
            delta = self._fill_rate * (now - self._last_time)
            self._tokens = min(self._capacity, self._tokens + delta)
            self._last_time = now
        return self._tokens

    def get_cur_tokens(self):
        if self._is_lock:
            with self._lock:
                return self._get_cur_tokens()
        else:
            return self._get_cur_tokens()

    def _consume(self, tokens):
        if tokens <= self.get_cur_tokens():
            self._tokens -= tokens
            return True
        return False

    def consume(self, tokens):
        if self._is_lock:
            with self._lock:
                return self._consume(tokens)
        else:
            return self._consume(tokens)

res=[]
token_consume=[]
token_num=[]

l=TokenBucket(10,20)
for i in range(50):
    time.sleep(0.1)
    a = random() * (3+i/5)
    token_consume.append(a)
    token_num.append(l.get_cur_tokens())
    if l.consume(a)==True:
        res.append(1)
    else:
        res.append(0)

print(token_num)
print(res)

#plot graph
plt.plot(token_consume,label='data_in')
plt.plot(token_num,label='token_in_bucket')
plt.title('TokenBucket Algorithm')
plt.ylabel('token_num')
plt.xlabel('time')
plt.legend() # 显示图例
plt.savefig('1_.jpg')
plt.show()

plt.plot(res,label='True=1/False=0')
plt.title('TokenBucket Algorithm')
plt.ylabel('True or False')
plt.xlabel('time')
plt.legend() # 显示图例
plt.savefig('2_.jpg')
plt.show()