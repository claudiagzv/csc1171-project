# Predicting Plasmodium falciparum activity - CSC1171

CSC1171 Data Analytics and Data Mining group project investigating whether molecular properties can predict activity against Plasmodium falciparum using the supplied MMV/ChEMBL dataset. DNDi was explored initially but is not used for the selected prediction task.

## Research question

**How accurately can we predict activity against Plasmodium falciparum (pf_ec50_uM) using molecular properties in the MMV dataset?**

The inputs are molecular properties such as molecular weight, logP, hydrogen bonding, polar surface area, flexibility and aromaticity. The target is `pf_ec50_uM`.

We will first inspect and prepare the data, then explore relationships and evaluate prediction models. Predictions do not establish that a compound is a safe or effective treatment.

## Repository structure

```text
data/                       Original supplied datasets (keep unchanged)
notebooks/                   Exploration, preprocessing and modelling notebooks
results/figures/            Exported charts
results/tables/             Exported summary tables
slides/                     Presentation PDFs and slide files
scripts/                    Optional reusable analysis scripts
.gitignore                  Lecturer template ignore rules
README.md                   Project overview and instructions
requirements.txt            Python dependencies
```

The structure follows NoCh-Git's ProjectTemplate: https://github.com/NoCh-Git/ProjectTemplate. Existing project work is retained instead of copying the template's blank example files.

## Datasets

MMV contains 2,452 compound records, including 1,687 with an available `pf_ec50_uM` value. These measured values will provide the labelled examples for PF prediction.

DNDi contains 190 compound records but no available `pf_ec50_uM` values. Its exploration is retained to document why we selected MMV. The datasets are not being combined for this task.

Both files are tab-separated despite the `.csv` extension: load with `sep="\t"`. Keep the original files unchanged. Missing activity values must not be treated as zero.

Columns include compound identifiers, SMILES, molecular properties, biological activity, cytotoxicity and selectivity indices. The initial model will use molecular properties as inputs, excluding identifiers, other pathogen activity measurements and selectivity indices.

Confirm endpoint definitions and units before transforming the target. Source/extraction details and reuse terms still need to be documented.

## Getting started

Run these commands from the `csc1171-project` folder.

### macOS / Linux (bash/zsh)

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

### Windows (PowerShell)

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

### Open the notebooks

Open a notebook in VS Code, click **Select Kernel**, and choose the `.venv` Python environment. Install the VS Code Python and Jupyter extensions if prompted.

