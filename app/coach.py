import os
import timeit
import datetime
import numpy as np
import pandas as pd
from catboost import Pool, CatBoostClassifier, cv
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, cohen_kappa_score
from imblearn.over_sampling import SMOTE

class Coach(object):
    __file = pd.read_csv('../dataset/dataset.csv')
    __dataset = pd.DataFrame()

    @property
    def dataset(self):
        return self.__dataset
        
    @dataset.setter
    def dataset(self, dataset):
        self.__dataset = dataset

    def setDataset(self):
        try:
            group = self.__file.groupby(['radiantClass']).count()
            where = group.where(group > 10, 0)
            classes = where[where['id'] > 10].index

            database = pd.DataFrame()

            for _class in classes:
                for row in self.__file.itertuples():
                    if row[6] == _class:
                        database = database.append(self.__file.loc[row[0]])

            self.dataset = database
            return "Success"
        except Exception as e:
            return "Exception: "+e

    def trainNeuralNetwork(self, solver, activation_method):
        x = self.dataset.drop(['id','radiantClass'], axis=1)
        y = self.dataset['radiantClass']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.20, random_state=0, stratify=y)
        
        model = MLPClassifier(hidden_layer_sizes=(100,100,100), activation=activation_method, max_iter=10000, alpha=0.0001,
        solver=solver, verbose=False, tol=0.000000001)

        # smote = SMOTE('minority')
        # x_sm, y_sm = smote.fit_sample(x_train, y_train)

        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        
        accuracy = accuracy_score(y_test, pred, normalize=True)
        f1score = f1_score(y_test, pred, average=None)
        kappa = cohen_kappa_score(y_test, pred)
        cm = confusion_matrix(y_test, pred)

        print('Accuracy: ', accuracy)
        print('F1 score: ', f1score)
        print(cm)

        return [accuracy, f1score, kappa, cm, y_test, pred]

    def trainDecisionTree(self):
        x = self.dataset.drop(['id','radiantClass'], axis=1)
        y = self.dataset['radiantClass']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.20, random_state=0, stratify=y)
        
        model = CatBoostClassifier(iterations=1000,learning_rate=1,depth=2,loss_function='MultiClass',eval_metric='Accuracy')

        # smote = SMOTE('minority')
        # x_sm, y_sm = smote.fit_sample(x_train, y_train)

        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        
        accuracy = accuracy_score(y_test, pred, normalize=True)
        f1score = f1_score(y_test, pred, average=None)
        kappa = cohen_kappa_score(y_test, pred)
        cm = confusion_matrix(y_test, pred)

        print('Accuracy: ', accuracy)
        print('F1 score: ', f1score)
        print(cm)

        return [accuracy, f1score, kappa, cm, y_test, pred]

        # sns.heatmap(cm, center=True)
        # plt.show()


if __name__ == "__main__":
    coach = Coach()
    print(coach.setDataset())

    initialTime = timeit.default_timer()
    # response = coach.trainNeuralNetwork('sgd', 'identity')
    response = coach.trainDecisionTree()
    finalTime = timeit.default_timer() 

    print('Execution time: ', finalTime-initialTime)

    # treino = Treinador()
    # treino.setDataset()

    # date = datetime.datetime.now().strftime('%d%m%Y_%H%M%S')
    # fileReturn = open('../dataset/response_'+date+'.txt', 'w')     

    # inicio = timeit.default_timer()
    # response = treino.treinar('lbfgs', 'identity')
    # fim = timeit.default_timer()

    # fileReturn.write('Métricas Resultantes dos Testes com Sklearn MLPClassifier\n\n')
    # fileReturn.write('Obs.: Neste teste não utilizei aumento de classes minoritárias\n\n')
    # fileReturn.write('Execution time: ')
    # fileReturn.write(str(fim-inicio))
    # fileReturn.write('\n\n')

    # fileReturn.write('Acuracia: ')
    # fileReturn.write(str(response[0]))
    # fileReturn.write('\n\n')

    # fileReturn.write('F1 Score*: ')
    # fileReturn.write(str(response[1]))
    # fileReturn.write('\n* Note que cada um dos valores espressos nesta métrica se referem a uma classe do conjunto\n\n')

    # fileReturn.write('Kappa: ')
    # fileReturn.write(str(response[2]))
    # fileReturn.write('\n\n')

    # fileReturn.write('Matriz de confusão:\n')
    # fileReturn.write(str(response[3]))
    # fileReturn.write('\n\n')
    
    # fileReturn.write('----------------------------------------\n\n')
    # fileReturn.write('TESTE, PREDITO\n')
    # i = 0
    # for y_test in response[4]:
    #     fileReturn.write(str(y_test))
    #     fileReturn.write(',  ')
    #     fileReturn.write(str(response[5][i]))
    #     fileReturn.write('\n')
    #     i += 1

    # fileReturn.close()

    # print('Execution time: ', fim-inicio)
