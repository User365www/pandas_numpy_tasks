#%% md
# ## Упражнения по библиотеке Numpy
#%%
import numpy as np
#%% md
# **1.** Дан случайный массив, поменять знак у элементов, значения которых между 3 и 8
#%%
arr = np.random.randint(1, 20, (2,4))
res = np.where((arr > 3) & (arr < 8), -arr, arr)
print(res)
#%%
import random
mylist = [random.randint(1, 10) for _ in range(5)]
print(mylist)
res = [-x if 3 < x < 8 else x for x in mylist]
print(res)
#%% md
# **2.** Заменить максимальный элемент случайного массива на 0
#%%
rand_arr = np.random.randint(1, 20, (3, 3))
mask = rand_arr == rand_arr.max()
res = np.where(mask, 0, rand_arr)
print(res)
#%%
random_list = [random.randint(1, 10) for _ in range(5)]
res = [0 if max(random_list) == x else x for x in random_list]
print(random_list)
print(res)
#%% md
# **3.** Построить прямое произведение массивов (все комбинации с каждым элементом). На вход подается двумерный массив
#%%
arr1 = np.random.randint(1, 10, (2, 2))
raveled = [arr1.ravel(), arr1.ravel()]
mesh = np.meshgrid(raveled[0], raveled[1], indexing='ij')
stacked = np.stack([mesh[0].ravel(), mesh[1].ravel()], axis=1)
print(stacked)
#%%
import random
matrix = [[random.randint(1, 10) for _ in range(2)] for _ in range(2)]
print("matrix:")
for row in matrix:
    print(row)

flat = [num for row in matrix for num in row]
print('flat:')
print(flat)
result = []
for a in flat:
    for b in flat:
        result.append([a, b])

print("combinations:")
for combo in result:
    print(combo)
#%% md
# **4.** Даны 2 массива A (8x3) и B (2x2). Найти строки в A, которые содержат элементы из каждой строки в B, независимо от порядка элементов в B
#%%
a_arr = np.random.randint(1, 4, (8, 3))
b_arr = np.random.randint(1, 4, (2, 2))
comp_mask = a_arr[:, None, None, :] == b_arr[None, :, :, None]
b_found_in_a = np.any(comp_mask, axis=3)
contains_all_elem = np.all(b_found_in_a, axis=2)
contains_all_rows = np.all(contains_all_elem, axis=1)
print(np.where(contains_all_rows)[0])
#%%
import itertools
list_A = [[random.randint(1, 3) for _ in range(3)] for _ in range(8)]
list_B = [[random.randint(1, 3) for _ in range(2)] for _ in range(2)]
res = []
print(list_A)
print(list_B)
set_b = set(list(itertools.chain(*list_B)))
print(set_b)
for i, row in enumerate(list_A):
    if set(row) >= set_b:
       res.append(i)
print(res)
#%% md
# **5.** Дана 10x3 матрица, найти строки из неравных значений (например строка [2,2,3] остается, строка [3,3,3] удаляется)
#%%
arr = np.random.randint(1, 4, (10, 3))
comp = arr.max(axis=1) - arr.min(axis=1) == 0
print(np.where(~comp)[0])
#%%
list5 = [[random.randint(1, 3) for _ in range(3)] for _ in range(10)]
print(list5)
comp = [max(x) - min(x) == 0 for x in list5]
print(comp)
indexis = [i for i, b in enumerate(comp) if not b]
print(indexis)
#%% md
# **6.** Дан двумерный массив. Удалить те строки, которые повторяются
#%%
arr = np.random.randint(1, 4, (10, 2))
print(np.unique(arr, axis=0))
#%% md
# ______
# ______
#%% md
# Для каждой из следующих задач (1-5) нужно привести 2 реализации – одна без использования numpy (cчитайте, что там, где на входе или выходе должны быть numpy array, будут просто списки), а вторая полностью векторизованная с использованием numpy (без использования питоновских циклов/map/list comprehension).
# 
# 
# __Замечание 1.__ Можно считать, что все указанные объекты непустые (к примеру, в __задаче 1__ на диагонали матрицы есть ненулевые элементы).
# 
# __Замечание 2.__ Для большинства задач решение занимает не больше 1-2 строк.
#%% md
# ___
#%% md
# * __Задача 1__: Подсчитать произведение ненулевых элементов на диагонали прямоугольной матрицы.  
#  Например, для X = np.array([[1, 0, 1], [2, 0, 2], [3, 0, 3], [4, 4, 4]]) ответ 3.
#%%
arr = np.random.randint(1, 5, (4, 3))
diag_elem = np.diag(arr)
nenul_diag_elem = diag_elem[diag_elem != 0]
res = np.prod(nenul_diag_elem)
print(res)
#%%
import random
list_arr = [[random.randint(0, 4) for _ in range(3)] for _ in range(4)]
size = min(len(list_arr), len(list_arr[0]))
print(list_arr)
print(size)
res = 1
for i in range(size):
    if list_arr[i][i] != 0:
        res *= list_arr[i][i]
print(res)
#%% md
# * __Задача 2__: Даны два вектора x и y. Проверить, задают ли они одно и то же мультимножество.  
#   Например, для x = np.array([1, 2, 2, 4]), y = np.array([4, 2, 1, 2]) ответ True.
#%%
x = np.random.randint(1, 4, 4)
y = np.random.randint(1, 4, 4)
res = np.all((len(x) == len(y)) & (np.sort(x) == np.sort(y)))
print(res)
#%%
x = [random.randint(1, 4) for _ in range(4)]
y = [random.randint(1, 4) for _ in range(4)]
print(x)
print(y)
res = len(x) == len(y) and sorted(x) == sorted(y)
print(res)
#%% md
# * __Задача 3__: Найти максимальный элемент в векторе x среди элементов, перед которыми стоит ноль. 
#  Например, для x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]) ответ 5.
#%%
arr = np.array([1, 0, 3, 5, 0, 7, 4, 3, 0, 11])
pos = np.where(arr[:-1]==0)[0]
res = np.max(arr[pos+1])
print(res)
#%%
arr = [1, 0, 3, 9, 0, 7, 4, 3, 0, 11]
max_el = 0
for i in range(0, len(arr) - 1):
    if arr[i] == 0:
        if arr[i+1] > max_el:
            max_el = arr[i+1]
print(max_el)
#%% md
# * __Задача 4__: Реализовать кодирование длин серий (Run-length encoding). Для некоторого вектора x необходимо вернуть кортеж из двух векторов одинаковой длины. Первый содержит числа, а второй - сколько раз их нужно повторить.  
#  Например, для x = np.array([2, 2, 2, 3, 3, 3, 5]) ответ (np.array([2, 3, 5]), np.array([3, 3, 1])).
#%%
arr = np.array([2, 2, 2, 3, 3, 3, 5])
changed = np.where(np.diff(arr) != 0)[0] + 1
start = np.concatenate(([0], changed))
end = np.concatenate((changed, [len(arr)]))
# print(start)
# print(end)
counts = end - start
values = arr[start]
print(values)
print(counts)
#%%
arr = [2, 2, 2, 3, 3, 3, 5]
values, counts = [], []
for num in arr:
    if not values or num != values[-1]:
        values.append(num)
        counts.append(1)
    else:
        counts[-1] += 1
res = tuple[values, counts]
print(res)
#%% md
# * __Задача 5__: Даны две выборки объектов - X и Y. Вычислить матрицу евклидовых расстояний между объектами. Сравните с функцией scipy.spatial.distance.cdist по скорости работы.
#%%
arr_x = np.array([[1,2],[3,4]])
arr_y = np.array([[1,3],[2,4],[6,8]])
x_sq = np.sum(arr_x**2, axis=1)[:, None]
y_sq = np.sum(arr_y**2, axis=1)[None, :]
xy = arr_x @ arr_y.T
expr = np.maximum(x_sq+y_sq-2*xy, 0)
res = np.sqrt(expr)
print(res)
#%%
import math

X = [[1, 2], [3, 4]]
Y = [[1, 3], [2, 4], [6, 8]]

dist_matrix = [[math.sqrt(sum((xi - yj) ** 2 for xi, yj in zip(x, y)))for y in Y]
    for x in X
]

for row in dist_matrix:
    print(row)
#%% md
# _______
# ________
#%% md
# * #### __Задача 6__: CrunchieMunchies __*__
# 
# Вы работаете в отделе маркетинга пищевой компании MyCrunch, которая разрабатывает новый вид вкусных, полезных злаков под названием **CrunchieMunchies**.
# 
# Вы хотите продемонстрировать потребителям, насколько полезны ваши хлопья по сравнению с другими ведущими брендами, поэтому вы собрали данные о питании нескольких разных конкурентов.
# 
# Ваша задача - использовать вычисления Numpy для анализа этих данных и доказать, что ваши **СrunchieMunchies** - самый здоровый выбор для потребителей.
# 
#%%
import numpy as np
#%% md
# 1. Просмотрите файл cereal.csv. Этот файл содержит количества калорий для различных марок хлопьев. Загрузите данные из файла и сохраните их как calorie_stats.
#%%
calorie_stats = np.loadtxt("./data/cereal.csv", delimiter=",")
calorie_stats
#%% md
# 2. В одной порции CrunchieMunchies содержится 60 калорий. Насколько выше среднее количество калорий у ваших конкурентов?
# 
# Сохраните ответ в переменной average_calories и распечатайте переменную в терминале
#%%
average_calories = np.mean(calorie_stats) - 60
print(average_calories)
#%% md
# 3. Корректно ли среднее количество калорий отражает распределение набора данных? Давайте отсортируем данные и посмотрим.
# 
# Отсортируйте данные и сохраните результат в переменной calorie_stats_sorted. Распечатайте отсортированную информацию
#%%
print(calorie_stats_sorted := np.sort(calorie_stats))
#%% md
# 4. Похоже, что большинство значений выше среднего. Давайте посмотрим, является ли медиана наиболее корректным показателем набора данных.
# 
# Вычислите медиану набора данных и сохраните свой ответ в median_calories. Выведите медиану, чтобы вы могли видеть, как она сравнивается со средним значением.
#%%
print(median_calories := np.median(calorie_stats_sorted))
#%% md
# 5. В то время как медиана показывает, что по крайней мере половина наших значений составляет более 100 калорий, было бы более впечатляюще показать, что значительная часть конкурентов имеет более высокое количество калорий, чем CrunchieMunchies.
# 
# Рассчитайте различные процентили и распечатайте их, пока не найдете наименьший процентиль, превышающий 60 калорий. Сохраните это значение в переменной nth_percentile.
#%%
nth_percentile = None
for p in range(1, 101):
    print(value := np.percentile(calorie_stats_sorted, p))
    if value > 60:
        nth_percentile = np.percentile(calorie_stats_sorted, p)
        break
#%% md
# 6. Хотя процентиль показывает нам, что у большинства конкурентов количество калорий намного выше, это неудобная концепция для использования в маркетинговых материалах.
# 
# Вместо этого давайте подсчитаем процент хлопьев, в которых содержится более 60 калорий на порцию. Сохраните свой ответ в переменной more_calories и распечатайте его
#%%
more_calories = None
for p in range(1, 101):
    if np.percentile(calorie_stats_sorted, p) > 60:
        more_calories = 100 - p
        break
print(more_calories)
#%% md
# 7. Это действительно высокий процент. Это будет очень полезно, когда мы будем продвигать CrunchieMunchies. Но один вопрос заключается в том, насколько велики различия в наборе данных? Можем ли мы сделать обобщение, что в большинстве злаков содержится около 100 калорий или разброс еще больше?
# 
# Рассчитайте величину отклонения, найдя стандартное отклонение, Сохраните свой ответ в calorie_std и распечатайте на терминале. Как мы можем включить эту ценность в наш анализ?
#%%
calorie_std = np.std(calorie_stats_sorted)
print(calorie_std)
print('Стандартное отклонение составляет около 19,36 калорий. Это говорит о том, что калорийность хлопьев у конкурентов довольно сильно варьируется — не все хлопья имеют строго около 100 калорий, а разброс значений значительный. Это подтверждает, что рынок предлагает как более калорийные, так и менее калорийные варианты.')
#%% md
# 8. Напишите короткий абзац, в котором кратко изложите свои выводы и то, как, по вашему мнению, эти данные могут быть использованы в интересах Mycrunch при маркетинге CrunchieMunchies.
#%%
print('CrunchieMunchies (60 калорий на порцию) существенно ниже как среднего значения калорийности по рынку (~106,9 калорий), так и медианы (110 калорий). Более того, 96% конкурентов имеют калорийность выше нашей, что делает наш продукт одним из самых низкокалорийных на рынке. Стандартное отклонение показывает, что разброс калорийности у конкурентов велик, но наша позиция остается стабильно выигрышной.Акцент на том, что CrunchieMunchies — один из самых низкокалорийных продуктов на рынке.')