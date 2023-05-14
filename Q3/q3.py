# Q3
# 제주도에는 여성의 비율이 더 높다는 속설이 있다. 이 속설이 맞는지 시각화 분석
# 제주특별자치도를 기준으로 데이터 획득
# 데이터 시각화 후 분석결과 설명
# 단, 연령대별로 비교할 필요 없고, 성별로만 비교
# 단, 한 해에 대해서만 비교하거나, 여러 해를 통합하여, 단 한번만 비교 시 증명 불충분으로 간주

import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def main():
    f = open('q3.csv', 'r')
    data = csv.reader(f)
    header = next(data)
    jeju_data = next(data)

    male=[]
    female=[]
    total_num = []
    count=0

    for data in header:
        if '총' in data:
            total_num.append(count)
            count += 1
        else:
            count += 1


    for i in range(0, len(total_num), 2):
        male.append(int(jeju_data[total_num[i]]))
    for j in range(1, len(total_num), 2):
        female.append(int(jeju_data[total_num[j]]))

    print('연도별 남자 총 인구 수:', male)
    print('연도별 여자 총 인구 수:', female)

    font_path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    x = [2018, 2019, 2020, 2021, 2022]

    bar_width=0.4

    index = np.arange(len(x))
    
    plt.bar(index, male, width=bar_width, alpha=0.5, label='남자', color='royalblue', align='edge')
    plt.bar(index+bar_width, female, width=bar_width, alpha=0.5, label='여자', color='crimson', align='edge')

    plt.title('제주도 성별 인구수 비교')
    plt.xticks(index+bar_width, x)
    plt.xlabel('연도')
    plt.ylabel('인구 수')
    plt.legend()
    plt.grid(linestyle=':')
    plt.show()
    

if __name__ == '__main__':
    main()
