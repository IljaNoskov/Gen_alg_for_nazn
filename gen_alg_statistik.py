import random
import itertools
import time


def matrix_from_file(file_name: object) -> object:
    f = open(file_name)
    matrix = []
    for line in f:
        matrix.append([])
        for num in line.split():
            matrix[-1].append(int(num))
    f.close()
    return matrix


def print_matrix(matrix) -> object:
    for line in matrix:
        print(*line)


def prod_pereb(a):
    comb1 = list(range(a))


def comb_sum(matrix, combination):
    sum_comb = 0
    for index in range(len(matrix)):
        sum_comb += matrix[index][combination[index]]
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
                elif (new_zn == comb2[index]) and comb1[index] not in not_in_posl:
                    not_in_posl.append(comb1[index])

        elif comb1[index] in comb and comb2[index] in comb:
            new_zn = random.choice(not_in_posl)
            not_in_posl.remove(new_zn)

        elif comb1[index] in comb:
            new_zn = comb2[index]
            if new_zn in not_in_posl:
                not_in_posl.remove(new_zn)

        else:
            new_zn = comb1[index]
            if new_zn in not_in_posl:
                not_in_posl.remove(new_zn)

        comb.append(new_zn)
        assert is_norm_comb(comb), comb
    return comb


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
            gen = gen[0:-(child_num + mut_num)]
            real_child_num = 0
            for comb1_ind in range(num_of_best_comb(child_num)):
                if real_child_num == child_num:
                    break
                for comb2_ind in range(comb1_ind + 1, num_of_best_comb(child_num) + 2):
                    assert comb2_ind < len(gen), (len(gen), comb2_ind, child_num, mut_num)
                    gen.append(make_child(gen[comb1_ind][1], gen[comb2_ind][1]))
                    gen[-1] = [comb_sum(matrix, gen[-1]), gen[-1], 'make_child']
                    real_child_num += 1
                    if real_child_num == child_num:
                        break
            assert real_child_num == child_num, (real_child_num, child_num)

            for comb in range(mut_num):
                gen.append(mutation(gen[comb][1]))
                gen[-1] = [comb_sum(matrix, gen[-1]), gen[-1], 'mutation']
        gen = sorted(gen, reverse=True)
    return gen[0]


def num_of_best_comb(n):
    # n=(x*(x+1))/2
    # x*x + x - 2n = 0
    D = 1 + 8 * n
    return round((-1+pow(D, 1/2))/2)


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


child_per = 20
mutatiom_per = 5


def statistic(matrix, pokol_num, pokol_size, sr):
    sr_rez = 0
    s_time = time.time()
    for _ in range(sr):
        sr_rez += gen_alg(matrix, pokol_num, pokol_size, round(pokol_size * child_per / 100), round(mutatiom_per * pokol_size / 100))[0]
    e_time = time.time()
    sr_time = (e_time - s_time) / sr
    sr_rez = sr_rez/sr
    return sr_rez, sr_time


for i in range(3, 21):
    file_name = "matrix" + str(i) + ".txt"
    mat = matrix_from_file(file_name)
    # Размер матрицы
    matrix_size = i
    if i <= 10:
        start_time = time.time()
        if i < 8:
            for iter in range(199):
                t = pereb_reh(mat)[0]
            perebor_num = pereb_reh(mat)[0]
            end_time = time.time()
            perebor_time = (end_time - start_time)/200
        else:
            perebor_num = pereb_reh(mat)[0]
            end_time = time.time()
            perebor_time = end_time-start_time
    else:
        perebor_time = 0
        perebor_num = 10**6
    if i == 3:
        file = open("stat.txt", "w")
    else:
        file = open("stat.txt", "a")

    # среднее значение генетического алгоритма в зависимости от размеров поколения их количества
    # , а также время выполнения алгоритма

    print(matrix_size, "Старт")
    # Перебираем одновременно количество и размер поколения
    for p_size, p_num in zip(range(100, 1001, 100), range(100, 1001, 100)):
        st = statistic(mat, p_num, p_size, 20)
        string = f"{matrix_size} {perebor_num} {perebor_time} {p_size} {p_num} {st[0]} {st[1]}\n"
        file.write(string)
    print(matrix_size, "1")

    p_size = 100
    for p_num in range(100, 1001, 100):
        st = statistic(mat, p_num, p_size, 20)
        string = f"{matrix_size} {perebor_num} {perebor_time} {p_size} {p_num} {st[0]} {st[1]}\n"
        file.write(string)
    print(matrix_size, "2")

    p_num = 100
    for p_size in range(100, 1001, 100):
        st = statistic(mat, p_num, p_size, 20)
        string = f"{matrix_size} {perebor_num} {perebor_time} {p_size} {p_num} {st[0]} {st[1]}\n"
        file.write(string)
    print(matrix_size, "Конец")
    print(matrix_size)
    
file.close()

