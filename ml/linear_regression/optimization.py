import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    boston = pd.read_csv('../../files/Boston_house.csv')
    X = boston[['LSTAT']]
    y = boston[['Target']]

    # 데이터를 학습 데이터와 평가데이터로 나누기.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    plt.scatter(X_train, y_train)
    plt.show()

    plt.scatter(X_test, y_test)
    plt.show()

    # numpy 라이브러리 활용해 최적의 선형회기 모델 찾기
    # 최적 모델은 모든 데이터에 대해 실제값과 예측값의 차이가 제일 적은 모델
    # 선형 회귀 모델은 MSE 손실을 최소화 하도록 학습
    # 경사 하강법 계산

    reg = LinearRegression()

    # train 데이터로 학습
    reg.fit(X_train, y_train)

    # 학습된 모델로 예측
    y_pred = reg.predict(X_test)

    plt.scatter(y_test, y_pred, alpha=0.4)
    plt.xlabel('Actial')
    plt.ylabel('Predicted')
    plt.title('LINEAR REGRESSION')
    plt.show()
