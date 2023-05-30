import numpy as np
import ase
from pyemto.utilities import distort, rotation_matrix
from pyemto.examples.emto_input_generator import *
from ase.visualize import view
from ase.build import cut, make_supercell
import sys

nkx = 25
nky = 25
nkz = 25
a = np.sqrt(2) / 2
b = np.sqrt(6)
c = np.sqrt(3)

os.mkdir('./NiCoCr_hcp')
os.chdir('./NiCoCr_hcp')

folder = './'
emtopath = folder
latpath = emtopath

slurm_options = ['#!/bin/sh',
                 '#PBS -q mpi',
                 '#PBS -N Print_fcc',
                 '#PBS -l nodes=1:ppn=1',
                 '#PBS -l walltime=48:00:00',
                 'cd $PBS_O_WORKDIR']

coa_array = np.linspace(4 / 3, 2, 9)
print(coa_array)
find_primitive = False
coords_are_cartesian = True
# Calculate equilibrium volume

for i in range(len(coa_array)):
	coa = coa_array[i]

	# Primitive hcp
	prims0 = np.array([[1.0000000000, 0.0000000000, 0.0000000000],
	                   [-0.5000000000, np.sqrt(3.) / 2, 0.0000000000],
	                   [0.0000000000, 0.0000000000, coa]])

	basis0 = np.array([[0.0, 0.0, 0.0], [0.0, 0.57735027, coa / 2.0]])

	species = [['Co', 'Co', 'Cr', 'Cr', 'Ni', 'Ni'], ['Co', 'Co', 'Cr', 'Cr', 'Ni', 'Ni']]
	splts = [[1, -1, 1, -1, 1, -1], [1, -1, 1, -1, 1, -1]]
	concs = [[0.166, 0.166, 0.167, 0.167, 0.167, 0.167],
	         [0.166, 0.166, 0.167, 0.167, 0.167, 0.167]]

	input_creator = EMTO(folder=emtopath, EMTOdir='/share/apps/emto/bin')
	input_creator.prepare_input_files(latpath=latpath,
	                                  jobname='hea_ca{}'.format(i+1),
	                                  species=species,
	                                  splts=splts,
	                                  concs=concs,
	                                  prims=prims0,
	                                  basis=basis0,
	                                  find_primitive=find_primitive,
	                                  coords_are_cartesian=coords_are_cartesian,
	                                  latname='hea_ca{}'.format(i+1),
	                                  nz1=32,
	                                  ncpa=20,
	                                  sofc='Y',
	                                  nkx=nkx,
	                                  nky=nky,
	                                  nkz=nkz,
	                                  parallel=True,
	                                  alpcpa=0.6,
	                                  KGRN_file_type='scf',
	                                  KFCD_file_type='fcd',
	                                  amix=0.01,
	                                  tole=1e-6,
	                                  tolef=1e-6,
	                                  iex=7,
	                                  niter=200,
	                                  kgrn_nfi=91,
	                                  crt='M',
	                                  slurm_options=slurm_options)

	sws0 = np.array(np.linspace(2.48, 2.92, 12))

	input_creator.write_bmdl_kstr_shape_input()
	input_creator.write_kgrn_kfcd_swsrange(sws=sws0)
