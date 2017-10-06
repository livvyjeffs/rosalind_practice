max_count = 0
max_nt = 1000
dna = ""
rna = ""

with open("rosalind_rna.txt",'r') as file:
	dna = file.read().strip()
	#dna = dna.strip()

dna_rna_pairs = {
	'A':'A',
	'C':'C',
	'G':'G',
	'T':'U'
}

#while max_count < max_nt:
for nt in dna:
	if max_count < max_nt:
		max_count+=1
		#print dna_rna_pairs[nt]
		rna += dna_rna_pairs[nt]
	else:
		break
					
print rna