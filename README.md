# Chemical properties and pathogen activity — CSC1171

CSC1171 Data Analytics and Data Mining group project using the supplied MMV/ChEMBL and DNDi compound datasets.

## Research question

**How do chemical properties relate to activity against the pathogens in our MMV and DNDi data?**

We will explore relationships between molecular size, lipophilicity, polar surface area, hydrogen bonding, flexibility, aromaticity and rule-of-five violations, and the available pathogen activity measurements. The analysis is exploratory: associations do not establish causation or clinical effectiveness.

## Repository structure

```text
data/                       Original supplied datasets (keep unchanged)
notebooks/                  Team plan and analysis notebooks
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

| File | Rows | Columns |
|---|---:|---:|
| `data/mmv_ChEMBL-IC50s-Sep2026.csv` | 2,452 | 27 |
| `data/dndi_compounds-IC50.csv` | 190 | 27 |

Both files are **tab-separated** despite the `.csv` extension: load with `sep="\t"`. Four compound IDs occur in both sources; inspect overlapping measurements before combining records. Missing activity values must not be treated as zero.

Columns include compound identifiers, SMILES, chemical properties, pathogen IC50/EC50 measurements, cytotoxicity and selectivity indices. Confirm endpoint definitions and units before comparisons or transformations. Source/extraction details and reuse terms still need to be documented by the team.

## Getting started

From the repository root, install the analysis dependencies into your chosen Python environment:

```sh
python -m pip install -r requirements.txt
```

Open the notebooks in a Jupyter-capable editor using that environment. For the standalone Jupyter interface, install Jupyter separately in the same environment. Start with `notebooks/01_team_plan_property_pathogen_analysis.ipynb`, then `notebooks/initial_data_exploration.ipynb`.

The exploration notebook supports launching from the repository root or the `notebooks` folder. It retains earlier troubleshooting cells and their saved outputs; the successful import uses tab separation.


