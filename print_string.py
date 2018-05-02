# -*- coding:utf-8 -*-
name = input("Name:")
age = int(input("Age:"))
meg = '''
-----%s----
Name:%s
Age:%s
you will be retired: %s
--------------
'''%(name,name,age,65-age)
print(meg)