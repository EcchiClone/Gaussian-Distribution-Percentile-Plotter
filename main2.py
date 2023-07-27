# 표준편차 대신, '평균이 100이고, 80에서 120 사이에 95%의 영역이 포함된다' 처럼
# 평균(100) 과 범위(80,120) 그리고 영역(95) 을 입력하여 출력을 할 수는 없을까?

# 네, 가능합니다. 이 경우, 우리는 분포의 범위를 알고 있으므로, 이를 사용하여 표준편차를 계산할 수 있습니다. 정규 분포에서 대략 95%의 데이터는 평균에서 ±2 표준편차 범위 내에 있습니다. 따라서 범위의 절반을 2로 나누면 표준편차를 얻을 수 있습니다.
# 이를 반영하여 코드를 다음과 같이 수정하겠습니다.

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def plot_gaussian(mu, sigma, percentile):
    # percentile 값을 확률로 변환
    p = percentile / 100.0
    
    # 정규 분포를 따르는 임의의 데이터 생성
    x = np.linspace(mu - 3.5*sigma, mu + 3.5*sigma, 100)
    y = norm.pdf(x, mu, sigma)

    # 분위수 계산
    low, high = norm.ppf([0.5 - p/2, 0.5 + p/2], loc=mu, scale=sigma)
    
    # 전체 분포 그래프 그리기
    plt.plot(x, y, label='Normal Distribution')

    # n% 분포 그리기
    x_fill = np.linspace(low, high, 100)
    y_fill = norm.pdf(x_fill, mu, sigma)
    plt.fill_between(x_fill, y_fill, color='red', alpha=0.5, label=f'{percentile}% of Distribution')

    plt.legend()
    plt.grid(True)
    plt.title('Gaussian Distribution')
    plt.show()
    
def plot_gaussian_range(mean, range_start, range_end, percentile):
    # 표준편차 계산 (범위는 평균에서 ±2 표준편차이므로)
    sigma = (range_end - mean) / 2

    # 나머지는 이전과 동일
    plot_gaussian(mean, sigma, percentile)

# 예시
plot_gaussian_range(mean=100, range_start=80, range_end=120, percentile=50)


# 이 함수는 평균, 범위의 시작과 끝, 그리고 분포에서 차지하는 비율을 입력으로 받아 정규 분포를 그래프로 표시합니다. 이 경우, 평균이 100이고, 범위가 80에서 120인 정규 분포에서 95%의 데이터를 빨간색으로 표시합니다.