import requests


ip_filt = open('python/ip.txt')
max_num = 1000

i = 0
while i < max_num:
    file = open('python/ip_ok.txt', 'w', encoding='utf-8')
    try:
        ip = ip_filt.readline()
        requests.get('http://baidu.com/', proxies={"http": ip}, timeout=10)
    except:
        pass
    else:
        file.write(ip)
    print('%.1f %%' % (i/max_num*100), end='\r')
    i = i + 1
file.close()
print('*************完成*************')

