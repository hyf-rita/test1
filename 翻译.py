def fanyi():
    import urllib.request
    import urllib.parse
    import json
    content=input("请输入要翻译的内容：")
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    '''
    head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51'
    '''
    data={}
    data['i']=content
    data['from']= 'AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='16038774188109'
    data['sign']='c249aaf027ffc09bd84117fb8b2e76a4'
    data['lts']='1603877418810'
    data['bv']='23a17424f135105a1b57871cc3d87452'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_REALTlME'
    data=urllib.parse.urlencode(data).encode('utf-8')
    req=urllib.request.Request(url,data)#req=urllib.request.Request(url,data，head)注释掉了head.
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51')
    response=urllib.request.urlopen(url,data)
    html=response.read().decode('utf-8')
    target=json.loads(html)
    print("翻译结果：%s"%(target['translateResult'][0][0]['tgt']),"。")
    fanyi()
fanyi()
