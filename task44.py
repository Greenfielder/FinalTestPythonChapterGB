# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
# Вариант решения с использованием get_dummies
# print(pd.get_dummies(data['whoAmI']))

unique_values = data['whoAmI'].unique()
for value in unique_values:
    # Если нужно вместо 0 и 1 использовать true и false : data[value] = (data['whoAmI'] == value)
    data[value] = (data['whoAmI'] == value).astype(int)
data = data.drop('whoAmI', axis=1)
print(data)