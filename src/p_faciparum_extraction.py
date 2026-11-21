import os
from pathlib import Path

import pandas as pd

# Gets user's current working directory and reads the MMV dataset.
root_dir = str(Path(os.getcwd()))
mmv_dataset = Path(root_dir, 'data/mmv_ChEMBL-IC50s-Sep2026.csv')

mmv_compounds_df = pd.read_csv(mmv_dataset, delimiter='\t')
mmv_compounds_df = mmv_compounds_df.drop(columns=['tb_ic50_uM', 'tc_ic50_uM', 'tbrucei_ic50_uM',
       'ld_ic50_uM', 'cp_ec50_uM', 'tg_ec50_uM', 'hepg2_cc50_uM', 'si_pf',
       'si_tb', 'si_tc', 'si_tbrucei', 'si_ld', 'si_cp', 'si_tg'])

# Creates a CSV file of rows containing potency values for P. Falciparum and stores it in the data directory.
pf_df = mmv_compounds_df[mmv_compounds_df["pf_ec50_uM"].notna()]

pf_df.to_csv('data/p_falciparum_mmv_data.csv', index=False)
