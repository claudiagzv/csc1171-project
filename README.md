# Table of Contents
1. Project Overview
2. Getting started
3. Usage
4. Data & File Overview
5. Results
#

# PROJECT OVERVIEW
## Predicting Plasmodium falciparum activity - CSC1171

CSC1171 Data Analytics and Data Mining group project investigating whether molecular properties can predict activity against Plasmodium falciparum using the supplied MMV/ChEMBL dataset. DNDi was explored initially but is not used for the selected prediction task.

## Research question

**How accurately can we predict activity against Plasmodium falciparum (pf_ec50_uM) using molecular properties in the MMV dataset?**

The inputs are molecular properties such as molecular weight, logP, hydrogen bonding, polar surface area, flexibility and aromaticity. The target is `pf_ec50_uM`.

We will first inspect and prepare the data, then explore relationships and evaluate prediction models. Predictions do not establish that a compound is a safe or effective treatment.

---

# Getting started

Run these commands from the `csc1171-project` folder.

## macOS / Linux (bash/zsh)

```bash
# Optional: select Python version if pyenv is installed
pyenv local 3.11.3

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Windows (PowerShell)

```powershell
# Optional: select Python version if pyenv is installed
pyenv local 3.11.3

# Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Open the notebooks

Open a notebook in VS Code, click **Select Kernel**, and choose the `.venv` Python environment. Install the VS Code Python and Jupyter extensions if prompted.


#


# USAGE

## Commands

Get P. Falciparum dataset & its corressponding training and test sets as CSV files, stored in data directory.
```sh
just get-pf-split-data
```

#

## Repository structure

```text
data/                       Original supplied datasets (keep unchanged)
notebooks/                  Exploration, preprocessing and modelling notebooks
results/figures/            Exported charts
results/tables/             Exported summary tables
slides/                     Presentation PDFs and slide files
src/                        Optional reusable analysis scripts
.justfile                   Command runner file
.gitignore                  Lecturer template ignore rules
README.md                   Project overview and instructions
requirements.txt            Python dependencies
```


## Data & File Overview

[MMV]('data/mmv_ChEMBL-IC50s-Sep2026.csv') contains 2,452 compound records, including 1,687 with an available `pf_ec50_uM` value. These measured values will provide the labelled examples for PF prediction.

[DNDi]('data/dndi_compounds-IC50.csv') contains 190 compound records but no available `pf_ec50_uM` values. Its exploration is retained to document why we selected MMV. The datasets are not being combined for this task.

**Table 1. MMV and DNDi Column Information**
Column            | Content                 | Data Type
------------------|-------------------------|--------------
chembl_id | ChEMBL ID of compound | Varchar
pref_name | Preffered name of a compound | Text
smiles | Text code translation of a chemical molecule's 3D structure | Varchar
molecular_weight | Molecular Weight | Float
logp | Calculated partition coefficient | Float
hba | Hydrogen bond acceptors | Integer
hbd | Hydrogen bond donors | Integer
rtb | Rotatable Bond Count | Integer
ro5_violations | Number of Lipinski's Rule of Five violations | Integers
aromatic_rings | Number of aromatic rings | Integer
heavy_atoms | Number of heavy atoms | Integer
pf_ec50_uM | Plasmodium falciparum 3D7 EC50 | Float
tb_ic50_uM | Mycobacterium tuberculosis H37Rv IC50| Float
tc_ic50_uM | Trypanosoma cruzi IC50 | Float
tbrucei_ic50_uM | Trypanosoma brucei IC50 | Float
ld_ic50_uM | Leishmania donovani IC50 | Float
cp_ec50_uM | Cryptosporidium parvum EC50 | Float
tg_ec50_uM | Toxoplasma gondii EC50 | Float
hepg2_cc50_uM | HepG2 CC50 (Cytotoxicity) | Float
si_pf | Selectivity Index of Plasmodium falciparum 3D7 | Float
si_tb | Selectivity Index of Mycobacterium tuberculosis H37Rv | Float
si_tc | Selectivity Index of Trypanosoma cruzi | Float
si_tbrucei | Selectivity Index of Trypanosoma brucei | Float
si_ld | Selectivity Index of Leishmania donovani | Float
si_cp | Selectivity Index of Cryptosporidium parvum | Float
si_tg | Selectivity Index of Toxoplasma gondii | Float

___


[Train set]('data/train.csv') dataset used to train ML model.


[Test set]('data/test.csv') dataset used to test ML model accuracy.


**Table 2. P. Falciparum Train and Test Set Column Information**
Column            | Content                 | Data Type
------------------|-------------------------|--------------
chembl_id | ChEMBL ID of compound | Varchar
pref_name | Preffered name of a compound | Text
smiles | Text code translation of a chemical molecule's 3D structure | Varchar
molecular_weight | Molecular Weight | Float
logp | Calculated partition coefficient | Float
hba | Hydrogen bond acceptors | Integer
hbd | Hydrogen bond donors | Integer
rtb | Rotatable Bond Count | Integer
ro5_violations | Number of Lipinski's Rule of Five violations | Integers
aromatic_rings | Number of aromatic rings | Integer
heavy_atoms | Number of heavy atoms | Integer
pf_ec50_uM | Plasmodium falciparum 3D7 EC50 | Float
pf_pEC50 | Plasmodium falciparum potency score | Float

#

# RESULTS

Four regression models were compared against a predict-the-mean baseline on a stratified 80/20 split, using the same five cross-validation folds for every model.

| Model | Features | Test R² | Test RMSE |
|---|---|---:|---:|
| Mean baseline | - | -0.002 | 0.584 |
| Linear Regression | 9 descriptors | 0.044 | 0.570 |
| XGBoost | fingerprints + descriptors | 0.120 | 0.547 |
| SVR | fingerprints + descriptors | 0.121 | 0.547 |
| Random Forest | fingerprints + descriptors | 0.148 | 0.538 |

Random Forest using Morgan fingerprints and molecular descriptors performed best, explaining about 15% of the variation in pEC50. All models predict within roughly half a pEC50 unit, so they can rank compounds for screening but cannot replace experimental measurement. Random Forest and SVR scored far higher on training data than in cross-validation, indicating overfitting.

A Random Forest classifier separating potent (pEC50 >= 6) from less potent compounds reached 65% accuracy, against 57% for always predicting the majority class.

Full comparison in `notebooks/model_evaluation.ipynb`. Exported figures are in `results/figures/` and summary tables in `results/tables/`.
