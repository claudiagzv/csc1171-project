import os
from pathlib import Path

import pandas as pd

root_dir = str(Path(os.getcwd()))
mmv_dataset = Path(root_dir, 'data/mmv_ChEMBL-IC50s-Sep2026.csv')

mmv_compounds_df = pd.read_csv(mmv_dataset, delimiter='\t')

pf_df = mmv_compounds_df[mmv_compounds_df['pf_ec50_uM'].notna()]

pf_df.to_csv('data/p_falciparum_mmv_data.csv')
