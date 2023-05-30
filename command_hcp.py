import os
import numpy as np

cons = ['NiCoCr_hcp', 'FeNiCoCr_hcp']

fout = open('command_hcp.sh', "w")

for i in range(len(cons)):
	sws = np.linspace(2.48, 2.92, 12)
	coa_array = np.linspace(4 / 3, 2, 9)
	for n in range(len(sws)):
		a = cons[i]
		b = sws[n]
		for c in range(len(coa_array)):
			fout.write("cd ./%s;" % (a))
			fout.write(
		" /home1/07053/cli110/5.8.1/build1/bin/kgrn_cpa < ./hea_ca%s_%3.3f.scf > ./hea_ca%s_%3.3f_kgrn.output;" % (
		c + 1, b, c + 1, b))
			fout.write(
		" /home1/07053/cli110/5.8.1/build1/bin/kfcd_cpa < ./hea_ca%s_%3.3f.fcd > ./hea_ca%s_%3.3f_kfcd.output;" % (
		c + 1, b, c + 1, b))
			fout.write(" cd ..; ./check_status.sh ./%s/kgrn/hea_ca%s_%3.3f.chd ./%s/kgrn/hea_ca%s_%3.3f.prn >> ./kgrn.log\n"
			           % (a, c + 1, b, a, c + 1, b))

fout.close()
