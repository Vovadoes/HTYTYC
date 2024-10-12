import math
# from pprint import pprint
from typing import List
from scipy.stats import t


# from Charts import *

# from scipy.stats import t

# CONST
# None

class Calculation:
    def __init__(self, name, alpha, n, lst1: list[list[int]]):
        d_med = 0
        summ_d_d = 0
        summ_d_d_2 = 0
        for i in range(n):
            lst1[i].append(lst1[i][2] - lst1[i][1])
            d_med += lst1[i][3]
        d_med = d_med / n
        for i in range(n):
            lst1[i].append(lst1[i][3] - d_med)
            lst1[i].append(lst1[i][4] ** 2)
            summ_d_d_2 += lst1[i][5]
            summ_d_d += lst1[i][4]
        # pprint(lst1)

        S_m_d = math.sqrt(summ_d_d_2 / (n * (n - 1)))

        t_see = d_med / S_m_d

        t_crit = t.ppf(1 - alpha / 2, n - 1)

        self.d_med = d_med
        self.summ_d_d_2 = summ_d_d_2
        self.summ_d_d = summ_d_d
        self.S_m_d = S_m_d
        self.t_see = t_see
        self.t_crit = t_crit
        self.lst = lst1


if __name__ == "__main__":
    name = "озимая пшеница"
    alpha = 0.05
    n = 7
    lst1 = [[2017, 46, 52], [2018, 48, 53], [2019, 46, 45], [2020, 51, 56], [2021, 52, 58], [2022, 48, 55],
            [2023, 52, 59]]
    # pprint(lst1)
    calculation = Calculation(name, alpha, n, lst1)
    print(calculation)
    # ChartLinePLT(calculation.chart_v_y_data)
    # plt.legend()
    # plt.show()
