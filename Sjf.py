def initialize(process,t_process):
	i=0	
	for i in xrange(t_process):
		process.append([])
		process[i].append(input("Enter Process Name"))
		process[i].append(input("Enter Process Name:"))
		process[i].append(int(input("Arrival Time:")))
		process[i].append(int(input("Brust Time")))

def print_process(process,t_process):
	total_burst=0
	print 'Process Name\t Arrival Time\t Brust Time'
	i=0
	for i in xrange(int(t_process)):
        	print process[i][0] ,'\t',process[i][1],'\t',process[i][2]
        	total_burst+=process[i][2]
	
	print "Total Time : ",total_burst

def sorting(process):
	process.sort(key=lambda process:process[1])
	process.sort(key=lambda process:process[2])


t_process=int(input("Enter Number:"))
process=[] 
initialize(process,t_process)
sorting(process)
print_process(process,t_process)