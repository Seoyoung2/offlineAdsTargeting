from .models import Input
import pandas as pd
from django.shortcuts import render, get_object_or_404,redirect
import os

data_path = '..'

district_dict = {'1': [-118.232639, 34.029397], '2': [-118.397251, 34.183011], '3': [-118.471433, 34.192783],
                '4': [-118.301819, 34.136700], '5': [-118.441259, 34.082240], '6': [-118.444573, 34.228821],
                '7': [-118.403763, 34.261176], '8': [-118.316748, 33.984020], '9': [-118.258982, 34.001521], 
                '10': [-118.326731, 34.036869], '11': [-118.514252, 34.055796], '12': [-118.322400, 34.153600],
                '13': [-118.242890, 34.053988], '14': [-118.181057, 34.071523], '15': [-118.256222, 33.810272]}

dict1 = {('Under 19', 'male'):[9,15,6], ('Under 19', 'female'):[9,15,8], ('Between 19 and 34', 'male'):[13,5,4], ('Between 19 and 34', 'female'):[5,4,13],
        ('Between 34 and 54', 'male'):[4,13,2], ('Between 34 and 54', 'female'):[4,2,10], ('Above 54', 'male'):[12,11,3], ('Above 54', 'female'):[12,11,3],}

# gender와 age를 가지고서 top3 경도위도를 리스트형태로 return
# return [(--,--), (--,--), (--,--)]
def calLocation(pk):
    post = get_object_or_404(Input, pk=pk)

    
    for i in dict1.keys():
        if post.age == i[0] and post.gender == i[1]:
            list1 = dict1[i]
            break
    print(list1)
    result = []
    for i in list1:
        result.append(district_dict[str(i)])

   
    print(result)

    return result
