
import time

def sleep(n_secs):
    time.sleep(n_secs)

def gettime_stamp():  # 订单方法获取时间戳
    return str(int(time.time() * 1000))


def print_documentId(doc_id): # 打印documentId参数里边的值
    print ("documentId = {}".format(doc_id))
