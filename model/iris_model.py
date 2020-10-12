import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from model.perceptron import Perceptron
from model.adaline import AdalineGD


class IrisModel:
    def __init__(self):
        self.iris = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None)
        print(self.iris.head())
        print('----------------------')
        print(self.iris.tail)
        print('----------------------')
        print(self.iris.columns)
        '''
        [150 rows x 5 columns]>
        ----------------------
        Int64Index([0, 1, 2, 3, 4], dtype='int64')
        '''

        # Iris-setosa 와 versicolor 선택 (MCP 는 이진분류만 할 수 있다)
        t = self.iris.iloc[0:100,4].values
        self.y = np.where(t == 'Iris-setosa', -1, 1)
        # 꽃받침 길이, 꽃잎 추출
        self.X = self.iris.iloc[0:100, [0,2]].values
        self.clf = Perceptron(eta = 0.1, n_iter=10)

    def get_iris(self):
        return self.iris

    def get_X(self):
        return self.X

    def get_y(self):
        return self.y

    def draw_scatter(self):
        X = self.X
        plt.scatter(X[:50, 0], X[:50, 1], color = 'red', marker='o', label = 'setosa')
        plt.scatter(X[50:100, 0], X[50:100, 1], color = 'blue', marker='x', label = 'versicolor')
        plt.xlabel('sepal length[cm]')
        plt.ylabel('petal length[cm]')
        plt.legend(loc = 'upper left')
        plt.show()

    def draw_errors(self):
        X = self.X
        y = self.y
        self.clf.fit(X, y)
        plt.plot(range(1, len(self.clf.errors_) + 1), self.clf.errors_, marker='o')
        plt.xlabel('Epoch')
        plt.ylabel('Number of Errors')
        plt.show()

    def plot_decision_regions(self, X, y, classifier, resolution=0.02):
    
        # 마커와 컬러맵을 설정합니다
        markers = ('s', 'x', 'o', '^', 'v')
        colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])

        # 결정 경계를 그립니다
        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        """
        numpy 모듈의 arrange 함수는 반열린구간 [start, stop) 에서
        step 의 크기만큼 일정하게 떨어져 있는 숫자들을
        array 형태로 반환하는 함수

        meshgrid 함수는 사각형 영역을 구성하는
        가로축의 점들과 세로축의 점을
        나타내는 두 벡터를 인수로 받아서
        이 사각형 영역을 이루는 조합을 출력한다.
        결과는 그리드 포인트의 x 값만을 표시하는 행렬과
        y 값만을 표시하는 행렬 두 개로 분리하여 출력한다
        """
        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                            np.arange(x2_min, x2_max, resolution))
        Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        Z = Z.reshape(xx1.shape)
        plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max())

        # 샘플의 산점도를 그립니다
        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(x=X[y == cl, 0], 
                        y=X[y == cl, 1],
                        alpha=0.8, 
                        c=colors[idx],
                        marker=markers[idx], 
                        label=cl, 
                        edgecolor='black')

        plot_decision_regions(X, y, classifier=self.clf)
        plt.xlabel('sepal length [cm]')
        plt.ylabel('petal length [cm]')
        plt.legend(loc='upper left')

        plt.show()


    def draw_adaline_graph(self):
        X = self.X
        y = self.y
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))

        ada1 = AdalineGD(n_iter=10, eta=0.01).fit(X, y)
        ax[0].plot(range(1, len(ada1.cost_) + 1), np.log10(ada1.cost_), marker='o')
        ax[0].set_xlabel('Epochs')
        ax[0].set_ylabel('log(Sum-squared-error)')
        ax[0].set_title('Adaline - Learning rate 0.01')

        ada2 = AdalineGD(n_iter=10, eta=0.0001).fit(X, y)
        ax[1].plot(range(1, len(ada2.cost_) + 1), ada2.cost_, marker='o')
        ax[1].set_xlabel('Epochs')
        ax[1].set_ylabel('Sum-squared-error')
        ax[1].set_title('Adaline - Learning rate 0.0001')

        plt.show()

    def draw_adaline_gd_graph(self):
        # 특성을 표준화합니다.
        X = self.X
        y = self.y
        X_std = np.copy(X)
        X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
        X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()


        ada = AdalineGD(n_iter=15, eta=0.01)
        ada.fit(X_std, y)

        plot_decision_regions(X_std, y, classifier=ada)
        plt.title('Adaline - Gradient Descent')
        plt.xlabel('sepal length [standardized]')
        plt.ylabel('petal length [standardized]')
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.show()

        plt.plot(range(1, len(ada.cost_) + 1), ada.cost_, marker='o')
        plt.xlabel('Epochs')
        plt.ylabel('Sum-squared-error')

        plt.tight_layout()
        plt.show()


    






    