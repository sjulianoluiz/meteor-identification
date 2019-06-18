from extractor import Extractor
from feature import Features
from systemHandler import SystemHandler
from xml.dom.minidom import parse
from threading import Thread
import csv
import imageProcessingCython

class ClassifiedRecords(Extractor):
	__system = SystemHandler()
	__features = Features()

	def extractFeatures(self, directories):
		doc = ""
		for dir in directories:
			for file in dir[1]:
				if file.find('.xml') != -1:
					doc = parse(dir[0]+'/'+file)
					xml = doc.documentElement
					uc_path = xml.getElementsByTagName('uc_path')
					pixel = []
					pixels = []

					for item in uc_path:
						pixel.append(item.getAttribute('y'))
						pixel.append(item.getAttribute('x'))
						pixels.append(pixel)
						pixel = []

					for file1 in dir[1]:
						a = file1.find(file[:16])
						if a != -1:
							b = file1.find('P.jpg') 
							c = file1.find('.XML')
							if b != -1:
								image = dir[0]+'/'+file1
							if c != -1:
								docClassified = parse(dir[0]+'/'+file1)

					for ua_object in docClassified.getElementsByTagName('ua2_object'):
						self.__features.radiantClass = self.getMeteorClasses('../dataset/classList.csv', ua_object.getAttribute('class'))
					
					print(image)

					self.__features.magnitude = imageProcessingCython.countBrightnessPixels(pixels, image)

					self.__features.id = file[:16]
					self.__features.frames = xml.getAttribute('frames')
					self.__features.month = xml.getAttribute('mo')
					self.__features.day = xml.getAttribute('d')

					thread = Thread(target=self.__system.appendCsv, args=(self.__features,))
					thread.start()
					thread.join()

	def getMeteorClasses(self, path, classe):
		try:
			fileOpen = open(path, 'r')
			file = csv.reader(fileOpen)
			response = None
			for row in file:
				if row[1] == classe:
					response = row[0]
			return response
		except Exception as e:
			print(e)
		finally:
			fileOpen.close()
