
# Presentation 1 · Team plan

**Question:** How do chemical properties relate to activity against the pathogens in our MMV and DNDi data?

**Workflow:** Clean the data → plot distributions and relationships → explain findings → prepare slides.

**Presentation:** 10 minutes + 2–3 minutes Q&A.


## 1 · Who does what?

| Main responsibility | Team members | Deliverable |
|---|---|---|
| Examination, analysis and writing | **Claudia & Bashir** | Explain patterns, unusual values and limitations; write the findings |
| Distribution and relationship plots | **Zea & Eghosa** | Clear, labelled charts for the analysis and slides |
| Final review and rehearsal | **Everyone** | Agree on the conclusions and understand the cleaning decisions |

**Property sections** — each section is checked against all seven pathogen outcomes. These are topic assignments; the plotting and interpretation roles above apply across sections.

| Member | Section | Properties |
|---|---|---|
| Zea | Molecular size | `molecular_weight`, `heavy_atoms` |
| Eghosa | Lipophilicity & polar surface area | `logp`, `psa` |
| Bashir | Hydrogen-bond acceptors & donors | `hba`, `hbd` |
| Claudia | Flexibility, aromaticity & rule violations | `rtb`, `aromatic_rings`, `ro5_violations` |


## 2 · Prepare one shared dataset

- Read both files with **tab separation** then convert to CSV format.
- Fill missing properties using the **verified ChEMBL values** we recovered. Match by `chembl_id`; record the source and check matching property definitions.
- Combine the datasets, resolve the four overlapping compound IDs and retain MMV/DNDi source labels.
- Check numeric types, remaining missing values and unusual values. Investigate outliers before removing anything.
- For each property–activity pair, use rows with **both values present**. Do not remove rows because another pathogen is missing; never fill missing activity with zero.
- Agree on a shared cleaned version and record the row counts before and after cleaning.

**Activity conversion:** for confirmed IC50 in µM, `pIC50 = 6 − log10(IC50)`. Higher pIC50 means stronger inhibitory activity.

> **Check first:** the supplied extraction mixes IC50 and EC50 measurements. Verify the endpoint and units before labelling a value pIC50; confirmed EC50 becomes pEC50. Keep the original concentrations.


## 3 · Make the plots — Zea & Eghosa

| Plot | What to include |
|---|---|
| Distributions | All numeric columns; exclude `chembl_id`, `pref_name`, `smiles` and source labels. Include converted activity distributions. |
| Property vs. activity | Scatterplots for continuous properties; boxplots or jittered points for properties with few integer values. |
| Source comparison | Colour or separate MMV and DNDi to check whether patterns differ. Count shared compounds once in pooled results. |

**Every chart:** clear title, axis labels, units/activity scale and sample size (`n`). Use consistent colours. Split the plotting workload evenly and use the property sections above as the starting point.


## 4 · Examine and explain — Claudia & Bashir

For each property–pathogen pair:

1. **Describe the distribution:** typical values, spread, skew and unusual points.
2. **Examine the relationship:** increasing, decreasing, curved or no clear pattern? Calculate **Spearman correlation** alongside the plot.
3. **Check the explanation:** does the pattern also appear within each source, or depend on a few points or a small sample?
4. **Write 2–3 sentences:** what we see, what it might suggest and what limits the conclusion.

| Property / pathogen | n | Spearman correlation | What we see | Limitation |
|---|---:|---:|---|---|
| Fill in after analysis | | | | |

**Keep claims exploratory:** association is not causation. Report weak relationships too, and remember that correlation with pIC50 has the opposite direction to correlation with raw IC50.


## 5 · Build the presentation together

| Slides | Content | Time |
|---|---|---:|
| 1 | Research question and motivation | 1 min |
| 2 | Dataset, sources and team roles | 1 min |
| 3 | Cleaning, recovered values and final sample sizes | 2 min |
| 4–6 | Selected distributions and property–activity findings | 4 min |
| 7 | Ethics, limitations and next steps | 2 min |

**Ethics & limitations:** credit data sources; explain missingness, assay differences and small samples; do not claim laboratory activity proves treatment effectiveness.

- Zea & Eghosa provide the labelled plots.
- Claudia & Bashir add short interpretations beside them.
- Everyone selects the clearest findings and checks that charts support the wording.
- Assign speaking parts, rehearse to 10 minutes and practise Q&A.

**Keep the full analysis in our notebooks; show only the clearest findings in the slides.**

