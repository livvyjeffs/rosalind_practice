max_count = 0
max_nt = 1000
dna = ""
total_count = 0

a = 0
t = 0
g = 0
c = 0

count_nt = {'A':a,'C':c,'G':g,'T':t}

with open("rosalind_dna.txt",'r') as file:
	dna = file.read()

#while max_count < max_nt:
for nt in dna:
	total_count+=1
	max_count+=1
	for count in count_nt:
		#print 'count: ',count
		if nt == count:
			count_nt[count]+=1
				

#print total_count
#print count_nt

count_string = ""
for count in count_nt:
	count_string += str(count_nt[count]) + " "

print count_string