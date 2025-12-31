#%% md
# ## Датасет собран из базы данных переписи 1994 года и содержит данные о доходах.
# ### Информация о данных:
# * age: continuous.
# * workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
# * fnlwgt: continuous.
# * education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, * Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
# * education-num: continuous.
# * marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
# * occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
# * relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
# * race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
# * sex: Female, Male.
# * capital-gain: continuous.
# * capital-loss: continuous.
# * hours-per-week: continuous.
# * native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
# * salary: >50K,<=50K
# 
# ## Проведите анализ данных при помощи Pandas выполнив поставленные задачи.
# #### 
#%%
import pandas as pd
from numpy.ma.extras import unique
#%%
# загружаем датасет
data = pd.read_csv("./data/adult.data.csv")
data.head()
#%% md
# **1. Посчитайте, сколько мужчин и женщин (признак *sex*) представлено в этом датасете**
#%%
print(data['sex'].value_counts())
#%% md
# **2. Каков средний возраст мужчин (признак *age*) по всему датасету?**
#%%
data_m = data[data['sex'] == 'Male']
res = data_m['age'].mean()
print(res)
#%% md
# **3. Какова доля граждан Соединенных Штатов (признак *native-country*)?**
#%%
everybody = len(data)
usa_natives = len(data[data['native-country'] == 'United-States'])
print(usa_natives/everybody)
#%% md
# **4-5. Рассчитайте среднее значение и среднеквадратичное отклонение возраста тех, кто получает более 50K в год (признак *salary*) и тех, кто получает менее 50K в год**
#%%
print(data.groupby('salary')['age'].mean())
print(data.groupby('salary')['age'].std())
#%% md
# **6. Правда ли, что люди, которые получают больше 50k, имеют минимум высшее образование? (признак *education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters* или *Doctorate*)**
#%%
education = ['Bachelors', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', 'Masters', 'Doctorate']
educated = data['education'].isin(education) # educated - true, not educated - false
high_salary = educated[data['salary'] == '>50K'] # only high salary
print(high_salary.all()) # all high salary - educated
#%% md
# **7. Выведите статистику возраста для каждой расы (признак *race*) и каждого пола. Используйте *groupby* и *describe*. Найдите таким образом максимальный возраст мужчин расы *Asian-Pac-Islander*.**
#%%
data.groupby(['race', 'sex'])['age'].describe()
#%% md
# **8. Среди кого больше доля зарабатывающих много (>50K): среди женатых или холостых мужчин (признак *marital-status*)? Женатыми считаем тех, у кого *marital-status* начинается с *Married* (Married-civ-spouse, Married-spouse-absent или Married-AF-spouse), остальных считаем холостыми.**
#%%
res_for_married = data[(data['sex'] == 'Male') & data['marital-status'].str.startswith('Married')]['salary'].eq('>50K').mean()*100
res_for_single = data[(data['sex'] == 'Male') & ~(data['marital-status'].str.startswith('Married'))]['salary'].eq('>50K').mean()*100
print(res_for_married)
print(res_for_single)
res = 'married' if res_for_married > res_for_single else 'single'
print(res)
#%% md
# **9. Какое максимальное число часов человек работает в неделю (признак *hours-per-week*)? Сколько людей работают такое количество часов и каков среди них процент зарабатывающих много?**
#%%
max_hours_per_week = data['hours-per-week'].max()
print(f'max hours per week - {max_hours_per_week}')
hard_workers = data[data['hours-per-week'] == max_hours_per_week]
print(f'number of people working max hours per week - {len(hard_workers)}')
res = hard_workers['salary'].eq('>50K').mean()*100
print(f'{res}% of hard workers have high salary')
#%% md
# **10. Посчитайте среднее время работы (*hours-per-week*) зарабатывающих мало и много (*salary*) для каждой страны (*native-country*).**
#%%
grouped = data.groupby(['salary', 'native-country'])['hours-per-week'].mean()
print(grouped)
#%% md
# **11.Сгруппируйте людей по возрастным группам *young*, *adult*, *retiree*, где:**
# * *young* соответствует 16-35 лет
# * *adult* - 35-70 лет
# * *retiree* - 70-100 лет
# 
# **Проставьте название соответсвтуещей группы для каждого человека в новой колонке AgeGroup**
#%%
def get_age_group(age):
    if 16 <= age <= 35:
        return 'young'
    elif 35 < age <= 70:
        return 'adult'
    elif 70 < age <= 100:
        return 'retiree'
    else:
        return 'Default'

data['AgeGroup'] = data['age'].apply(get_age_group)
print(data['AgeGroup'])
#%% md
# **12-13. Определите количество зарабатывающих >50K в каждой из возрастных групп (колонка AgeGroup), а также выведите название возрастной группы, в которой чаще зарабатывают больше 50К (>50K)**
#%%
data['higher_sal'] = data['salary'] == '>50K'
grouped = data.groupby('AgeGroup')['higher_sal'].mean() * 100
print(grouped)
res = grouped[grouped == grouped.max()].index[0]
print(f'{res} - more percent of high salary')
#%% md
# **14. Сгруппируйте людей по типу занятости (колонка occupation) и определите количество людей в каждой группе. После чего напишите функциюю фильтрации filter_func, которая будет возвращать только те группы, в которых средний возраст (колонка age) не больше 40 и в которых все работники отрабатывают более 5 часов в неделю (колонка hours-per-week)**
#%%
data_f = data.groupby('occupation').size()
print(f'count of people for every group - {data_f}')
def filter_func(mydata):
    age_condition = mydata['age'].mean() <= 40
    hours_condition = (mydata['hours-per-week'] > 5).all()
    return age_condition and hours_condition
res = data.groupby('occupation').filter(filter_func)
print(f' group - {res['occupation'].unique()[0]}')