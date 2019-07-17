from urllib import request,parse
#1.基本步骤
#引入urllib模块 parse模块用于编码解码
url = "http://www.baidu.com/s"
#设置需要爬取的网址
params = {"wd":"博客园"}
#url参数，urlencode函数用于编码中文和特殊字符 parse.parse_qs(qs)用于解码
qs = parse.urlencode(params)
#编码
url = url + "?" + qs
#使用get方法，将url与参数相连
res = request.urlopen(url)
#urlopen的参数
#def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
#            *, cafile=None, capath=None, cadefault=False, context=None):
#print(res.read())

#2.将网页上的文件保存到本地
res = request.urlretrieve("https://www.cnblogs.com/",'cnblog.html')

#3.urlparse(url)对url的各个组成部分进行分割
url = "https://www.baidu.com/s?wd=cnblog#2"
result = parse.urlparse(url)
print(result)
#ParseResult(scheme='https', netloc='www.baidu.com', path='/s', params='', query='wd=cnblog', fragment='2')





