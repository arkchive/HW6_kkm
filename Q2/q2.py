# Q2
# 주사위 시뮬레이션 결과를 시각화하고 분석하시오
# 1~6 사이의 랜덤 숫자를 만들어, 다음 횟수만큼 시행하시오
# 100번 시행, 1000번 시행, 10000번 시행, 100000번 시행
# 시행 결과를 하나의 csv 파일로 저장하시오
# 각 시행별 데이터를 읽어와 1~6 숫자에 대해 히스토그램 시각화 (그래프 4개)
# 주사위 시뮬레이션 결과에 대한 분석결과 설명

import csv
import random
import numpy as np
import matplotlib.pyplot as plt

def main():
    f = open('q2.csv', 'w', newline='')
    num_rolls_list = [100, 1000, 10000, 100000]
    header = ['시행횟수',1, 2, 3, 4, 5, 6]
    writer = csv.DictWriter(f, header)
    writer.writeheader()
    total = []

    for num_rolls in num_rolls_list:
        results = roll_dice(num_rolls)
        total.append(results)
        counts = count_dice_results(results)
        save_results(f, num_rolls, counts, writer)

    f.close()

    f = open('q2.csv', 'r')
    data = csv.reader(f)
    header = next(data)
    roll_100 = next(data)
    roll_1000 = next(data)
    roll_10000 = next(data)
    roll_100000 = next(data)


    fig, ax = plt.subplots(2, 2, sharex=True, figsize=(10,6), tight_layout=True)

    ax[0,0].hist(total[0], bins=6, color='seashell', edgecolor='salmon',
                 rwidth=0.8, linewidth=1.5, alpha=0.8)
    ax[0,0].set_title('roll 100times')
    ax[0,1].hist(total[1], bins=6, color='seashell', edgecolor='salmon',
                 rwidth=0.8, linewidth=1.5, alpha=0.8)
    ax[0,1].set_title('roll 1000times')
    ax[1,0].hist(total[2], bins=6, color='seashell', edgecolor='salmon',
                 rwidth=0.8, linewidth=1.5, alpha=0.8)
    ax[1,0].set_title('roll 10000times')
    ax[1,1].hist(total[3], bins=6, color='seashell', edgecolor='salmon',
                 rwidth=0.8, linewidth=1.5, alpha=0.8)
    ax[1,1].set_title('roll 100000times')

    for i in ax.flat:
        i.set_xlabel('number of dice')
        i.set_ylabel('count')
        i.grid(linestyle=':')

    for i in ax.flat:
        i.label_outer()

    fig.suptitle('Dice Simulation Analysis Result')
    plt.show()
                  
    
def roll_dice(num_rolls):
    results = []
    for i in range(num_rolls):
        roll = random.randint(1, 6)
        results.append(roll)
    return results

def count_dice_results(results):
    counts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in results:
        counts[i] += 1
    return counts

def save_results(f, num_rolls, counts, writer):
    writer.writerow({'시행횟수':num_rolls, 1:counts[1],
                     2:counts[2], 3:counts[3], 4:counts[4],
                     5:counts[5], 6:counts[6]})

if __name__ == '__main__':
    main()
