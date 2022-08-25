"""
event 线程同步互斥演示
"""
from threading import Thread, Event

msg = None  # 线程通信
e = Event() # Event对象


def 杨子荣():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set()# 打开阻塞


t = Thread(target=杨子荣)
t.start()

# 主线程认证
print("说对口令才是自己人")
e.wait()# 验证前阻塞
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("自己人")
else:
    print("打死他.....无情呀")
t.join()
