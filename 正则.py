import re
content='''000
到款大口大口阿萨,德加1.1万/月；
基础范围内非我,方将1.0万/月；
爱上了村民撒村,民们1.2万/月；
某某人1846198999
hyf号码13781699999
hyf号码13462929999
hyf号码00120109999
hyf1a2b3d4e5f
20
,
<html><head><title>hahaha</title>
'''
names='lita, yayi,qiyana fuhua;jiazi'
a=re.compile(r'<.*>')#贪婪模式就是尽可能多的获取更多内容，像hahah都被打印出来了*和+都具有贪婪属性
b=re.compile(r'<.*?>')#加？号即非贪婪模式向hahaha没打印.
c=re.compile(r'[.\d]+万/每{0,1}月')#r表示所有字符不转义，就代表他自己  .代表除换行外所有东西.   +跟*唯一不同点就是不包括0次.
d=re.compile(r',.*')#  *表示匹配前面的子表达式任意次包括0次，意思就是找逗号后的所有内容.
f=re.compile(r'(.*),')#这个表示找，前面的所有内容.把小括号去掉就表示查找的也包括小括号.
e=re.compile(r'\d{10}|\d{2}')#{}里面左面表示最少出现次数右边表最多，只有一个的话就是固定次数.
g=re.compile(r'13[74|4-7]\d{8}')#[74]表示13后面跟7或4都行也可是范围.
h=re.compile(r'[\d][\D]')
#j=re.compile(r'[^abc]')这个即打印非a非b非c的所有东西太长了不打印了.
k=re.compile(r'^\d+',re.MULTILINE)#如果不加这个re.MUL..就只会匹配第一行了.^\d表示只查询开头是数字的.\d+$表示查询结尾数字.
l=re.compile(r'(hyf)\D\D(\d{11})')#两个小括号里面的东西会组队中间用逗号隔开.
m=re.split(r'[,;\s]\s*',names)#\s是空格\s*是任意次数空格
for i in a.findall(content):
    print(i)
for i in b.findall(content):
    print(i)
for i in c.findall(content):
    print(i)
for i in e.findall(content):
    print(i)
for i in g.findall(content):
    print(i)
for i in d.findall(content):
    print(i)
for i in f.findall(content):
    print(i)
for i in h.findall(content):
    print(i)
#for i in j.findall(content):
    #print(i)
for i in k.findall(content):
    print(i)
for i in l.findall(content):
    print(i)
print(m)
