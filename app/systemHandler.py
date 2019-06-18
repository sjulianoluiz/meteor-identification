import os
import csv

class SystemHandler(object):
    __directories = []
    __classified = []
    __notClassified = []

    @property
    def directories(self):
        return sorted(self.__directories)

    @directories.setter
    def directories(self, dir):
        self.__directories.append(dir[:])

    @property
    def classified(self):
        return self.__classified

    @classified.setter
    def classified(self, dir):
        self.__classified.append(dir[:])

    @property
    def notClassified(self):
        return self.__notClassified

    @notClassified.setter
    def notClassified(self, dir):
        self.__notClassified.append(dir[:])

    # mapeia os diretórios que armazenam os arquivos capturados e armazena em um atributo da radiantClass
    def mapDirectories(self, fullPath, initialFolder):
        root = os.path.join(fullPath,initialFolder)
        years = os.listdir(root)
        for year in years:
            pathYear = os.fspath(os.path.join(root,year))
            if os.path.isdir(pathYear) is True:
                months = os.listdir(pathYear)
                for month in months:
                    pathMonth = os.fspath(os.path.join(pathYear,month))
                    if os.path.isdir(pathMonth) is True:
                        days = os.listdir(pathMonth)
                        for day in days:
                            pathDay = os.fspath(os.path.join(pathMonth,day))
                            self.directories = pathDay
        self.mapClassifiedRegistry()

    # mapeia os registros que já possuem classificação e armazena em um atributo da radiantClass
    def mapClassifiedRegistry(self):
        for folder in self.directories:        
            path = list()
            fullPath = list()
            if os.path.isdir(folder) is True:
                files = os.listdir(folder)
                for file in files:
                    if file.find('.date') != -1: 
                        for file1 in files:
                            if file1.find(file[:16]) != -1:
                                path.append(file1)
            fullPath.append(folder)
            fullPath.append(path)
            self.classified = fullPath

    # grava as características extraídas em arquivo .csv
    # colunas = id,frames,month,day,magnitude,radiantClass 
    def appendCsv(self, feature):
        try:
            if os.path.exists('../dataset/dataset.csv') is False:
                file = open('../dataset/dataset.csv', 'w')
                file.write('id,frames,month,day,magnitude,radiantClass\n')
                file.close()
            else:
                file = open('../dataset/dataset.csv', 'r')
                fileSize = len(file.readlines())
                if fileSize == 0:
                    file.write('id,frames,month,day,magnitude,radiantClass\n')
                file.close()

            file = open('../dataset/dataset.csv', 'a')
            file.write(feature.id)
            file.write(',')
            file.write(feature.frames)
            file.write(',')
            file.write(feature.month)
            file.write(',')
            file.write(feature.day)
            file.write(',')
            file.write(feature.magnitude)
            file.write(',')
            file.write(feature.radiantClass)
            file.write('\n')
        except Exception as e:
            print('Error: ', e)
        finally:
            file.close()
