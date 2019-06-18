class Features(object):
	def __init__(self, __id=None, __frames=None, __month=None, __day=None, __radiantClass=None, __magnitude=None):
		self.__id = __id
		self.__frames = __frames
		self.__month = __month
		self.__day = __day
		self.__radiantClass = __radiantClass
		self.__magnitude = __magnitude
		
	@property
	def id(self):
		return self.__id
		
	@id.setter	
	def id(self, id):
		self.__id = id

	@property
	def magnitude(self):
		return self.__magnitude

	@magnitude.setter
	def magnitude(self, magnitude):
		self.__magnitude = magnitude

	@property
	def month(self):
		return self.__month

	@month.setter
	def month(self, month):
		self.__month = month

	@property
	def day(self):
		return self.__day

	@day.setter
	def day(self, day):
		self.__day = day

	@property
	def radiantClass(self):
		return self.__radiantClass

	@radiantClass.setter
	def radiantClass(self, radiantClass):
		self.__radiantClass = radiantClass
	
	@property
	def frames(self):
		return self.__frames

	@frames.setter
	def frames(self, frames):
		self.__frames = frames

