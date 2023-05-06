# План работы:
# 1) Пишу функцию считывания матрицы из файла +
# 2) Функцию решения за O(M!) - где M -размер матрицы +
# 3) Пишу функцию оценки той или иной комбинации +- (использовать comb_sum, O(n))
# 4) Функцию создания ребёнка из родителей +
# 5) Запускаю весь алгоритм +
# 6) Пишу функцию для мутации
# 7) Пишу нормальный выбор родителей для детей
# 8) Редачу генетику так, чтобы можно было выбирать % детей и % мутаций
# 9) Делаю GUI
# 9.1) Возмодность задать матрицу, параметры гинетики и галачку на решение перебором
# 10) Визуал с графиками

import random
import itertools
import time


def matrix_from_file(file_name):
    f = open(file_name)
    matrix = []
    for line in f:
        matrix.append([])
        for num in line.split():
            matrix[-1].append(int(num))
    return matrix


def print_matrix(matrix):
    for line in matrix:
        print(*line)


def prod_pereb(a):
    comb1 = list(range(a))


def comb_sum(matrix, combination):
    sum_comb = 0
    for i in range(len(matrix)):
        sum_comb += matrix[i][combination[i]]
    return sum_comb


def pereb_reh(matrix):
    a = len(matrix)
    massiv = list(range(a))
    combs = itertools.permutations(massiv)
    max_sum = 0
    max_comb = []
    for comb in combs:
        cur_sum = comb_sum(matrix, list(comb))
        if max_sum < cur_sum:
            max_sum = cur_sum
            max_comb = list(comb)
    return max_sum, max_comb


def make_child(comb1, comb2):
    comb = []
    not_in_posl = []
    for index in range(len(comb1)):
        if comb1[index] not in comb and comb2[index] not in comb:
            new_zn = random.choice([comb1[index], comb2[index]])
            if new_zn in not_in_posl:
                not_in_posl.remove(new_zn)

            if comb1[index] != comb2[index]:
                if (new_zn == comb1[index]) and comb2[index] not in not_in_posl:
                    not_in_posl.append(comb2[index])
                    assert comb2[index] not in comb, (new_zn, comb2[index], comb)
                elif (new_zn == comb2[index]) and comb1[index] not in not_in_posl:
                    not_in_posl.append(comb1[index])
                    assert comb1[index] not in comb, (new_zn, comb1[index], comb)
            assert new_zn not in comb, "1"

        elif comb1[index] in comb and comb2[index] in comb:
            new_zn = random.choice(not_in_posl)
            assert new_zn not in comb, ("2", comb, not_in_posl, new_zn)
            not_in_posl.remove(new_zn)

        elif comb1[index] in comb:
            new_zn = comb2[index]
            if new_zn in not_in_posl:
                not_in_posl.remove(new_zn)
            assert new_zn not in comb, "3"

        else:
            new_zn = comb1[index]
            if new_zn in not_in_posl:
                not_in_posl.remove(new_zn)
            assert new_zn not in comb, "4"

        comb.append(new_zn)
        assert is_norm_comb(comb), comb
    return comb
    # Мне всего 19, так что я
    # pass


def is_norm_comb(comb):
    for index in range(len(comb)):
        if comb[index] in [*comb[0:index], *comb[index + 1:-1]]:
            return False
    return True


def make_random_matrix(a):
    matrix = []
    for i in range(a):
        matrix.append([])
        for j in range(a):
            matrix[i].append(random.randint(0, 100))
    return matrix


def random_gen(glen):
    k = range(glen)
    return random.sample(k, glen)


def gen_alg(matrix, pokol_num, gen_size, child_num, mut_num):
    gen = []
    for cur_pokol in range(pokol_num):
        if cur_pokol == 0:
            for j in range(gen_size):
                gen.append(random_gen(len(matrix)))
                gen[j] = [comb_sum(matrix, gen[j]), gen[j], 'rand_gen']
        else:
            gen = gen[0:-(child_num+mut_num)]
            for comb in range(child_num):
                # assert is_norm_comb(gen[0][1]) and is_norm_comb(gen[comb][1]), (gen[0], " ", gen[comb])
                gen.append(make_child(gen[0][1], gen[comb][1]))
                gen[-1] = [comb_sum(matrix, gen[-1]), gen[-1], 'make_ch']

            for comb in range(mut_num):
                gen.append(mutation(gen[comb][1]))
                gen[-1] = [comb_sum(matrix, gen[-1]), gen[-1], 'mutation']
        gen = sorted(gen, reverse=True)
    return gen[0]


def mutation(comb):
    new_comb = []
    not_in_comb = list(range(len(comb)))
    for index in range(len(comb)):
        if random.choice([True, False]):
            if comb[index] not in new_comb:
                new_comb.append(comb[index])
            else:
                new_comb.append(random.choice(not_in_comb))

        else:
            new_comb.append(random.choice(not_in_comb))
        not_in_comb.remove(new_comb[-1])
        assert is_norm_comb(new_comb), new_comb
    return new_comb


# mat = matrix_from_file("matrix")
# print_matrix(mat)
#
# print(pereb_reh(mat))
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 1]
#
# print(make_child(list1, list2))


mat = make_random_matrix(5)

# print_matrix(mat)
# print(pereb_reh(mat))


per_rez = pereb_reh(mat)[0]
print(per_rez)
for i in range(10, 1000, 100):
    start_time = time.time()
    cur_rez = gen_alg(mat, i, i, i // 10, i//10)
    end_time = time.time()
    rez = end_time - start_time
    print(i, rez, cur_rez[0], cur_rez[2])
