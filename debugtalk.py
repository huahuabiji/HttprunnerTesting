
import time

def sleep(n_secs):
    time.sleep(n_secs)

def gettime_stamp():  # 订单方法获取时间戳
    return str(int(time.time() * 1000))


def print_documentId(doc_id): # 打印documentId参数里边的值
    print ("documentId = {}".format(doc_id))

def get_base_url(env_type="prod"):  # 定义环境函数
    if env_type == "prod": # 线上环境地址
        return "https://mubu.com"
    elif env_type == "beta":  # beta环境地址
        return "https://beta-mubu.com"
    else:
        return "https://test-mubu.com"  # 测试环境地址