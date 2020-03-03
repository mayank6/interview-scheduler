class Time:
	def __init__(self, startTime,endTime):
		self.startTime = startTime
		self.endTime = endTime

class Attendee:
	def __init__(self, id):
		self.uniqueId = id

class Interviewer:
	def __init__(self, id):
		self.uniqueId = id
						
class Room:
	def __init__(self, id):
		self.uniqueId = id
		
class printOutput:
	def __init__(self,attendee,interviewer,room,time):
		self.attendee = attendee
		self.interviewer = interviewer
		self.room = room
		self.time = time

	def __str__(self):
		return self.attendee.uniqueId + "  " + self.interviewer.uniqueId + "  " + self.room.uniqueId + "  " + str(self.time.startTime%12) +"-" + str(self.time.endTime%12)


class getInput:
	def __init__(self):
		self.attendees = []
		self.interviewers = []
		self.rooms = []

	def processAttendee(self, attendeeList):
		for uid in attendeeList:
			attendee = Attendee(uid)
			self.attendees.append(attendee)
	
	def processInterviewer(self,interviewerList):
		for uid in interviewerList:
			interviewer = Interviewer(uid)
			self.interviewers.append(interviewer)

	def processRoom(self,roomList):
		for uid in roomList:
			room = Room(uid)
			self.rooms.append(room)
	def getAttendee(self):
		return self.attendees

	def getInterviewer(self):
		return self.interviewers

	def getRoom(self):
		return self.rooms
#

class InterviewDayRoutine:
	def __init__(self,start,end,lengthInterview,lunchtime):
		#param start:str
		#return 
		self.startDay = start
		self.endDay = end
		self.lengthInterview = lengthInterview
		self.lunchtime = lunchtime

	def getHour(self):
		return self.lengthInterview
	
	def valid(self,time):
		lunchtime = self.lunchtime
		if time.startTime < lunchtime.startTime < time.endTime or  time.startTime < lunchtime.endTime < time.endTime:
			return False
		if lunchtime.startTime < time.startTime and lunchtime.endTime > time.endTime:
			return False
		if time.startTime > self.endDay or time.endTime > self.endDay:
			return False
		return True
	def isDayEnd(self,time):
		if time.startTime > self.endDay or time.endTime > self.endDay:
			return True
		return False


class Schedule:
	def __init__(self):
		pass
	def solve(self):
		lunch = Time(10,11)
		Routine = InterviewDayRoutine(9,18,2,lunch)
		Input = getInput()
		# attendee = list(map(str,input().split()))
		# interviewer = list(map(str,input().split()))
		# room = list(map(str,input().split()))
		attendee = ["1","2","3","4","5"]
		interviewer = ["A","B","C","D","E"]
		room = ["R1","R2","R3","R4","R5"]
		Input.processAttendee(attendee)
		Input.processInterviewer(interviewer)
		Input.processRoom(room)
		getAttendee = Input.getAttendee()
		getRoom = Input.getRoom()
		getInterviewer = Input.getInterviewer()
		start = Routine.startDay
		end = Routine.endDay
		hour = Routine.getHour()
		indexInterviewer = 0
		indexRoom = 0
		indexAttendee = 0
		answer = []
		leftAttendee = []
		while(indexAttendee < len(getAttendee)):
			indexInterviewer = 0
			indexRoom = 0
			timeSlot = Time(start,start + hour)
			if Routine.valid(timeSlot):
				while (indexAttendee < len(getAttendee) and indexInterviewer < len(getInterviewer)):
					if (indexRoom < len(getRoom)):
						ans = printOutput(getAttendee[indexAttendee],getInterviewer[indexInterviewer],getRoom[indexRoom],timeSlot)
						answer.append(ans)
					else:
						break
					indexRoom += 1
					indexInterviewer += 1
					indexAttendee += 1
			elif Routine.isDayEnd(timeSlot):
				break
			start = start + hour
 
		for i in answer:
			print(i)
		while indexAttendee < len(getAttendee):
			print(getAttendee[indexAttendee].uniqueId, "interview can not Schedule")
			indexAttendee += 1

if __name__ == "__main__":
	Schedule().solve()
