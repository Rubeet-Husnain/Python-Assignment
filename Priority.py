def initialize(process,t_process):
	i=0	
	for i in xrange(t_process):
		process.append([])
		process[i].append(input("Process Name:"))
		process[i].append(int(input("Arival Time:")))
		process[i].append(int(input("Brust Time:")))
		process[i].append(int(input("Priority:")))

def print_process(process,t_process):
	total_burst=0
	print 'Process Name\t Arival Time\t Brust Time\t Priority'
	i=0
	for i in xrange(int(t_process)):
        	print process[i][0] ,"     ",process[i][1],"     ",process[i][2],"     ",process[i][3]
        	total_burst+=process[i][2]
	
	print "Total Time : ",total_burst

def sorting(process):
	process.sort(key=lambda process:process[1])
	process.sort(key=lambda process:process[3])


t_process=int(input("Enter Number:"))
process=[] 
initialize(process,t_process)
sorting(process)
print_process(process,t_process)



