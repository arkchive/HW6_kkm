# Q4
# 출근 시간대 사람들이 가장 많이 타고 내리는 역은 어디일까?
# 2023년 3월 교통카드 통계자료 사용
# 지하철 시간대별 이용현황 sheet를 사용
# 출근시간 오전 7시~9시
# 출근시간 최대 승차역 30개 추출, 승객수 정렬, 막대그래프 표현
# 출근시간 최대 하차역 30개 추출, 승객수 정렬, 막대그래프 표현
# 출근시간 최대 승하차역 30개 추출, 승객수 정렬, 막대그래프 표현
# 데이터 시각화를 통한 분석 결과 설명

import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

def main():
    f = open('q4.csv', 'r', encoding='utf-8')
    data = csv.reader(f)
    header = next(data)

    dic = {}
    for row in data:
        if row[-1] != '':
            if row[3] in dic:
                dic[row[3]][0] += int(row[10]) + int(row[12])
                dic[row[3]][1] += int(row[11]) + int(row[13])
                dic[row[3]][2] += int(row[10]) + int(row[11]) + int(row[12]) + int(row[13])
            else:
                dic_val = []
                dic_val.append(int(row[10]) + int(row[12]))
                dic_val.append(int(row[11]) + int(row[13]))
                dic_val.append(int(row[10]) + int(row[11]) + int(row[12]) + int(row[13]))
                dic[row[3]] = dic_val

    get_on_data = {}
    get_off_data = {}
    sum_data = {}
    
    for key, value in dic.items():
        get_on_data[key] = value[0]
        get_off_data[key] = value[1]
        sum_data[key] = value[2]

    top30_get_on = get_sorted_data(get_on_data)
    top30_get_off = get_sorted_data(get_off_data)
    top30_sum = get_sorted_data(sum_data)

    print('최대 승차역 30개 정렬:', top30_get_on)
    print('최대 하차역 30개 정렬:', top30_get_off)
    print('최대 승하차역 30개 정렬:', top30_sum)

    font_path = 'C:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

    fig, (ax1,ax2,ax3) = plt.subplots(3,1, figsize=(7,8), tight_layout=True)

    ax1.bar(list(top30_get_on.keys()), list(top30_get_on.values()), color='midnightblue', alpha=0.7)
    ax1.set_title('출근시간 최대 승차역 Top 30', fontsize=10)
    ax1.set_xticks(range(len(top30_get_on)))
    
    ax2.bar(list(top30_get_off.keys()), list(top30_get_off.values()), color='midnightblue', alpha=0.7)
    ax2.set_title('출근시간 최대 하차역 Top 30', fontsize=10)
    ax2.set_xticks(range(len(top30_get_off)))
    
    ax3.bar(list(top30_sum.keys()), list(top30_sum.values()), color='midnightblue', alpha=0.7)
    ax3.set_title('출근시간 최대 승하차역 Top 30', fontsize=10)
    ax3.set_xticks(range(len(top30_sum)))


    for i in (ax1,ax2,ax3):
        i.grid(linestyle=':')
        i.set_xticklabels(i.get_xticklabels(), rotation=90, ha='center', fontsize=7)
        i.set_yticks(i.get_yticks())
        i.set_yticklabels([int(label) for label in i.get_yticks()], fontsize=7)


    plt.show()
        
def get_sorted_data(data):
    sorted_data = sorted(data.items(), key=lambda x:x[1], reverse=True)
    return dict(sorted_data[:30])


if __name__ == '__main__':
    main()
