


# 统计一段英文短语里单词出现的次数
"""编写一段代码
1.接收键盘输入的英文短语
2.使用空格、逗号、句号分割短语中的单词
3.统计短语中每个单词，出现的次数(忽略大小写)
4.将结果存储为“字典”
范例：
输入:hello python.Learning Python
输出：{'hello':1,'python':2,'learning':1}"""

# 第一步，接收键盘输入
# input_string = input("请输入一段英文短语：")
input_string = 'hello python.Learning Python'
# 第二步，处理空格、逗号、句号。转化成唯一的标识符来识别
# input = raw_input.replace(',',' ')#使用字符串的replace()方法可以替换 逗号 为 空格
#这里遇到一个小问题
# 1.replace()仅仅支持一次替换一个字符串
# 2.需要穷尽可能的分隔符（逗号、句号）提问“回车”需要考虑么？
# 解决方案1：通过多次替换，达到目的
# input = raw_input.replace('.',' ')
# 解决方案2：使用for循环
mark_list = [",", "，", ".", "。", '"', "“", "”", "、", "(", ")"]
for i in mark_list:
    input_string = input_string.replace(i, " ")  # 把非空格的符号转化成空格
print(input_string)#处理完成，进行分割
input_string = input_string.lower()#不区分大小写这一步要在这处理
# 小问题：短语首尾可能有空格
input_string = input_string.strip()
word_list = input_string.split(' ')
print(word_list)

# 第三步，获取单词项
# 难点-对列表项进行去重
# 方式1:
# word_key = []
# for i in word_list:
#     if not i in word_key:
#         word_key.append(i)
# print(word_key)

# 方式2：
word_key = set(word_list)
print(word_key)
# 第四步：统计词频，并储存结果
dict_word = {}

# dict_word['hello'] = word_list.count('hello')

for i in word_key:
    dict_word[i] = word_list.count(i)

print(dict_word)


