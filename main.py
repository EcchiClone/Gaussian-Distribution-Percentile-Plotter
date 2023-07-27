# 80에서 120까지 전체의 n%를 차지하고 있는 가우스 분포의 그래프를 플롯하는 파이썬 프로그램을 작성해줘.
# 입력값은 n이야

# 네, 알겠습니다. 가우스 분포 (또는 정규 분포)에 대해 이야기하고 있으므로, 먼저 분포의 평균과 표준편차를 알아야 합니다. 그런 다음, scipy의 norm.ppf 함수를 사용하여 n% 분위수를 찾을 수 있습니다. 이것은 분포의 어떤 부분이 n%를 차지하는지 알려주는 값입니다.
# 예를 들어, 평균이 100이고 표준편차가 10인 정규 분포를 가정해 봅시다. 그러면 80에서 120까지의 범위는 분포의 대략적인 95%를 차지합니다.
# 그러나 이 정보 없이, 사용자가 원하는 n%를 찾는 것은 불가능합니다. 평균과 표준편차를 알려주시겠습니까? 아니면 특정한 가정을 하고 진행하시겠습니까?

# 평균과 표준편차도 사용자가 입력하도록 할게.
# 그리고 마지막에는 입력값의 예시와 함께 출력의 예시도 보여주면 좋겠어

# 네, 알겠습니다. 평균, 표준편차, 그리고 분포에서 차지하는 비율을 입력으로 받는 파이썬 함수를 작성해 보겠습니다. 또한 matplotlib 라이브러리를 사용하여 분포 그래프를 그리는 코드도 포함하겠습니다.

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

# 예시
plot_gaussian(mu=100, sigma=10, percentile=80)

# 이 코드를 실행하면 평균이 100이고 표준편차가 10인 정규 분포를 그리고, 이 분포에서 95%를 차지하는 부분을 빨간색으로 채워서 표시합니다.
