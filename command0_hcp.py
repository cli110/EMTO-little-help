import os
import numpy as np

cons = ['NiCoCr_hcp', 'FeNiCoCr_hcp']

fout = open('command0_hcp.sh',"w")

coa_array = np.linspace(4 / 3, 2, 9)

for i in range(len(cons)):
	a = cons[i]
	for j in range(len(coa_array)):
        		fout.write("cd ./%s;"%(a))
        		fout.write(" /home1/07053/cli110/5.8.1/build1/bin/bmdl < ./hea_ca%s.bmdl > ./hea_ca%s_bmdl.output;"%(j + 1, j + 1))
        		fout.write(" /home1/07053/cli110/5.8.1/build1/bin/kstr < ./hea_ca%s.kstr > ./hea_ca%s_kstr.output;"%(j + 1, j + 1))
        		fout.write(" /home1/07053/cli110/5.8.1/build1/bin/shape < ./hea_ca%s.shape > ./hea_ca%s_shape.output;"%(j + 1, j + 1))
			fout.write("echo hea_ca%s finished;"%(j + 1))
			fout.write("cd ..\n")
fout.close()
