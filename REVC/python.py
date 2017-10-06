max_count = 0
max_bp = 1000
dna = ""
dna_rev = ""
dna_rev_c = ""


with open("rosalind_revc.txt",'r') as file:
	dna = file.read().strip()
	#dna = dna.strip()

length = len(dna)

for i in range(length):
	dna_rev += dna[length-i-1]

dna_complements = {'A':'T','C':'G','T':'A','G':'C'}

#while max_count < max_nt:
for bp in dna_rev:
	if max_count < max_bp:
		max_count+=1
		#print dna_rna_pairs[nt]
		dna_rev_c += dna_complements[bp]
	else:
		break
					
print dna_rev_c