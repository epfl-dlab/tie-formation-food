# tie-formation-food

This repository contains publicly available data and code for paper "Formation of Social Ties Influences Food Choice: A Campus-wide Longitudinal Study".
 
## The description of the data

### 1. Healthiness annotations.

In file */data/healthiness_annotations.xlsx*, the annotations of healthiness are available (0: likely to be healthy, 1: likely to be unhealthy, 2: unclassifiable).

### 2. Food item categorization.

File */data/categories.csv* contains category classification of food items.

## The description of the code

Although the transactional data cannot be made publicly available, data processing scripts and notebooks containing analyses and plotting code (Figures 1,2, 4-14, Tables 1 and 2) are available in the */code* folder. Contents:

*preprocessing_find_frequent_pairs.py*: The script for identifying frequent eating pairs by monitoring the queues.
*feature_extraction*: Notebook with code for feature extraction from raw transaction logs.
*descriptive.ipynb*: The notebook to produce Figures 1 and 2.
*seasonality.ipynb*: The notebook to produce Figure 5.
*matching.ipynb*: The pipeline for matched incident user design comparisons. Notebook to produce Figures 6, 7, 8, 9, and Table 1.
*sensitivity.R*: Script to compute gamma.
*pooled_analyses.ipynb*: Notebook to produce Figures 10, 11, 13, and Table 2.
*dose_response.ipynb*: Notebook to produce Figure 12 and difference-in-differences estimates.
*categories.ipynb*: Notebook to produce Figure 14.

## Reference

Please cite the paper when using the data:

**Formation of Social Ties Influences Food Choice: A Campus-Wide Longitudinal Study,** Kristina Gligori&#263;, Ryen W. White, Emre Kiciman, Eric Horvitz, Arnaud Chiolero, and Robert West. *Proc. ACM Hum.-Comput. Interact.5, CSCW1, Article 184 (April 2021)*
