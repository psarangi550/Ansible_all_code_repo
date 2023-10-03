str1="aaabbccdddaa"

from collections import Counter

# print(Counter(str1))

dict1={}

# for item in str1:
#     if item not in dict1:
#         dict1[item]=1
#     else:
#         dict1[item]+=1

    
# print(dict1)

#[2:48 PM] Tiwari, Sailee (ADV D IN PAMC MC TPA-T&E)


# Find the most repeated word in a text file:
# text : "Hello World! This is the interview session for Python technology. Python uses the latest technical jargons and a booming technology. All the best for the interview"
# and return as a dictionary. Also count the number of characters and return it as integer. Create a function.


# text1="Hello World! This is the interview session for Python technology. Python uses the latest technical jargons and a booming technology. All the best for the interview"

f=open("test.txt")

text1=f.read()

list1=text1.split()

my_dict=dict(Counter(list1))

for key,value in my_dict.items():
    print(f"{key}--->{value}")


result=[]

# for item in list1:
#     if item not in result:
#         result.append(item)

    

# for item in text1:
#     if item not in dict1:
#         dict1[item]=1
#     else:
#         dict1[item]+=1

# print(dict1)

# # dictdoeted()

# print(dict1)