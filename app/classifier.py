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
