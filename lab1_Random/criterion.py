from scipy.stats import chisquare, chi2


# Критерий промежутков между днями рождений
# Генератор Фибоначчи и его производные не проходят этот критерий
def bday_criterion(cnt):
    r = [0] * 4

    non_zero_ind = [i for i in range(len(cnt)) if cnt[i] != 0]

    for i in range(len(non_zero_ind) - 1):
        r[0] += cnt[non_zero_ind[i]] - 1
        step = non_zero_ind[i + 1] - non_zero_ind[i]
        if step > 2:
            r[3] += 1
        else:
            r[step] += 1

    # учет шага последнего и первого
    step = non_zero_ind[0] + len(cnt) - non_zero_ind[-1]
    if step > 2:
        r[3] += 1
    else:
        r[step] += 1

    return r


# Критерий хи-квадрат
def chi2_criterion(cnt):
    chisq, pvalue = chisquare(cnt)  # значение критерия хи2 и p-value
    # Другой способ:
    # df = len(cnt) - 1  # кол-во степеней свободы
    # chisq = calculate_chisq(cnt)
    # pvalue = 1 - chi2.cdf(chisq, df)  # вероятность получить значение критерия хи2
    return pvalue


# Вычисление значения критерия хи-квадрат
def calculate_chisq(cnt):
    n = sum(cnt)  # кол-во сгенерированных чисел
    k = len(cnt)  # кол-во чисел в диапазоне генерации

    p = 1 / k
    e = n * p

    chisq = 0
    for j in range(k):
        chisq += (cnt[j] - e)**2 / e

    return chisq


# Преобразование последовательности сгенерированных чисел в список-счетчик
def create_cnt_from_seq(seq, start, stop):
    n = stop - start
    cnt = [0] * n
    for i in range(n):
        new_index = seq[i] - start
        if new_index < n:
            cnt[new_index] += 1
    return cnt
