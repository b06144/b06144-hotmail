 # -*- coding:UTF-8 -*-
import os
import requests
from bs4 import BeautifulSoup


for i in range(8):
     for j in range(8):
             if (i+j)%2!=0:
                 print(chr(219),end="")
                 print(chr(219),end="")
             else:
                 print("",end="")
     print("\n",end="")



'''
url= "http://www.biqukan.com/2_2792/"
req = requests.get(url)
req.encoding="gbk"
html = req.text
print(type(html))
#list1=list(html)
#print(type(list1))
#"".join(list1)
#
#print(type(list1))
#print(list1)


if "\ufffd" in html:
    print("我错了")
    html.replace("\ufffd", "我错了")
    print(html)

 #   print(list1)
 #  list2.append("有错误字符")


#print(html)
f=open("biqu1.txt", "w+")
f.writelines(html)
f.close()


#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#html=str(list1)
#html2="".join(html)
#print(html)
#print(html2)

#for line in html:
#	f.write(line)
#	f.write("\n")


#print(f.tell())
'''

'''
div_bf = BeautifulSoup(html)
print(type(div_bf.text))
f=open("biqu1.txt", "w+")
f.writelines(str(div_bf))
'''
#f.close()


