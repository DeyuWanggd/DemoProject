import hashlib
import time
import base64
import re
import datetime
def _md5(value):
    '''md5加密'''
    m = hashlib.md5()
    m.update(value.encode('utf-8'))
    return m.hexdigest()
def _base64_decode(data):
    '''bash64解码，要注意原字符串长度报错问题'''
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += '=' * missing_padding
    return base64.b64decode(data)
def jiandan(o,y = '',g = 0):
    d = o
    l = 'DECODE'
    h = 4
    y = _md5(y)
    x = _md5(y[:16])
    v = _md5(y[16:32])
    if h:
        if l == "DECODE":
            b = _md5(str((datetime.datetime.now().microsecond)))
            e = len(b) - h
            u = b[e:]
        else:
            u = ""
        t = x + _md5(x+u)
    if l == "DECODE":
        if g == 0:
            g += int(time.time())
        else:
            g = 0
        tmpstr =str(g)
        if len(tmpstr) >= 10:
            o  = tmpstr[:10]+_md5(o+v)[:16]+o
        else:
                f = 10 - len(tmpstr)
                for each in range(f):
                    tmpstr += '0'
                o = tmpstr +_md5(o+v)[:16]+0
        n = o
    k = []
    for q in range(256):
        k.append(q)
    r = []
    for q in range(256):
        r.append(ord(t[q%len(t)]))
    p = 0
    for q in range(256):
        p = (p+k[q]+r[q])%256
        tmp = k[q]
        k[q] = k[p]
        k[p] = tmp
    m = ''
    #n = n.split('')
    w = 0
    p = 0
    for q in range(len(n)):
        w = (w+1)%256
        p = (p+k[w])%256
        tmp = k[w]
        k[w] = k[p]
        k[p] = tmp
        m += chr(ord(n[q]) ^ k[(k[w]+k[p])%256])
    if l == 'DECODE':
        m =  str(base64.b64encode(m.encode('utf-8')))#编码问题
        c = re.sub('=','',m)
        m += u
        m = _base64_decode(d)
        m = m.decode('utf-8')
        return m
if __name__ == '__main__':
    a = jiandan('Ly93eDIuc2luYWltZy5jbi9tdzYwMC8wMDc2QlNTNWx5MWZ2Zjc5d3h3ZzJqMzB6azBwZXRmMC5qcGc=',"XATlyZjMvyFDoy1qUPmA2stoQqu1bou8")
    print(a)
                
            
        
            
                
                
