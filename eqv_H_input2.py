import numpy as np
import ase
from pyemto.utilities import distort, rotation_matrix
from pyemto.examples.emto_input_generator import *
from ase.visualize import view
from ase.build import cut, make_supercell
import sys

print(np.linspace(2.60, 2.80, 12))
find_primitive = False

coords_are_cartesian = True

nkx = 25
nky = 25
nkz = 25
a = np.sqrt(2) / 2
b = np.sqrt(6)
c = np.sqrt(3)

#os.mkdir('./NiCoCr_H2')
os.chdir('./FeNiCoCr_H2')

prims0 = np.array([[-0.5, -0.5, 0.0],
                   [-0.5, 0.0, -0.5],
                   [0.0, -0.5, -0.5]])

basis0 = np.array([[0.0, 0.0, 0.0],
                   [0.25, 0.25, 0.25], [0.75, 0.75, 0.75],
                   [0.5, 0.5, 0.5]])

species = [['Fe', 'Fe', 'Co', 'Co', 'Cr', 'Cr', 'Ni', 'Ni'],
           ['H', 'H', 'Va', 'Va'], ['H', 'H', 'Va', 'Va'],
           ['Va', 'Va']]
splts = [[1, -1, 1, -1, 1, -1, 1, -1],
         [1, -1, 1, -1], [1, -1, 1, -1],
         [1, -1]]
concs = [[0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125],
         [0.25, 0.25, 0.25, 0.25], [0.25, 0.25, 0.25, 0.25],
         [0.5, 0.5]]
print(concs)
folder = './'
emtopath = folder
latpath = emtopath

slurm_options = ['#!/bin/sh',
                 '#PBS -q mpi',
                 '#PBS -N Print_fcc',
                 '#PBS -l nodes=1:ppn=1',
                 '#PBS -l walltime=48:00:00',
                 'cd $PBS_O_WORKDIR']

input_creator = EMTO(folder=emtopath, EMTOdir='/share/apps/emto/bin')
input_creator.prepare_input_files(latpath=latpath,
                                  jobname='hea',
                                  species=species,
                                  splts=splts,
                                  concs=concs,
                                  prims=prims0,
                                  basis=basis0,
                                  find_primitive=find_primitive,
                                  coords_are_cartesian=coords_are_cartesian,
                                  latname='hea',
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

sws0 = np.array(np.linspace(1.40, 3.60, 24))

input_creator.write_bmdl_kstr_shape_input()
input_creator.write_kgrn_kfcd_swsrange(sws=sws0)
