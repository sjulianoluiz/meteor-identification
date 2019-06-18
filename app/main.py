import os
import sys
import pandas as pd
from systemHandler import SystemHandler
from classifiedRecords import ClassifiedRecords
from multiprocessing import Process
from threading import Thread

if __name__ == '__main__':
    try:
        system = SystemHandler()
        system.mapDirectories('/media/juliano/HDJULIANO/', 'EMC2')

        classifiedRecords = ClassifiedRecords()
        # classifiedRecords.extractFeatures(system.classified)
        thread = Thread(target=classifiedRecords.extractFeatures, args=(system.classified,))
        thread.start()
        thread.join()
    except Exception as e:
        print(e)

