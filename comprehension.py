#list comprehension
fruits = [
    {'name':'avacado','price':10},
    {'name':'apple','price':20},
    {'name':'orange','price':5},
]
fruit_names = [i['name'] for i in fruits if i['price']>=10]
fruit_price = [i['price'] for i in fruits if i['name'][0]=='a']
print(fruit_names,fruit_price)
#dict comprehension
from collections import OrderedDict
dict = OrderedDict({i['name']:i['price'] for i in fruits})
dict2 = {i for i in dict.items()}
list = [i for i in dict.values()]
print(dict,dict2,list)

words = ['abhishek', 'aditya', 'abhinav', 'adarsh']
wordlength = {str(i): len(i) for i in words}
print(wordlength.items())
