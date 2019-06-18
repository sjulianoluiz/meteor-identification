from abc import ABCMeta, abstractmethod

class Extractor(object, metaclass=ABCMeta):
  @abstractmethod
  def extractFeatures(self):
    pass
