#coding=utf-8
class RoundData(object):
	count =1
	count_=0
	begin=0
	startlist=[]
	endlist=[]

	temp1='0:00:00'
	temp2='0:00:00'
	temp_old='0:00:00'
	temp_next='59:59:59'

	def init(self):
		self.count =1
		self.count_=0
		self.begin=0
		self.startlist=[]
		self.endlist=[]
		self.temp1='0:00:00'
		self.temp2='0:00:00'
		self.temp_old='0:00:00'
		self.temp_next='59:59:59'

	def t2s(self,time):#时间格式转换为秒
		n=len(time)
		if time[n-2]=='.':
			second=0
			second+=float(time[n-4:n])
			second+=float(time[n-7:n-5])*60
			second+=float(time[:n-8])*3600
		else:
			second=0
			second+=int(time[n-2:n])
			second+=int(time[n-5:n-3])*60
			second+=int(time[:n-6])*3600
		return second

	def checkformat(self,time):
		n=len(time)
		if time[n-3] !=':' or time[n-6] !=':':
			return False
		if int(time[n-2:n]) >= 60 or int(time[n-5:n-3]) >=60 :
			return False
		return True

class BattleData(object):
	count =1
	count_=0
	begin=0
	startlist=[]
	endlist=[]

	temp1='0:00:00'
	temp2='0:00:00'
	temp_old='0:00:00'
	temp_next='59:59:59'

	winteam=1
	winlist=[]

	def init(self):
		self.count =1
		self.count_=0
		self.begin=0
		self.startlist=[]
		self.endlist=[]
		self.temp1='0:00:00'
		self.temp2='0:00:00'
		self.temp_old='0:00:00'
		self.temp_next='59:59:59'
		self.winteam=1
		self.winlist=[]

	def t2s(self,time):#时间格式转换为秒
		n=len(time)
		if time[n-2]=='.':
			second=0
			second+=float(time[n-4:n])
			second+=float(time[n-7:n-5])*60
			second+=float(time[:n-8])*3600
		else:
			second=0
			second+=int(time[n-2:n])
			second+=int(time[n-5:n-3])*60
			second+=int(time[:n-6])*3600
		return second

	def checkformat(self,time):
		n=len(time)
		if time[n-3] !=':' or time[n-6] !=':':
			return False
		if int(time[n-2:n]) >= 60 or int(time[n-5:n-3]) >=60 :
			return False
		return True

class MatchData(object):
	Aplayerlist=[]
	Bplayerlist=[]
	Aherolist=[]
	Bherolist=[]
	finalwinner='A'
	attack='A'
	game=1
	mapn=' '
	time=' '
	teama=' '
	teamb=' '
	def init(self):
		self.finalwinner='A'
		self.attack='A'
		self.Aplayerlist=[]
		self.Bplayerlist=[]
		self.Aherolist=[]
		self.Bherolist=[]
		self.game=1
		self.mapn=' '
		self.time=' '
		self.teama=' '
		self.teamb=' '

class Path(object):
	def __init__(self):
		pass
		
