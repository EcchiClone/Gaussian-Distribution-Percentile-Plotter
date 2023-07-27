# 이게 아니야.
# 예를 들어 mean=100, range_start=80, range_end=120, percentile=50 을 입력하였을 때
# 80 부터 120 까지의 범위가 전체의 50%를 차지하고 있어야 해.

# 아, 이해했습니다. 사용자가 제공하는 범위 내에서 분포의 특정 백분율을 계산하려는 것이군요.
# 이 경우, 범위 내에서 특정 백분율이 되도록 정규 분포의 표준편차를 조정해야 합니다. 그러기 위해 우리는 분포의 누적 분포 함수 (CDF)를 사용할 수 있습니다. 이것은 분포 내의 특정 값 이하의 확률을 제공합니다.
# 다음은 이를 수행하는 파이썬 코드입니다:

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


from scipy.optimize import fsolve

def find_sigma(mu, low, high, target_percentile):
    target_prob = target_percentile / 100.0

    # 표준편차를 찾기 위한 방정식 정의
    def equation(sigma):
        return (norm.cdf(high, loc=mu, scale=sigma) - norm.cdf(low, loc=mu, scale=sigma)) - target_prob

    # scipy의 fsolve 함수를 사용하여 방정식 해결
    sigma = fsolve(equation, x0=1)[0]

    return sigma

def plot_gaussian_target_percentile(mu, low, high, percentile):
    sigma = find_sigma(mu, low, high, percentile)
    plot_gaussian(mu, sigma, percentile)

# 예시
plot_gaussian_target_percentile(mu=100, low=98, high=102, percentile=99)


# 이 코드는 사용자가 제공한 범위 내에서 원하는 백분율을 차지하도록 정규 분포의 표준편차를 계산하고, 해당 분포를 그래프로 그립니다. 이 경우, 평균이 100이고 80에서 120 사이의 범위가 분포의 50%를 차지하도록 하는 정규 분포를 그립니다.

# (내가 percentile=50으로 정규분포와는 맞지 않는 예시를 들어 오류 발생했음. 이후 대화 통해 알게되어 코드가 제대로 되었다는 것을 확인.)