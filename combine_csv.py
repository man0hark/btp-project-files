# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:10:46 2021

@author: Sowrappa
"""

import os
import glob
import pandas as pd
os.chdir("D:/extra_audio/full_csv_feat")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", header=False,index=False, encoding='utf-8-sig')