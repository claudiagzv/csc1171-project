# Presentation 1 - Team Analysis & Preprocessing Plan

**Module:** CSC1171 - Data Analytics and Data Mining  
**Dataset:** MMV & DNDi - Chemical Descriptors and Antipathogen Activity

**Research Question:** How are molecular properties associated with measured activity against seven pathogen targets?

**Objective:** Prepare a reproducible data analysis demonstrating dataset understanding, appropriate preprocessing, descriptive statistics and initial property–activity relationships.

---

## 1. Team Responsibilities & Deliverables

| Team Members | Main Responsibilities | Deliverables |
|---|---|---|
| **Claudia & Bashir** | Dataset inspection, cleaning, preprocessing, general distributions, descriptive statistics and documentation of findings. | Data-quality summary, cleaning log, distribution plots and written observations. |
| **Zea & Eghosa** | Manual data curation of missing chemical descriptors, targeted property–activity visualisations and correlation analysis. | Curation log, labelled relationship plots, correlation table and initial observations. |
| **Everyone** | Review preprocessing decisions, interpret results, prepare slides and rehearse the presentation. | Agreed cleaned dataset, documented limitations and final presentation. |

## 2. Initial Dataset Overview

The project uses two datasets containing molecular descriptors and experimentally measured activity against seven pathogens.

| Dataset | Rows | Columns | Initial Observations |
|---|---:|---:|---|
| MMV | 2,452 | 27 | 5 records with missing molecular descriptors. |
| DNDi | 190 | 27 | 8 records with missing molecular descriptors. |
| Combined (before deduplication) | 2,642 | 27 | 4 overlapping compound IDs; 2,638 unique compounds. |

**Initial technical observations:**
- Both files use tab-separated formatting despite their `.csv` extensions.
- Nine molecular descriptors are available for analysis.
- Seven pathogen potency endpoints contain IC50 and/or EC50 measurements.
- Additional variables include HepG2 CC50 and selectivity indices.
- The four overlapping compounds require examination before consolidation.
- These are baseline observations; final counts must be verified following preprocessing.

## 3. Preprocessing & Exploratory Data Analysis Workflow

### Stage 1 - Dataset Inspection & Initial Cleaning

**Responsible: Claudia & Bashir**

**Tasks:**
1. Import both datasets using `sep="\t"`.
2. Examine dataset dimensions (rows and columns).
3. Identify numerical, categorical and identifier columns.
4. Check missing values and calculate missing-value percentages.
5. Identify duplicate rows and repeated `chembl_id` values.
6. Check numerical ranges and investigate unusual or invalid values.
7. Calculate initial descriptive statistics.
8. Record findings and justify cleaning decisions.

**Deliverables:**
- Initial data-quality report.
- Missing-values summary.
- Duplicate and outlier checks.
- Preprocessing and cleaning log.

### Stage 2 - Manual Data Curation

**Responsible: Zea & Eghosa**

**Tasks:**
1. Identify the 13 records containing missing molecular descriptors. If not found, decide what to do next (remove or replace values).
2. Match compounds using their `chembl_id`.
3. Verify that chemical structures and descriptor definitions correspond to the original dataset.
4. Document all changes, sources and decisions.


**Curation log:**

| Compound ID | Property | Original Value | Updated Value | Source | Verification |
|---|---|---|---|---|---|
| To complete | | | | | |



### Stage 3 - Dataset Integration & Validation

**Responsible: Claudia & Bashir (reviewed by everyone)**

**Tasks:**
1. Combine MMV and DNDi datasets using consistent column names.
2. Add source labels identifying the original dataset.
3. Examine the four overlapping `chembl_id` records.
4. Compare overlapping records before deciding whether to consolidate them.
5. Preserve source information and relevant differences in activity measurements.
6. Check data types, missing values and duplicates after integration.
7. Save a versioned, analysis-ready dataset.

**Deliverable:** Validated dataset and documented merge decisions.

### Stage 4 - General Distributions & Descriptive Statistics

**Responsible: Claudia & Bashir**

**Tasks:**
1. Examine distributions of the nine molecular descriptors.
2. Examine distributions of the seven pathogen activity endpoints.
3. Generate appropriate histograms and boxplots.
4. Calculate descriptive statistics:
   - Count and missing-value percentage.
   - Median and interquartile range (IQR).
   - Minimum and maximum values.
   - Distribution shape, spread and potential outliers.
5. Compare data coverage between MMV and DNDi.
6. Write concise observations describing important patterns, unusual values and limitations.

**Deliverables:**
- Labelled distribution plots.
- Descriptive-statistics table.
- Written findings for the presentation.

### Stage 5 - Property-Activity Relationship Analysis

**Responsible: Zea & Eghosa**

Investigate how molecular properties relate to experimentally measured activity against the seven pathogens.

**Allocated properties:**

| Member | Property Group | Variables |
|---|---|---|
| **Zea** | Molecular size and hydrogen bonding | `molecular_weight`, `heavy_atoms`, `hba`, `hbd` |
| **Eghosa** | Lipophilicity, polarity, flexibility and aromaticity | `logp`, `psa`, `rtb`, `aromatic_rings`, `ro5_violations` |

**Tasks:**
1. Examine assigned properties against applicable pathogen activity endpoints.
2. Generate scatterplots for continuous properties.
3. Use boxplots or jittered plots where integer-valued properties make scatterplots difficult to interpret.
4. Calculate Spearman correlation coefficients where appropriate.
5. Identify positive, negative, weak or absent relationships.
6. Examine whether findings differ between MMV and DNDi.
7. Record sample size (`n`) for each analysis.
8. Write initial observations and limitations.

**Deliverables:** Property–activity plots, correlation summary and preliminary findings.

---

## 4. Technical Preprocessing & Analysis Rules

### Missing Values
- Do not replace missing activity measurements with zero.
- For each property–activity analysis, include only records where both variables are available.
- Do not remove a compound solely because an unrelated pathogen outcome is missing.

### Activity Measurements
- Verify activity endpoints and concentration units before conversion.
- For positive IC50 concentrations confirmed in µM:

  `pIC50 = 6 − log10(IC50 in µM)`

- For positive EC50 concentrations confirmed in µM:

  `pEC50 = 6 − log10(EC50 in µM)`

- Higher pIC50 or pEC50 indicates greater measured potency.
- Retain original measurements and distinguish IC50 from EC50.
- Do not automatically combine measurements from incompatible assays.

### Outliers
- Investigate unusual values before deciding whether they should be excluded.
- Record the reasoning behind any exclusion.

### Interpretation
- Treat findings as exploratory associations rather than evidence of causation.
- Account for differences in sample size, assay conditions and dataset source.
- Report weak or absent relationships where relevant.

## 5. Documentation & GitHub Organisation

All preprocessing, analysis and findings should be recorded to demonstrate a clear and reproducible workflow.

**Suggested repository structure:**

```text
project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_audit/
│   ├── 02_curation/
│   ├── 03_descriptive/
│   └── 04_relationships/
├── outputs/
│   └── figures/
├── docs/
└── presentation/
```

**Documentation requirements:**
- Preserve original data.
- Record all preprocessing decisions.
- Document sources of manually recovered values.
- Keep code organised and reproducible.
- Record sample sizes before and after preprocessing.
- Ensure all findings can be traced to the relevant analysis.

## 6. Presentation Structure - 10 Minutes

| Slide | Content | Duration |
|---|---|---|
| 1 | Research question, motivation and project objectives. | 1 min |
| 2 | Dataset overview, sources and team responsibilities. | 1 min |
| 3 | Data inspection, missing values, cleaning and preprocessing decisions. | 2 min |
| 4–6 | Descriptive statistics, distributions and selected property–activity findings. | 4 min |
| 7 | Ethical considerations, limitations and next steps. | 2 min |

**Presentation guidance:**
- Select approximately 4–6 meaningful figures rather than presenting every generated plot.
- Include both informative relationships and relevant limitations.
- Use concise interpretations supported by numerical results.
- Ensure every member understands the complete analytical workflow.

## 7. Ethical Considerations & Limitations

The presentation should acknowledge:
- Proper attribution of MMV, DNDi, ChEMBL and external data sources.
- Missing values and incomplete pathogen activity measurements.
- Differences between experimental assays and IC50/EC50 endpoints.
- Potential bias due to unequal MMV and DNDi sample sizes.
- Limitations of interpreting correlations without controlling for other variables.
- Experimental activity does not establish clinical effectiveness.

## 8. Final Team Checklist

Before Session 6, confirm that:

- Both datasets have been inspected and documented.
- Missing values and duplicates have been examined.
- Manual curation is completed and verified where possible.
- Dataset integration and cleaning decisions are documented.
- General distribution plots and descriptive statistics are completed.
- Targeted property–activity plots and correlation summaries are completed.
- Initial findings and limitations are clearly written.
- The shared dataset, code and figures are reproducible.
- Presentation slides are complete and technically accurate.
- Every member understands their contribution and can answer questions.

