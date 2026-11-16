# Course Guide: Machine Learning and Data Mining (MLDM)
**Instructors:** Prof. Matteo Golfarelli & teaching team  
**Key Milestone:** **December 16, 2026 – Official Exam Simulation**  
**Course Location:** [`Machine Learning and Data Mining M - Machine Learning and Data Mining/`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Machine%20Learning%20and%20Data%20Mining%20M%20-%20Machine%20Learning%20and%20Data%20Mining)

---

## 1. Course Architecture & Exam Profile

MLDM combines **enterprise data architecture and warehousing** with **rigorous algorithmic machine learning and hands-on Python/scikit-learn pipelines**.

The course consists of two complementary pillars:
1. **Data Mining & Architecture (Golfarelli Track)**: Conceptual modeling (DFM), data warehouse schemas, data lakes, and pattern extraction (Association Rules / Apriori).
2. **Machine Learning Foundations & Pipelines**: Supervised learning (classification, regression), unsupervised learning (clustering), model selection, evaluation, and end-to-end Python labs.

---

## 2. Topic Mastery Checklist

### Track A: Data Architecture & Data Mining
*Materials:* [`02 - Lecture Archives & Readings/Data Mining Lectures-20261105.zip`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Machine%20Learning%20and%20Data%20Mining%20M%20-%20Machine%20Learning%20and%20Data%20Mining/02%20-%20Lecture%20Archives%20&%20Readings/Data%20Mining%20Lectures-20261105.zip)

- [ ] **Data Warehousing & OLAP**:
  - Understand the operational vs informational data divide.
  - Star Schema vs Snowflake Schema vs Constellation. Fact tables vs Dimension tables.
  - Surrogate keys, slowly changing dimensions (SCD Types 1, 2, 3).
  - OLAP operations: Roll-up, Drill-down, Slice, Dice, Pivot.
- [ ] **Dimensional Fact Model (DFM)**:
  - Representing business facts graphically.
  - Fact attributes, dimensions, hierarchies, terminal nodes, and descriptive attributes.
  - Non-additive, semi-additive, and additive measures.
  - Shared hierarchies, cross-dimensional attributes, multiple arcs (overlapping dimensions).
- [ ] **Data Lake & Big Data Architectures**:
  - Raw (Bronze) $\to$ Curated / Cleaned (Silver) $\to$ Business-ready / Aggregated (Gold).
  - Schema-on-read vs Schema-on-write. Data pipelines and ingestion patterns.
  - Study the **NordicMart Case Study** (`01 - Workshops & Case Studies/05-NordicMart-voices from inside the company.pdf`).
- [ ] **CRISP-DM Process Model**:
  - The 6 phases: Business Understanding $\to$ Data Understanding $\to$ Data Preparation $\to$ Modeling $\to$ Evaluation $\to$ Deployment.
- [ ] **Association Rules & Frequent Itemset Mining**:
  - Transaction database format.
  - **Support**: $\text{supp}(X \to Y) = P(X \cup Y) = \frac{\sigma(X \cup Y)}{N}$
  - **Confidence**: $\text{conf}(X \to Y) = P(Y \mid X) = \frac{\sigma(X \cup Y)}{\sigma(X)}$
  - **Lift**: $\text{lift}(X \to Y) = \frac{P(X \cup Y)}{P(X)P(Y)} = \frac{\text{conf}(X \to Y)}{\text{supp}(Y)}$
  - **The Apriori Principle**: Downward-closure property of support (all non-empty subsets of a frequent itemset must also be frequent; if an itemset is infrequent, all its supersets are infrequent).
  - Using `mlxtend.frequent_patterns.apriori` and `association_rules`.

---

### Track B: Machine Learning & Statistical Learning
*Materials:* [`02 - Lecture Archives & Readings/Machine Learning Lectures-20261105.zip`](file:///c:/Users/Wilayat%20Hussain/Documents/UniBo/Machine%20Learning%20and%20Data%20Mining%20M%20-%20Machine%20Learning%20and%20Data%20Mining/02%20-%20Lecture%20Archives%20&%20Readings/Machine%20Learning%20Lectures-20261105.zip)

- [ ] **Decision Trees & Ensembles**:
  - Splitting criteria: Entropy ($H(S) = -\sum p_i \log_2 p_i$), Information Gain, Gini Impurity ($1 - \sum p_i^2$).
  - Overfitting: Minimum samples split, maximum depth, cost-complexity pruning ($\alpha$).
  - Random Forests: Bagging + random feature sub-sampling ($\sqrt{p}$ features). Out-of-Bag (OOB) error estimation.
  - Boosting: Sequential error correction (AdaBoost sample re-weighting, Gradient Boosting pseudo-residuals).
- [ ] **Evaluation Metrics & Cost of Errors**:
  - Confusion Matrix: $TP, FP, FN, TN$.
  - Precision ($\frac{TP}{TP+FP}$), Recall / Sensitivity ($\frac{TP}{TP+FN}$), Specificity ($\frac{TN}{TN+FP}$).
  - $F_\beta$-measure: $F_1 = 2 \cdot \frac{\text{Prec} \cdot \text{Rec}}{\text{Prec} + \text{Rec}}$.
  - Cohen's Kappa ($\kappa$): Inter-rater agreement corrected for chance agreement:
    $$\kappa = \frac{p_o - p_e}{1 - p_e}$$
  - Cost Matrices: Minimizing total monetary/operational cost rather than raw accuracy when false negatives are more expensive than false positives.
  - ROC Curves & Area Under Curve (AUC): Sensitivity vs (1 - Specificity) across all decision thresholds.
- [ ] **Model Selection & Preventing Data Leakage**:
  - Never fit scalers or imputers on the full dataset before splitting!
  - Cross-validation: K-Fold, Stratified K-Fold (for imbalanced classes).
  - Always wrap transformers and estimators inside `sklearn.pipeline.Pipeline`.
  - Hyperparameter optimization: `GridSearchCV` vs `RandomizedSearchCV`.
- [ ] **Regression & Regularization**:
  - Ordinary Least Squares (OLS) objective: $\min_w \|y - Xw\|_2^2$.
  - **Ridge Regression ($L_2$)**: Adds $\lambda \|w\|_2^2$. Shrinks weights smoothly; handles multicollinearity.
  - **Lasso Regression ($L_1$)**: Adds $\lambda \|w\|_1$. Drives unimportant weights to exact zero (performs automated feature selection).
  - **Elastic Net**: Combines $L_1$ and $L_2$ penalties with mixing parameter $\alpha$.
- [ ] **Clustering & Unsupervised Learning**:
  - **K-Means**: Lloyd's algorithm, K-Means++ initialization, minimizing Within-Cluster Sum of Squares (Inertia). Elbow method.
  - **Hierarchical Clustering**: Agglomerative bottom-up. Linkages: Single (min distance, chaining effect), Complete (max distance, compact spheres), Average, Ward (minimum variance increase). Dendrogram cutting.
  - **DBSCAN**: Density-based. Hyperparameters: $\epsilon$ (neighborhood radius) and $\text{MinPts}$. Points: Core points, Border points, Noise outliers. Handles arbitrary non-convex cluster shapes without pre-specifying $k$.
  - Evaluation: **Silhouette Coefficient** $s = \frac{b - a}{\max(a, b)}$ where $a$ is mean intra-cluster distance and $b$ is mean nearest-cluster distance.

---

## 3. Python Lab Mastery Blueprint

In the exam or lab tests, speed and syntax fluency in Python are critical. Practice building this boilerplate workflow from muscle memory:

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, cohen_kappa_score

# 1. Feature / Target Split
X = df.drop(columns=['target'])
y = df['target']

# 2. Preprocessor with ColumnTransformer (zero data leakage)
num_cols = X.select_dtypes(include=['int64', 'float64']).columns
cat_cols = X.select_dtypes(include=['object', 'category']).columns

preprocessor = ColumnTransformer(transformers=[
    ('num', StandardScaler(), num_cols),
    ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
])

# 3. Encapsulated Pipeline
pipe = Pipeline(steps=[
    ('prep', preprocessor),
    ('model', RandomForestClassifier(random_state=42))
])

# 4. Cross-Validated Grid Search
param_grid = {
    'model__n_estimators': [100, 200],
    'model__max_depth': [5, 10, None],
    'model__min_samples_leaf': [1, 3]
}
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
grid = GridSearchCV(pipe, param_grid, cv=cv, scoring='f1_macro', n_jobs=-1)

# 5. Fit & Evaluate
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
grid.fit(X_train, y_train)
y_pred = grid.predict(X_test)
print(classification_report(y_test, y_pred))
print("Cohen's Kappa:", cohen_kappa_score(y_test, y_pred))
```

---

## 4. December 16 Exam Simulation Protocol

On **December 16, 2026**, the course runs an official exam simulation in class:
1. Treat it with the exact conditions of the real exam: no notes, timed session, strict deadlines.
2. If any pipeline fails, note down the exact bug (e.g. dimensions mismatch, NaN handling, wrong metric passed to GridSearchCV).
3. Attend the follow-up review on **December 17, 2026** ("Comment on last lab") to understand the grading rubric.

