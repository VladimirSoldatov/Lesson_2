import pymorphy2
with open("C:\\Users\\Samuel\\Downloads\\text.txt", encoding = 'utf-8') as file:

    temp_list = file.read().replace('?','').replace('!','').replace(',','').replace('.','')
    temp_list = temp_list.replace('«','').replace('—','').replace('»','').replace('\n',' ')

morpy = pymorphy2.MorphAnalyzer()
temp_list = temp_list.split()
temp_list = list(map(str.lower, temp_list))

temp = []
temp_dict = dict()
for i in range(len(temp_list)):
    if temp_list[i] not in temp_dict:
        temp_dict[temp_list[i]]=0
    temp_dict[temp_list[i]]+=1
for key, value in temp_dict.items():
    print(key, value, end='\t')
for i in range(len(temp_list)):
   temp_form = morpy.parse(temp_list[i])[0]
   temp.append(temp_form.normal_form)
print()
print()
temp_dict2=dict()
for i in range(len(temp)):
    if temp[i] not in temp_dict2:
        temp_dict2[temp[i]]=0
    temp_dict2[temp[i]]+=1
for key, value in temp_dict2.items():
    print(key, value, end='\t')
#Проверить в PyCharm  не смог, возможно есть более красивое решение
# C:\Users\Samuel\PycharmProjects\Lesson_1\venv\Scripts\python.exe C:/Users/Samuel/PycharmProjects/Lesson_2/Lesson_3.py
# Traceback (most recent call last):
#   File "C:/Users/Samuel/PycharmProjects/Lesson_2/Lesson_3.py", line 1, in <module>
#     import pymorphy2
# ModuleNotFoundError: No module named 'pymorphy2'
#
# Process finished with exit code 1

