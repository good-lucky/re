元字符 （即正则表达式中有特殊含义的符号）

1. 普通字符
元字符 ： abc
匹配规则 ： 匹配相应的普通字符

In [6]: re.findall("abc","abcdefghabcdhig")
Out[6]: ['abc', 'abc']

2. 或 
元字符 ：  ab|cd
匹配规则 ： 匹配|两边任意一个正则表达式符合的情况
In [7]: re.findall("ab|cd","abcdefghabcdhig")
Out[7]: ['ab', 'cd', 'ab', 'cd']
* |两侧不要有没用的空格

3. 匹配单一字符
元字符 ：  .
匹配规则： 匹配除了换行之外的任意字符
f.o---》 foo  fao  f@o

In [10]: re.findall("f.o","foo is not fao")
Out[10]: ['foo', 'fao']

4. 匹配开始位置
元字符： ^
匹配规则： 匹配一个字符串的开始位置
^Hello  ---> Hello world  : Hello

In [14]: re.findall("^hello","hello world")
Out[14]: ['hello']

5. 匹配结束位置
元字符： $
匹配规则：匹配目标字符串的结束位置
py$  --->  hello.py

In [16]: re.findall("py$","hello.py")
Out[16]: ['py']

6. 匹配重复
元字符 ：  *
匹配规则： 匹配前面的正则表达式重复0次或多次
fo* ---》 fo  foo  foooooooo   f

In [19]: re.findall("ab*","abbcdef")
Out[19]: ['abb']

7. 匹配重复
元字符 ：  + 
匹配规则： 匹配前面的正则表达式重复1次或多次

ab+   ---》   ab  abbb  abbbb
In [23]: re.findall(".+py$","hello.py")
Out[23]: ['hello.py']

8. 匹配重复
元字符：   ？
匹配规则： 匹配前面的正则表达式重复0次或1次
ab？ -->   a   ab

In [24]: re.findall("ab?","abcdefa")
Out[24]: ['ab', 'a']

9. 匹配重复
元字符：  ｛n｝
匹配规则 ： 匹配指定的重复次数
ab{3} --->  abbb
In [25]: re.findall("ab{3}","abbbbbbbb")
Out[25]: ['abbb']

10. 匹配重复
元字符 ：  ｛m,n｝
匹配规则 ： 匹配前面的正则表达式重复 m次 到 n次
ab｛3,5｝  abbb  abbbb abbbbb
In [26]: re.findall("ab{2,5}","abcdabbbabbbbbb")
Out[26]: ['abbb', 'abbbbb']

11. 匹配字符集合
元字符：  []
匹配规则 :  匹配括号范围内的任意一个字符
[abc123d]  a b c 1 2 3 d
[a-z]  
[A-Z]
[0-9]
[123a-zA-Z]
In [31]: re.findall("[_0-9a-zA-Z]","Hello world 123")

12. 匹配字符集合
元字符： [^...]
匹配规则 ： 匹配除指定字符集之外的任意字符

In [34]: re.findall("[^abc]","nihao abc")
Out[34]: ['n', 'i', 'h', 'o', ' ']

13. 匹配任意（非）数字字符
元字符：  \d    \D
匹配规则 ： \d 匹配任意数字字符   \D  匹配任意非数字字符
             [0-9]                 [^0-9]

In [35]: re.findall("1\d{10}","17611665537")
Out[35]: ['17611665537']

14. 匹配（非）普通字符  （普通字符： 数字字母下划线）
元字符 ： \w            \W
匹配规则:  \w 匹配任意一个普通字符  \W匹配任意非普通字符
          [_0-9a-zA-Z]              [^_0-9a-zA-Z]

In [39]: re.findall("\w+","hello$1")
Out[39]: ['hello', '1']

In [40]: re.findall("\W+","hello$1")
Out[40]: ['$']

15. 匹配（非）空字符
元字符 :  \s      \S
匹配规则：\s 匹配任意空字符    \S 匹配任意非空字符
          [ \n\t\r]

In [45]: re.findall("\s",'hello world\r\n\t\0')
Out[45]: [' ', '\r', '\n', '\t']

16. 匹配起止位置
元字符：   \A     \Z
匹配规则 ： \A匹配开始位置    \Z匹配结束位置
             ^                 $
绝对匹配  \Aabc\Z  ----> abc (且字符串只是abc)

In [48]: re.findall("\A/\w+/\w+\Z",'/football/zhongchao')
Out[48]: ['/football/zhongchao']

17. 匹配(非)单词边界位置
元字符： \b     \B
匹配规则 ： \b 匹配单词的边界    \B匹配非单词的边界

单词边界 ： 数字字母下划线和其他字符的交界位置为单词的边界

abc_1 haha

In [55]: re.findall(r"\Bis\b",'This is a test')
Out[55]: ['is']

元字符总结

匹配单个字符：a  .  \d  \D   \w  \W  \s  \S  [...]  [^...]
匹配重复性 ： *   +   ？  ｛N｝  ｛m,n｝
匹配某个位置 ： ^   $   \A  \Z   \b  \B
其他 ：  |   （）  \

正则表达式特殊符号 ： 
.   *   ?   $  ''   ""   []  {}  ()   \  ^ 
如果想匹配特殊符号则加转义

\"\.\"   ----->  "."

r ---> raw  原生字符串 ： 不进行转义

In [64]: re.findall(r"\bis",'This is')
Out[64]: ['is']


贪婪和非贪婪

正则表达式默认的重复匹配模式 ： 贪婪模式
尽可能多的向后匹配

*  +   ？  ｛m,n｝  这四种情况下会产生贪婪模式

非贪婪模式 ： 尽可能少的匹配内容，满足正则表达式含义即可

贪婪---》非贪婪   *？   +？  ??  ｛m,n｝?

In [70]: re.findall("ab*?",'abbbbbbbbcded')
Out[70]: ['a']

In [71]: re.findall("ab+?",'abbbbbbbbcded')
Out[71]: ['ab']

正则表达式分组

使用（）可以为一个正则表达式建立一个子组，子组可以看做内部的整体
abcdef ----》 http://www.baidu.com

子组的作用
1. 增加子组后对正则表达式整体的匹配内容没有影响
2. 子组可以改变重复元字符的重复行为
3. 子组在某些操作中可以对子组匹配内容单独提取

子组的注意事项
1.每个正则表达式可以有多个子组，由外到内由左到右为第一第二。。。。子组
2.子组通常不要交叉

捕获组和非捕获组（命名组和非命名组）
子组命名格式
（?P<name>abc）
1.很多编程接口可以直接通过名字获取子组匹配内容
2.捕获组中的正则表达式可以通过名字重复调用
(?P=name)

(?P<dog>ab)cdef(?P=dog) -----> abcdefab

In [83]: re.search('(ab)+','ababababab').group()
Out[83]: 'ababababab'

In [84]: re.search('(?P<dog>ab)cdef(?P=dog)','abcdefabcde').group()
Out[84]: 'abcdefab'




