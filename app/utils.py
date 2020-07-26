import json, urllib.request
from urllib.parse import urlencode


# def main():
#     # 配置您申请的APPKey
#     appkey = "3a18afd0be715ebd7d108d00b7c42729"
#
#     # 1.根据成语查询详细信息
#     request1(appkey, "GET")


# 根据成语查询详细信息
def request1(xz,m="GET"):
    url = "http://apis.juhe.cn/xzpd/query"
    # params = {
    #     "men": men,  # 男星座
    #     "key": '3a18afd0be715ebd7d108d00b7c42729',  # 应用APPKEY(应用详细页查询)
    #     "women": women,  # 女星座
    #
    # }
    key = 'key=3a18afd0be715ebd7d108d00b7c42729'
    # params = urlencode(params)
    params = key+'&'+xz
    if m == "GET":
        # f = urllib.request.urlopen("%s?%s" % (url, params))
        f = urllib.request.urlopen("%s?%s" % (url, params))

    else:
        f = urllib.request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    r = {}
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            r = res["result"]

        else:
            r = {"result":"%s:%s" % (res["error_code"], res["reason"])}
            print()

    else:
        r = {"result":"request api error"}
    return r



if __name__ == '__main__':
    pass