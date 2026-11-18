import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

#1. load zeas filtered data
pf_df = pd.read_csv("data/p_falciparum_mmv_data.csv", index_col=0)
print("Loaded rows and columns:", pf_df.shape) # 1687 rows and 27 columns

"""
EC50 is how much drug it takes to kill half the parasites

smaller ec50 e.g 0.01 is much stronger/better

in our data the numbers are widely spread out.

log10 fixes the spread as seen from bashirs exploration

so now EC50 of 0.01 > log10 is -2 > pEC50 is 6 - (-2) =8 which is very strong
"""

#2. make a potency score
# It turns the spread out EC50 values into an even 3 to 8 scale where bigger means stronger, and the 6 converts the µM units to the standard molar pEC50 scale.
pec50 = 6 - np.log10(pf_df["pf_ec50_uM"])
pf_df["pEC50"] = pec50 # adds pec50 as a new column 

#3. sort drugs into 5 groups
#ranks each group weakest to strongest, then cuts the list into 5 equal groups, 0 to 4
potency_group = pd.qcut(pec50, q=5, labels=False)

#4. split the data
#shuffles rows and cuts into two groups, train_df gets 80%, test_df gets 20%
train_df, test_df = train_test_split(
    pf_df, test_size=0.2, random_state=42, stratify=potency_group,
)

#5.saving the tables
# index=false stops it adding row-number column again
train_df.to_csv("data/train.csv", index=False)
test_df.to_csv("data/test.csv", index=False)

#6. check for myself
print("Train rows:", len(train_df))
print("Test rows:", len(test_df))

#check that no drugs are in both tables
print("Compounds in both files:", len(set(train_df["chembl_id"]) & set(test_df["chembl_id"])))

#check that numbers are close, so split is fair
print("Median pf_ec50_uM, train:", round(train_df["pf_ec50_uM"].median(), 3))
print("Median pf_ec50_uM, test:", round(test_df["pf_ec50_uM"].median(), 3))

# check that pEC50 is a new column
print("Columns in train:", train_df.shape[1], "Has pEC50:", "pEC50" in train_df.columns)