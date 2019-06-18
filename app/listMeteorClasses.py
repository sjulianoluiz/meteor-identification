from systemHandler import SystemHandler
from xml.dom.minidom import parse
import os

class ListMeteorClasses(object):
    def list(self, directories):
        list = []
        for dir in directories:
            if os.path.isdir(dir) is True:
                for file in os.listdir(dir):
                    if file.find('.XML') != -1:
                        doc = parse(dir+'/'+file)
                        for ua_object in doc.getElementsByTagName('ua2_object'):
                            list.append(ua_object.getAttribute('class'))

        return list

    def removeDuplicateClasses(self, list):
        t = []
        [ t.append(item) for item in list if not t.count(item) ]
        return t

    def recordList(self, list):
        file = open('../dataset/classList.csv', 'a')
        i = 1
        for element in list:
            file.write(str(i))
            file.write(',')
            file.write(element)
            file.write('\n')
            i += 1
        file.close()


if __name__ == "__main__":
    system = SystemHandler()
    classList = ListMeteorClasses()

    system.mapDirectories('/media/juliano/HDJULIANO', 'EMC1')
    list = classList.list(system.directories)
    system.mapDirectories('/media/juliano/HDJULIANO', 'EMC2')
    list1 = classList.list(system.directories)

    list = list + list1

    classList.recordList(classList.removeDuplicateClasses(list))
