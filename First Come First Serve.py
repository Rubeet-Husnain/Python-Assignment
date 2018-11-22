def initialize(process,t_process):
	i=0	
	for i in xrange(int(t_process)):
		process.append([])
		process[i].append(input("Enter Process Name:"))
		process[i].append(int(input("Arrival Time is:")))
		process[i].append(int(input("Burst Time is:")))

	
def print_process(process,t_process):
	brust_time=0
	print 'PName\tA. Time\tB.Time'
	i=0
	for i in xrange(int(t_process)):
        	print process[i][0] ,"     ", process[i][1],"     ", process[i][2]
        	brust_time+=process[i][2]
	
	print "Total Time : ",brust_time


def sorting(process):
	process.sort(key=lambda process:process[1])




process=[]
t_process=0
t_process=input("Enter Total Number of Processes:")
initialize(process,t_process)
sorting(process)
print_process(process,t_process)

