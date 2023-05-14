# Q1
# 2022년 1월~12월 각 지역별 월 평균 기온의 추이를 시각화하고
# 각 월별로 전국 평균대비 얼마만큼 기온의 차이가 나는지 수치 제시하여 분석하시오
# 전국, 서울, 대전, 부산, 제주
# 2022년 1월~12월 월평균 기온을 하나의 그래프로 시각화
# 전국대비 더 더운지역, 더 추운지역에 대한 분석 결과 설명

import csv
import numpy as np
import matplotlib.pyplot as plt


def main():
    f_all = open('all.csv')
    f_seoul = open('seoul.csv')
    f_daejeon = open('daejeon.csv')
    f_busan = open('busan.csv')
    f_jeju = open('jeju.csv')

    temp_all = temp(f_all)
    temp_seoul = temp(f_seoul)
    temp_daejeon = temp(f_daejeon)
    temp_busan = temp(f_busan)
    temp_jeju = temp(f_jeju)

    var_seoul = analysis(temp_all, temp_seoul)
    var_daejeon = analysis(temp_all, temp_daejeon)
    var_busan = analysis(temp_all, temp_busan)
    var_jeju = analysis(temp_all, temp_jeju)

    print('전국과 서울의 월 평균 온도차:', var_seoul)
    print('전국과 대전의 월 평균 온도차:', var_daejeon)
    print('전국과 부산의 월 평균 온도차:', var_busan)    
    print('전국과 제주의 월 평균 온도차:', var_jeju)

    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    fig, ax = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(10,6))
    plt.rc('font', family='Malgun Gothic')
    
    ax[0,0].plot(x, temp_all, color='gray', label='전국', marker='o')
    ax[0,0].plot(x, temp_seoul, color='yellowgreen', label='서울', marker='o')

    ax[0,1].plot(x, temp_all, color='gray', label='전국', marker='o')
    ax[0,1].plot(x, temp_daejeon, color='mediumpurple', label='대전', marker='o')
    
    ax[1,0].plot(x, temp_all, color='gray', label='전국', marker='o')
    ax[1,0].plot(x, temp_busan, color='cornflowerblue', label='부산', marker='o')
    
    ax[1,1].plot(x, temp_all, color='gray', label='전국', marker='o')
    ax[1,1].plot(x, temp_jeju, color='coral', label='제주', marker='o')

    for i in ax.flat:
        i.set_xlim(0,13)       # x축 범위 설정
        i.legend()             # 범례 추가
        i.grid(linestyle=':')  # 격자 추가
        i.set_xlabel('month')
        i.set_ylabel('temperature')  # label 추가

    for i in ax.flat:
        i.label_outer()  # 축 바깥쪽에 표시 

    fig.suptitle('2022년 지역별 월 평균 기온')
    fig.tight_layout()    # subplot 간격 조정
    
    plt.show()

def temp(region):
    list = []
    data = csv.reader(region)
    header = next(data)

    for row in data:
        if row[-1] != '':
            list.append(float(row[2]))
    
    return list

def analysis(standard, region):
    list = []
    for a, b in zip(standard, region):
        list.append(float(a-b))

    return np.round(list,1)
    
if __name__ == '__main__':
    main()
