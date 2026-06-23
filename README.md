# MCS-LFSDP
Mechanism-Coupled Spectral Label-Free Software Defect Prediction: a mechanism-aware framework for identifying defect-prone software modules without target-project labels or labeled source projects.


## Datasets and Metrics

This repository uses four widely used benchmark dataset families for software defect prediction: ReLink, AEEEM, JIRA, and PROMISE. These datasets contain software modules described by static code metrics, process metrics, ownership metrics, change-history metrics, and dependency-related metrics. Defect labels are included only for evaluation purposes and are not used during the label-free construction of MCS-LFSDP.

### Dataset Sources

1. **ReLink Dataset**  
   Wu, Rongxin, et al. “Relink: recovering links between bugs and changes.”  
   *Proceedings of the 19th ACM SIGSOFT Symposium and the 13th European Conference on Foundations of Software Engineering*, 2011.

2. **AEEEM Dataset**  
   D’Ambros, Marco, Michele Lanza, and Romain Robbes. “Evaluating defect prediction approaches: a benchmark and an extensive comparison.”  
   *Empirical Software Engineering*, 17, 2012, pp. 531–577.

3. **JIRA Dataset**  
   Yatish, Suraj, et al. “Mining software defects: Should we consider affected releases?”  
   *2019 IEEE/ACM 41st International Conference on Software Engineering (ICSE)*, IEEE, 2019.

4. **PROMISE Dataset**  
   T. Menzies, R. Krishna, and D. Pryor. “The PROMISE Repository of Empirical Software Engineering Data,” 2015.

### Dataset Folder

The `datasets/` folder contains the benchmark datasets used in this study. Each dataset family contains one or more software projects with module-level software metrics and defect labels.

The defect labels are used only after prediction to evaluate performance. They are not used during preprocessing decisions, mechanism construction, detector scoring, reliability estimation, graph refinement, anchor discovery, thresholding, or prioritization.

### Metric Details

The metric descriptions for each dataset family are provided below.

#### ReLink Dataset Metrics

| Abbreviation | Description |
|---|---|
| AvgCyclomatic | Average Cyclomatic Complexity |
| AvgCyclomaticModified | Average Modified Cyclomatic Complexity |
| AvgCyclomaticStrict | Average Strict Cyclomatic Complexity |
| AvgEssential | Average Essential Complexity |
| AvgLine | Average Lines |
| AvgLineBlank | Average Blank Lines |
| AvgLineCode | Average Code Lines |
| AvgLineComment | Average Comment Lines |
| CountLine | Number of Lines |
| CountLineBlank | Number of Blank Lines |
| CountLineCode | Number of Code Lines |
| CountLineCodeDecl | Number of Declarative Code Lines |
| CountLineCodeExe | Number of Executable Code Lines |
| CountLineComment | Number of Comment Lines |
| CountSemicolon | Number of Semicolons |
| CountStmt | Number of Statements |
| CountStmtDecl | Number of Declarative Statements |
| CountStmtExe | Number of Executable Statements |
| MaxCyclomatic | Maximum Cyclomatic Complexity of all nested functions |
| MaxCyclomaticModified | Maximum Modified Cyclomatic Complexity of all nested functions |
| MaxCyclomaticStrict | Maximum Strict Cyclomatic Complexity of all nested functions |
| RatioCommentToCode | Ratio of Comment Lines to Code Lines |
| SumCyclomatic | Sum of Cyclomatic Complexity of all nested functions |
| SumCyclomaticModified | Sum of Modified Cyclomatic Complexity of all nested functions |
| SumCyclomaticStrict | Sum of Strict Cyclomatic Complexity of all nested functions |
| SumEssential | Sum of Essential Complexity of all nested functions |

#### AEEEM Dataset Metrics

| Abbreviation | Description |
|---|---|
| ck_oo_wmc | Weighted method count |
| ck_oo_dit | Depth of inheritance tree |
| ck_oo_rfc | Response for class |
| ck_oo_noc | Number of children |
| ck_oo_cbo | Coupling between objects |
| ck_oo_lcom | Lack of cohesion in methods |
| ck_oo_fanin | Number of other classes that reference the class |
| ck_oo_fanout | Number of other classes referenced by the class |
| ck_oo_noa | Number of attributes |
| ck_oo_nopa | Number of public attributes |
| ck_oo_nopra | Number of private attributes |
| ck_oo_noai | Number of attributes inherited |
| ck_oo_loc | Number of lines of code |
| ck_oo_nom | Number of methods |
| ck_oo_nopm | Number of public methods |
| ck_oo_noprm | Number of private methods |
| ck_oo_nomt | Number of methods inherited |
| WCHU_wmc | Weighted churn of weighted method count |
| WCHU_dit | Weighted churn of depth of inheritance tree |
| WCHU_rfc | Weighted churn of response for class |
| WCHU_noc | Weighted churn of number of children |
| WCHU_cbo | Weighted churn of coupling between objects |
| WCHU_lcom | Weighted churn of lack of cohesion in methods |
| WCHU_fanin | Weighted churn of number of other classes that reference the class |
| WCHU_fanout | Weighted churn of number of other classes referenced by the class |
| WCHU_noa | Weighted churn of number of attributes |
| WCHU_nopa | Weighted churn of number of public attributes |
| WCHU_nopra | Weighted churn of number of private attributes |
| WCHU_noai | Weighted churn of number of attributes inherited |
| WCHU_loc | Weighted churn of number of lines of code |
| WCHU_nom | Weighted churn of number of methods |
| WCHU_nopm | Weighted churn of number of public methods |
| WCHU_noprm | Weighted churn of number of private methods |
| WCHU_nomt | Weighted churn of number of methods inherited |
| LDHH_wmc | Linear decayed history entropy of weighted method count |
| LDHH_dit | Linear decayed history entropy of depth of inheritance tree |
| LDHH_rfc | Linear decayed history entropy of response for class |
| LDHH_noc | Linear decayed history entropy of number of children |
| LDHH_cbo | Linear decayed history entropy of coupling between objects |
| LDHH_lcom | Linear decayed history entropy of lack of cohesion in methods |
| LDHH_fanin | Linear decayed history entropy of number of other classes that reference the class |
| LDHH_fanout | Linear decayed history entropy of number of other classes referenced by the class |
| LDHH_noa | Linear decayed history entropy of number of attributes |
| LDHH_nopa | Linear decayed history entropy of number of public attributes |
| LDHH_nopra | Linear decayed history entropy of number of private attributes |
| LDHH_noai | Linear decayed history entropy of number of attributes inherited |
| LDHH_loc | Linear decayed history entropy of number of lines of code |
| LDHH_nom | Linear decayed history entropy of number of methods |
| LDHH_nopm | Linear decayed history entropy of number of public methods |
| LDHH_noprm | Linear decayed history entropy of number of private methods |
| LDHH_nomt | Linear decayed history entropy of number of methods inherited |
| CvsEntropy | Entropy of CVS change log |
| CvsWEntropy | Weighted Entropy of CVS change log |
| CvsLogEntropy | Logarithmic Entropy of CVS change log |
| CvsExpEntropy | Exponential Entropy of CVS change log |
| CvsLinEntropy | Linear Entropy of CVS change log |
| numberOfNonTrivialBugsFoundUntil | Number of non-trivial bugs found until the corresponding fix |
| numberOfCriticalBugsFoundUntil | Number of critical bugs found until the corresponding fix |
| numberOfHighPriorityBugsFoundUntil | Number of high priority bugs found until the corresponding fix |
| numberOfMajorBugsFoundUntil | Number of major bugs found until the corresponding fix |
| numberOfBugsFoundUntil | Number of bugs found until the corresponding fix |

#### JIRA Dataset Metrics

| Abbreviation | Description |
|---|---|
| AvgCyclomatic | Average cyclomatic complexity for all nested functions or methods |
| SumCyclomatic | Sum of cyclomatic complexity of all nested functions or methods |
| AvgCyclomaticModified | Average modified cyclomatic complexity for all nested functions or methods |
| SumCyclomaticModified | Sum of modified cyclomatic complexity of all nested functions |
| AvgCyclomaticStrict | Average strict cyclomatic complexity for all nested functions or methods |
| SumCyclomaticStrict | Sum of strict cyclomatic complexity of all nested functions or methods |
| AvgEssential | Average essential complexity for all nested functions or methods |
| SumEssential | Sum of essential complexity for all nested functions or methods |
| AvgLine | Average number of lines for all nested functions or methods |
| AvgLineBlank | Average number of blank lines for all nested functions or methods |
| AvgLineCode | Average number of lines containing source code for all nested functions |
| AvgLineComment | Average number of comment lines for all nested functions or methods |
| CountClassBase | Number of immediate base classes |
| CountClassCoupled | Number of other classes coupled to |
| CountClassDerived | Number of immediate subclasses |
| MaxInheritanceTree | Maximum depth of class in inheritance tree |
| PercentLackOfCohesion | 100% minus the average cohesion for package entities |
| CountDeclClass | Number of classes |
| CountDeclClassMethod | Number of class methods |
| CountDeclClassVariable | Number of class variables |
| CountDeclFunction | Number of functions |
| CountDeclInstanceMethod | Number of instance methods |
| CountDeclInstanceVariable | Number of instance variables |
| CountDeclMethod | Number of local non-inherited methods |
| CountDeclMethodDefault | Number of local default methods |
| CountDeclMethodPrivate | Number of local non-inherited private methods |
| CountDeclMethodProtected | Number of local protected methods |
| CountDeclMethodPublic | Number of local non-inherited public methods |
| CountLine | Number of physical lines |
| CountLineBlank | Number of blank lines |
| CountLineCode | Number of lines containing source code |
| CountLineCodeDecl | Number of lines containing declarative source code |
| CountLineCodeExe | Number of lines containing executable source code |
| CountLineComment | Number of lines containing comment |
| CountSemicolon | Number of semicolons |
| CountStmt | Number of statements |
| CountStmtDecl | Number of declarative statements |
| CountStmtExe | Number of executable statements |
| MaxCyclomatic | Maximum cyclomatic complexity of all nested functions or methods |
| MaxCyclomaticModified | Maximum modified cyclomatic complexity of nested functions or methods |
| MaxCyclomaticStrict | Maximum strict cyclomatic complexity of nested functions or methods |
| RatioCommentToCode | Ratio of comment lines to code lines |
| CountInput_Min | Minimum number of calling subprograms plus global variables read |
| CountInput_Mean | Mean number of calling subprograms plus global variables read |
| CountInput_Max | Maximum number of calling subprograms plus global variables read |
| CountOutput_Min | Minimum number of called subprograms plus global variables set |
| CountOutput_Mean | Mean number of called subprograms plus global variables set |
| CountOutput_Max | Maximum number of called subprograms plus global variables set |
| CountPath_Min | Minimum number of unique paths through a body of code |
| CountPath_Mean | Mean number of unique paths through a body of code |
| CountPath_Max | Maximum number of unique paths through a body of code |
| MaxNesting_Min | Minimum of maximum nesting level of control constructs in the function |
| MaxNesting_Mean | Mean of maximum nesting level of control constructs in the function |
| MaxNesting_Max | Maximum of maximum nesting level of control constructs in the function |
| COMM | Number of Git commits |
| ADDED_LINES | Normalized number of lines added to the module |
| DEL_LINES | Normalized number of lines deleted from the module |
| ADEV | Number of active developers |
| DDEV | Number of distinct developers |
| MINOR_COMMIT | Developers contributing less than 5% of total code changes |
| MINOR_LINE | Developers contributing less than 5% of total LOC |
| MAJOR_COMMIT | Developers contributing more than 5% of total code changes |
| MAJOR_LINES | Developers contributing more than 5% of total LOC |
| OWN_COMMIT | Proportion of code changes by top contributor |
| OWN_LINE | Proportion of lines of code by top contributor |

#### PROMISE Dataset Metrics

| Abbreviation | Description |
|---|---|
| WMC | Weighted Methods per Class |
| DIT | Depth of Inheritance Tree |
| NOC | Number of Children |
| CBO | Coupling Between Object Classes |
| RFC | Response for a Class |
| LCOM | Lack of Cohesion in Methods |
| CA | Afferent Couplings |
| CE | Efferent Couplings |
| NPM | Number of Public Methods |
| LCOM3 | Lack of Cohesion in Methods variant |
| LOC | Lines of Code |
| DAM | Data Access Metric |
| MOA | Measure of Aggregation |
| MFA | Measure of Functional Abstraction |
| CAM | Cohesion Among Methods of a Class |
| IC | Inheritance Coupling |
| CBM | Coupling Between Methods |
| AMC | Average Method Complexity |
| CC | McCabe’s Cyclomatic Complexity |
| MAX_CC | Maximum Value of CC Among Methods in the Class |
| AVG_CC | Average Arithmetic Mean CC of Methods in the Class |



## Metric-to-Mechanism Mapping

MCS-LFSDP organizes dataset metrics into software-engineering mechanism views. The mapping is fixed using metric definitions and dataset characteristics. Defect labels are not used to define or activate mechanism views.

| Symbol | Mechanism View | General Meaning |
|---|---|---|
| `B` | Structural Burden | Size, complexity, cohesion, coupling, inheritance, and implementation burden |
| `I` | Evolutionary Instability | Change, churn, entropy, history, and instability-related evidence |
| `C` | Coordination Complexity | Developer, ownership, contribution, maintenance, and coordination-related evidence |
| `E` | Dependency Exposure | Dependency, fan-in/fan-out, inheritance, coupling, and reference exposure |

A metric may be associated with more than one mechanism when its definition supports multiple interpretations.

---

## Mechanism Views by Dataset Family

| Dataset Family | Active Mechanism Views |
|---|---|
| AEEEM | `B`, `I`, `C` |
| JIRA | `B`, `I`, `C`, `E` |
| PROMISE | `B`, `E` |
| ReLink | `B`, `I`, `C` |

---

## ReLink Metric-to-Mechanism Mapping

The ReLink dataset mainly contains static source-code metrics. In MCS-LFSDP, these metrics are organized into structural, instability-related, and coordination/maintainability-related views.

| Mechanism | Metrics |
|---|---|
| `B` Structural Burden | AvgCyclomatic, AvgCyclomaticModified, AvgCyclomaticStrict, AvgEssential, AvgLine, AvgLineBlank, AvgLineCode, AvgLineComment, CountLine, CountLineBlank, CountLineCode, CountLineCodeDecl, CountLineCodeExe, CountLineComment, CountSemicolon, CountStmt, CountStmtDecl, CountStmtExe, MaxCyclomatic, MaxCyclomaticModified, MaxCyclomaticStrict, SumCyclomatic, SumCyclomaticModified, SumCyclomaticStrict, SumEssential |
| `I` Evolutionary Instability | AvgCyclomaticModified, AvgCyclomaticStrict, AvgEssential, MaxCyclomaticModified, MaxCyclomaticStrict, SumCyclomaticModified, SumCyclomaticStrict, SumEssential |
| `C` Coordination Complexity | AvgLineComment, CountLineComment, RatioCommentToCode, CountStmtDecl, CountStmtExe, CountLineCodeDecl, CountLineCodeExe |

---

## AEEEM Metric-to-Mechanism Mapping

The AEEEM dataset contains static object-oriented metrics, churn/history metrics, entropy metrics, and bug-history metrics.

| Mechanism | Metrics |
|---|---|
| `B` Structural Burden | ck_oo_wmc, ck_oo_dit, ck_oo_rfc, ck_oo_noc, ck_oo_cbo, ck_oo_lcom, ck_oo_fanin, ck_oo_fanout, ck_oo_noa, ck_oo_nopa, ck_oo_nopra, ck_oo_noai, ck_oo_loc, ck_oo_nom, ck_oo_nopm, ck_oo_noprm, ck_oo_nomt |
| `I` Evolutionary Instability | WCHU_wmc, WCHU_dit, WCHU_rfc, WCHU_noc, WCHU_cbo, WCHU_lcom, WCHU_fanin, WCHU_fanout, WCHU_noa, WCHU_nopa, WCHU_nopra, WCHU_noai, WCHU_loc, WCHU_nom, WCHU_nopm, WCHU_noprm, WCHU_nomt, LDHH_wmc, LDHH_dit, LDHH_rfc, LDHH_noc, LDHH_cbo, LDHH_lcom, LDHH_fanin, LDHH_fanout, LDHH_noa, LDHH_nopa, LDHH_nopra, LDHH_noai, LDHH_loc, LDHH_nom, LDHH_nopm, LDHH_noprm, LDHH_nomt, CvsEntropy, CvsWEntropy, CvsLogEntropy, CvsExpEntropy, CvsLinEntropy |
| `C` Coordination Complexity | numberOfNonTrivialBugsFoundUntil, numberOfCriticalBugsFoundUntil, numberOfHighPriorityBugsFoundUntil, numberOfMajorBugsFoundUntil, numberOfBugsFoundUntil |

---

## JIRA Metric-to-Mechanism Mapping

The JIRA dataset contains static code metrics, process/change metrics, developer/ownership metrics, and dependency-related metrics. Therefore, all four mechanism views are available.

| Mechanism | Metrics |
|---|---|
| `B` Structural Burden | AvgCyclomatic, SumCyclomatic, AvgCyclomaticModified, SumCyclomaticModified, AvgCyclomaticStrict, SumCyclomaticStrict, AvgEssential, SumEssential, AvgLine, AvgLineBlank, AvgLineCode, AvgLineComment, CountDeclClass, CountDeclClassMethod, CountDeclClassVariable, CountDeclFunction, CountDeclInstanceMethod, CountDeclInstanceVariable, CountDeclMethod, CountDeclMethodDefault, CountDeclMethodPrivate, CountDeclMethodProtected, CountDeclMethodPublic, CountLine, CountLineBlank, CountLineCode, CountLineCodeDecl, CountLineCodeExe, CountLineComment, CountSemicolon, CountStmt, CountStmtDecl, CountStmtExe, MaxCyclomatic, MaxCyclomaticModified, MaxCyclomaticStrict, RatioCommentToCode, CountPath_Min, CountPath_Mean, CountPath_Max, MaxNesting_Min, MaxNesting_Mean, MaxNesting_Max, PercentLackOfCohesion |
| `I` Evolutionary Instability | COMM, ADDED_LINES, DEL_LINES |
| `C` Coordination Complexity | ADEV, DDEV, MINOR_COMMIT, MINOR_LINE, MAJOR_COMMIT, MAJOR_LINES, OWN_COMMIT, OWN_LINE |
| `E` Dependency Exposure | CountClassBase, CountClassCoupled, CountClassDerived, MaxInheritanceTree, CountInput_Min, CountInput_Mean, CountInput_Max, CountOutput_Min, CountOutput_Mean, CountOutput_Max |

---

## PROMISE Metric-to-Mechanism Mapping

The PROMISE dataset mainly contains static object-oriented software metrics. In MCS-LFSDP, these metrics support structural burden and dependency exposure views.

| Mechanism | Metrics |
|---|---|
| `B` Structural Burden | WMC, DIT, NOC, CBO, RFC, LCOM, CA, CE, NPM, LCOM3, LOC, DAM, MOA, MFA, CAM, IC, CBM, AMC, CC, MAX_CC, AVG_CC |
| `E` Dependency Exposure | DIT, NOC, CBO, RFC, CA, CE, IC, CBM |



## Experimental Results

Higher values are better for **AUC**, **MCC**, and **Popt@20**. Lower values are better for **IFA**.


### Performance of MCS-LFSDP and Unsupervised Baselines in Terms of AUC and MCC


| Target           |   AUC — MCS-LFSDP |   CLA |   CLAMI |   K-means |   K-medoids |   Manual UP |   Manual Down |   MUSDP |   TCL |   TCLP |   MCC — MCS-LFSDP |   CLA |   CLAMI |   K-means |   K-medoids |   Manual UP |   Manual Down |   MUSDP |   TCL |   TCLP |
|:-----------------|------------------:|------:|--------:|----------:|------------:|------------:|--------------:|--------:|------:|-------:|------------------:|------:|--------:|----------:|------------:|------------:|--------------:|--------:|------:|-------:|
| Activemq-5.0.0   |              0.82 |  0.80 |    0.81 |      0.66 |        0.68 |        0.70 |          0.74 |    0.80 |  0.83 |   0.74 |              0.39 |  0.45 |    0.43 |      0.13 |        0.15 |        0.16 |          0.29 |    0.48 |  0.38 |   0.35 |
| Camel-2.10.0     |              0.84 |  0.76 |    0.79 |      0.68 |        0.69 |        0.70 |          0.72 |    0.81 |  0.82 |   0.79 |              0.22 |  0.16 |    0.16 |      0.00 |        0.02 |       -0.01 |          0.08 |    0.21 |  0.19 |   0.19 |
| Derby-10.2.1.6   |              0.80 |  0.79 |    0.78 |      0.64 |        0.65 |        0.70 |          0.74 |    0.59 |  0.78 |   0.65 |              0.38 |  0.34 |    0.35 |      0.05 |        0.06 |        0.15 |          0.29 |    0.03 |  0.33 |   0.30 |
| Groovy-1.5.7     |              0.78 |  0.74 |    0.76 |      0.56 |        0.58 |        0.66 |          0.73 |    0.80 |  0.84 |   0.80 |              0.16 |  0.12 |    0.14 |     -0.05 |       -0.03 |       -0.02 |          0.10 |    0.34 |  0.21 |   0.22 |
| HBase-0.94.0     |              0.75 |  0.70 |    0.73 |      0.58 |        0.60 |        0.65 |          0.69 |    0.63 |  0.74 |   0.65 |              0.33 |  0.28 |    0.30 |     -0.01 |        0.00 |        0.07 |          0.20 |    0.03 |  0.26 |   0.27 |
| Hive-0.10.0      |              0.81 |  0.77 |    0.79 |      0.61 |        0.63 |        0.69 |          0.74 |    0.80 |  0.80 |   0.74 |              0.30 |  0.29 |    0.27 |     -0.01 |        0.00 |        0.05 |          0.19 |    0.33 |  0.35 |   0.32 |
| Jruby-1.1        |              0.91 |  0.79 |    0.82 |      0.61 |        0.64 |        0.69 |          0.76 |    0.82 |  0.86 |   0.80 |              0.48 |  0.43 |    0.44 |      0.08 |        0.10 |        0.14 |          0.29 |    0.35 |  0.45 |   0.40 |
| Lucene-2.3.0     |              0.83 |  0.81 |    0.83 |      0.63 |        0.66 |        0.71 |          0.75 |    0.84 |  0.78 |   0.60 |              0.37 |  0.41 |    0.51 |      0.04 |        0.07 |        0.17 |          0.31 |    0.39 |  0.22 |   0.18 |
| Wicket-1.3.0.a-1 |              0.89 |  0.82 |    0.85 |      0.63 |        0.66 |        0.72 |          0.77 |    0.80 |  0.86 |   0.77 |              0.33 |  0.31 |    0.32 |      0.01 |        0.03 |        0.08 |          0.21 |    0.26 |  0.31 |   0.25 |
| Ant-1.7          |              0.75 |  0.68 |    0.72 |      0.63 |        0.65 |        0.62 |          0.82 |    0.72 |  0.74 |   0.73 |              0.35 |  0.26 |    0.28 |      0.14 |        0.20 |        0.02 |          0.38 |    0.19 |  0.33 |   0.37 |
| Camel-1.0        |              0.84 |  0.77 |    0.79 |      0.63 |        0.69 |        0.69 |          0.72 |    0.54 |  0.72 |   0.70 |              0.20 |  0.13 |    0.17 |     -0.01 |        0.04 |       -0.02 |          0.06 |    0.11 |  0.16 |   0.17 |
| Forrest-0.8      |              0.60 |  0.64 |    0.67 |      0.85 |        0.62 |        0.59 |          0.74 |    0.78 |  0.62 |   0.60 |              0.05 |  0.18 |    0.11 |      0.22 |        0.05 |       -0.07 |          0.06 |   -0.05 |  0.16 |   0.03 |
| Ivy-1.1          |              0.65 |  0.62 |    0.63 |      0.50 |        0.52 |        0.58 |          0.72 |    0.62 |  0.64 |   0.66 |              0.22 |  0.19 |    0.21 |      0.00 |        0.01 |       -0.01 |          0.14 |    0.15 |  0.12 |   0.21 |
| Jedit-4.1        |              0.78 |  0.67 |    0.70 |      0.51 |        0.52 |        0.60 |          0.76 |    0.72 |  0.75 |   0.74 |              0.34 |  0.28 |    0.32 |     -0.06 |       -0.06 |        0.03 |          0.39 |    0.18 |  0.28 |   0.38 |
| Lucene-2.4       |              0.70 |  0.60 |    0.63 |      0.52 |        0.55 |        0.59 |          0.62 |    0.61 |  0.68 |   0.63 |              0.31 |  0.20 |    0.23 |     -0.13 |       -0.03 |       -0.01 |          0.13 |    0.06 |  0.24 |   0.22 |
| Synapse-1.1      |              0.66 |  0.67 |    0.69 |      0.65 |        0.64 |        0.62 |          0.66 |    0.68 |  0.64 |   0.63 |              0.32 |  0.20 |    0.23 |      0.32 |        0.11 |       -0.01 |          0.15 |    0.17 |  0.18 |   0.24 |
| Velocity-1.6     |              0.69 |  0.59 |    0.60 |      0.51 |        0.52 |        0.57 |          0.60 |    0.65 |  0.55 |   0.66 |              0.27 |  0.18 |    0.18 |     -0.14 |       -0.11 |       -0.08 |          0.18 |    0.12 |  0.17 |   0.25 |
| Xalan-2.6        |              0.64 |  0.60 |    0.60 |      0.47 |        0.47 |        0.51 |          0.69 |    0.63 |  0.62 |   0.60 |              0.25 |  0.16 |    0.20 |      0.04 |        0.01 |       -0.05 |          0.31 |    0.10 |  0.23 |   0.20 |
| Xerces-1.3       |              0.77 |  0.70 |    0.72 |      0.57 |        0.61 |        0.63 |          0.70 |    0.69 |  0.75 |   0.66 |              0.25 |  0.15 |    0.18 |     -0.05 |        0.00 |       -0.04 |          0.23 |    0.17 |  0.23 |   0.21 |
| Apache           |              0.64 |  0.62 |    0.62 |      0.49 |        0.51 |        0.56 |          0.58 |    0.63 |  0.58 |   0.60 |              0.20 |  0.15 |    0.16 |     -0.18 |       -0.17 |       -0.07 |          0.09 |    0.16 |  0.19 |   0.17 |
| Safe             |              0.74 |  0.63 |    0.66 |      0.84 |        0.86 |        0.60 |          0.64 |    0.68 |  0.70 |   0.72 |              0.34 |  0.16 |    0.18 |      0.27 |        0.27 |       -0.04 |          0.25 |    0.32 |  0.27 |   0.49 |
| ZXing            |              0.62 |  0.58 |    0.58 |      0.52 |        0.51 |        0.53 |          0.53 |    0.62 |  0.57 |   0.58 |              0.21 |  0.12 |    0.14 |      0.12 |        0.02 |       -0.11 |          0.12 |    0.17 |  0.15 |   0.11 |
| Equinox          |              0.65 |  0.76 |    0.77 |      0.60 |        0.64 |        0.66 |          0.75 |    0.70 |  0.79 |   0.74 |              0.31 |  0.34 |    0.26 |      0.04 |        0.08 |        0.05 |          0.40 |    0.28 |  0.33 |   0.26 |
| Jdt              |              0.76 |  0.72 |    0.76 |      0.57 |        0.65 |        0.66 |          0.73 |    0.68 |  0.75 |   0.63 |              0.35 |  0.30 |    0.31 |      0.05 |        0.18 |        0.11 |          0.31 |    0.24 |  0.29 |   0.20 |
| Lucene           |              0.78 |  0.71 |    0.73 |      0.61 |        0.60 |        0.63 |          0.70 |    0.68 |  0.77 |   0.76 |              0.30 |  0.21 |    0.26 |      0.04 |        0.07 |        0.01 |          0.16 |    0.17 |  0.29 |   0.26 |
| Mylyn            |              0.69 |  0.61 |    0.62 |      0.61 |        0.60 |        0.59 |          0.63 |    0.45 |  0.68 |   0.64 |              0.19 |  0.15 |    0.12 |      0.03 |        0.06 |       -0.06 |          0.06 |   -0.01 |  0.18 |   0.17 |
| Pde              |              0.68 |  0.67 |    0.71 |      0.63 |        0.64 |        0.64 |          0.68 |    0.68 |  0.60 |   0.68 |              0.21 |  0.28 |    0.12 |      0.12 |        0.09 |        0.05 |          0.20 |    0.22 |  0.15 |   0.23 |
| Average          |              0.74 |  0.70 |    0.72 |      0.60 |        0.61 |        0.63 |          0.70 |    0.69 |  0.72 |   0.69 |              0.28 |  0.24 |    0.24 |      0.04 |        0.05 |        0.02 |          0.21 |    0.19 |  0.25 |   0.25 |



### Effort-Aware Performance Summary Over 27 Projects


| Method      |   Popt@20 Mean |   Popt@20 Avg. Rank |   IFA Mean |   IFA Avg. Rank |
|:------------|---------------:|--------------------:|-----------:|----------------:|
| MCS-LFSDP   |           0.53 |                1.48 |       0.61 |            1.30 |
| CLA         |           0.49 |                5.70 |       0.63 |            4.06 |
| CLAMI       |           0.44 |                7.41 |       1.19 |            5.32 |
| K-means     |           0.49 |                5.06 |      10.15 |            6.50 |
| K-medoids   |           0.52 |                4.13 |      16.97 |            8.04 |
| Manual UP   |           0.52 |                5.04 |      32.88 |            8.91 |
| Manual Down |           0.35 |                8.54 |       2.67 |            6.43 |
| MUSDP       |           0.51 |                4.63 |       4.37 |            6.26 |
| TCL         |           0.46 |                6.67 |       0.64 |            3.91 |
| TCLP        |           0.46 |                6.35 |       1.11 |            4.30 |



### Comparison with Label-Using Reference Models


| Method    |   AUC |   MCC |   Popt@20 |   IFA |
|:----------|------:|------:|----------:|------:|
| MCS-LFSDP |  0.74 |  0.28 |      0.53 |  0.61 |
| BurakMHD  |  0.71 |  0.23 |      0.51 |  0.63 |
| DANN      |  0.59 |  0.21 |      0.53 | 22.90 |
| CFPS      |  0.73 |  0.25 |      0.50 |  1.22 |
| SSE       |  0.68 |  0.22 |      0.54 |  1.90 |
| DMDA      |  0.70 |  0.25 |      0.49 |  1.22 |



### Performance of Formulation-Level Variants by Target


| Target                         |   MCS AUC |   MCS MCC |   MCS Popt@20 |   MCS IFA |   Coupled AUC |   Coupled MCC |   Coupled Popt@20 |   Coupled IFA |   Graph AUC |   Graph MCC |   Graph Popt@20 |   Graph IFA |   Consensus AUC |   Consensus MCC |   Consensus Popt@20 |   Consensus IFA |   Raw-Graph AUC |   Raw-Graph MCC |   Raw-Graph Popt@20 |   Raw-Graph IFA |
|:-------------------------------|----------:|----------:|--------------:|----------:|--------------:|--------------:|------------------:|--------------:|------------:|------------:|----------------:|------------:|----------------:|----------------:|--------------------:|----------------:|----------------:|----------------:|--------------------:|----------------:|
| Activemq-5.0.0                 |      0.82 |      0.39 |          0.77 |      0.00 |          0.75 |          0.30 |              0.71 |          0.00 |        0.75 |        0.31 |            0.69 |        0.00 |            0.75 |            0.30 |                0.71 |            0.00 |            0.75 |            0.32 |                0.68 |            0.00 |
| Camel-2.10.0                   |      0.84 |      0.22 |          0.83 |      0.90 |          0.80 |          0.18 |              0.78 |          0.80 |        0.82 |        0.18 |            0.76 |        0.80 |            0.80 |            0.18 |                0.78 |            0.80 |            0.80 |            0.17 |                0.76 |            0.80 |
| Derby-10.2.1.6                 |      0.80 |      0.38 |          0.64 |      0.00 |          0.75 |          0.34 |              0.57 |          0.00 |        0.77 |        0.37 |            0.57 |        0.00 |            0.75 |            0.34 |                0.57 |            0.00 |            0.75 |            0.36 |                0.55 |            0.00 |
| Groovy-1_5_7                   |      0.78 |      0.16 |          0.75 |      0.00 |          0.74 |          0.16 |              0.70 |          0.00 |        0.75 |        0.14 |            0.69 |        0.00 |            0.74 |            0.14 |                0.70 |            0.00 |            0.74 |            0.17 |                0.68 |            0.00 |
| Hbase-0.94.0                   |      0.75 |      0.33 |          0.65 |      0.20 |          0.71 |          0.25 |              0.61 |          0.00 |        0.73 |        0.27 |            0.61 |        0.00 |            0.71 |            0.25 |                0.61 |            0.00 |            0.70 |            0.24 |                0.58 |            0.00 |
| Hive-0.10.0                    |      0.81 |      0.30 |          0.74 |      0.20 |          0.80 |          0.32 |              0.73 |          0.00 |        0.81 |        0.32 |            0.71 |        0.00 |            0.80 |            0.32 |                0.73 |            0.00 |            0.80 |            0.31 |                0.71 |            0.00 |
| Jruby-1.1                      |      0.91 |      0.48 |          0.85 |      0.00 |          0.86 |          0.45 |              0.79 |          0.00 |        0.88 |        0.45 |            0.78 |        0.00 |            0.86 |            0.45 |                0.79 |            0.00 |            0.74 |            0.36 |                0.75 |            0.00 |
| Lucene-2.3.0                   |      0.83 |      0.37 |          0.69 |      0.00 |          0.77 |          0.31 |              0.61 |          0.00 |        0.79 |        0.31 |            0.61 |        0.00 |            0.77 |            0.30 |                0.60 |            0.00 |            0.76 |            0.30 |                0.59 |            0.00 |
| Wicket-1.3.0-incubating-beta-1 |      0.89 |      0.33 |          0.82 |      0.00 |          0.83 |          0.29 |              0.75 |          0.00 |        0.85 |        0.29 |            0.74 |        0.00 |            0.83 |            0.28 |                0.75 |            0.00 |            0.82 |            0.27 |                0.72 |            0.00 |
| Ant-1.7                        |      0.75 |      0.35 |          0.46 |      0.00 |          0.73 |          0.33 |              0.42 |          0.00 |        0.74 |        0.34 |            0.41 |        0.00 |            0.73 |            0.33 |                0.42 |            0.00 |            0.72 |            0.32 |                0.40 |            0.00 |
| Camel-1.0                      |      0.84 |      0.20 |          0.68 |      3.53 |          0.80 |          0.21 |              0.63 |          3.80 |        0.81 |        0.20 |            0.61 |        4.00 |            0.80 |            0.19 |                0.62 |            4.00 |            0.78 |            0.18 |                0.61 |            3.80 |
| Forrest-0.8                    |      0.60 |      0.05 |          0.44 |      6.87 |          0.52 |         -0.01 |              0.38 |          8.20 |        0.51 |        0.08 |            0.36 |        7.90 |            0.52 |           -0.01 |                0.38 |            8.20 |            0.51 |           -0.02 |                0.36 |            8.60 |
| Ivy-1.1                        |      0.65 |      0.22 |          0.23 |      0.00 |          0.62 |          0.22 |              0.23 |          0.00 |        0.62 |        0.16 |            0.22 |        0.00 |            0.62 |            0.23 |                0.23 |            0.00 |            0.61 |            0.21 |                0.22 |            0.00 |
| Jedit-4.1                      |      0.78 |      0.34 |          0.39 |      0.00 |          0.73 |          0.30 |              0.36 |          0.00 |        0.74 |        0.28 |            0.37 |        0.00 |            0.73 |            0.26 |                0.36 |            0.00 |            0.72 |            0.33 |                0.35 |            0.00 |
| Lucene-2.4                     |      0.70 |      0.31 |          0.31 |      0.00 |          0.66 |          0.26 |              0.32 |          0.00 |        0.67 |        0.25 |            0.32 |        0.00 |            0.66 |            0.24 |                0.32 |            0.00 |            0.65 |            0.23 |                0.30 |            0.00 |
| Synapse-1.1                    |      0.66 |      0.32 |          0.48 |      1.73 |          0.64 |          0.24 |              0.46 |          1.60 |        0.63 |        0.29 |            0.44 |        1.80 |            0.64 |            0.23 |                0.46 |            1.60 |            0.63 |            0.22 |                0.43 |            1.80 |
| Velocity-1.6                   |      0.69 |      0.27 |          0.33 |      0.00 |          0.65 |          0.20 |              0.30 |          0.00 |        0.66 |        0.23 |            0.29 |        0.00 |            0.65 |            0.19 |                0.29 |            0.00 |            0.64 |            0.20 |                0.27 |            0.00 |
| Xalan-2.6                      |      0.64 |      0.25 |          0.55 |      0.00 |          0.59 |          0.22 |              0.48 |          0.00 |        0.61 |        0.23 |            0.47 |        0.00 |            0.59 |            0.21 |                0.48 |            0.00 |            0.59 |            0.20 |                0.45 |            0.00 |
| Xerces-1.3                     |      0.77 |      0.25 |          0.37 |      0.17 |          0.74 |          0.25 |              0.34 |          0.20 |        0.75 |        0.23 |            0.33 |        0.20 |            0.75 |            0.24 |                0.33 |            0.40 |            0.73 |            0.26 |                0.34 |            0.20 |
| Apache                         |      0.64 |      0.20 |          0.84 |      1.27 |          0.56 |          0.18 |              0.81 |          1.40 |        0.56 |        0.14 |            0.75 |        1.20 |            0.55 |            0.15 |                0.78 |            1.50 |            0.55 |            0.17 |                0.75 |            1.40 |
| Safe                           |      0.74 |      0.34 |          0.58 |      0.00 |          0.69 |          0.32 |              0.52 |          0.00 |        0.70 |        0.28 |            0.51 |        0.00 |            0.69 |            0.26 |                0.51 |            0.00 |            0.68 |            0.24 |                0.52 |            0.00 |
| Zxing                          |      0.62 |      0.21 |          0.43 |      0.00 |          0.59 |          0.18 |              0.41 |          0.00 |        0.59 |        0.18 |            0.39 |        0.00 |            0.59 |            0.16 |                0.40 |            0.00 |            0.58 |            0.18 |                0.39 |            0.00 |
| Equinox                        |      0.65 |      0.31 |          0.19 |      0.00 |          0.62 |          0.30 |              0.17 |          0.00 |        0.64 |        0.30 |            0.17 |        0.00 |            0.63 |            0.29 |                0.17 |            0.00 |            0.61 |            0.25 |                0.16 |            0.00 |
| Jdt                            |      0.76 |      0.35 |          0.23 |      0.00 |          0.72 |          0.33 |              0.22 |          0.00 |        0.74 |        0.33 |            0.22 |        0.00 |            0.73 |            0.33 |                0.22 |            0.00 |            0.70 |            0.29 |                0.21 |            0.00 |
| Lucene                         |      0.78 |      0.30 |          0.37 |      0.00 |          0.72 |          0.25 |              0.34 |          0.00 |        0.73 |        0.23 |            0.35 |        0.00 |            0.73 |            0.25 |                0.34 |            0.00 |            0.66 |            0.22 |                0.33 |            0.00 |
| Mylyn                          |      0.69 |      0.19 |          0.31 |      0.40 |          0.65 |          0.18 |              0.28 |          0.80 |        0.67 |        0.17 |            0.28 |        0.80 |            0.66 |            0.18 |                0.28 |            0.80 |            0.64 |            0.16 |                0.28 |            0.80 |
| Pde                            |      0.68 |      0.21 |          0.33 |      1.30 |          0.64 |          0.18 |              0.31 |          1.50 |        0.66 |        0.19 |            0.30 |        1.40 |            0.64 |            0.19 |                0.30 |            1.40 |            0.63 |            0.18 |                0.29 |            1.40 |
| Average                        |      0.74 |      0.28 |          0.53 |      0.61 |          0.70 |          0.25 |              0.49 |          0.68 |        0.71 |        0.25 |            0.48 |        0.67 |            0.70 |            0.24 |                0.49 |            0.69 |            0.68 |            0.23 |                0.47 |            0.70 |



### Component and Parameter Variation Results


| Experiment Family   | Variant           | Parameter    | Value   |   AUC |   MCC |   Popt@20 |   IFA |
|:--------------------|:------------------|:-------------|:--------|------:|------:|----------:|------:|
| component           | Anchor-Only       | -            | -       |  0.74 |  0.24 |      0.50 |  0.68 |
| component           | Equal-Detector    | -            | -       |  0.70 |  0.23 |      0.47 |  0.64 |
| component           | Equal-Mechanism   | -            | -       |  0.72 |  0.25 |      0.50 |  0.65 |
| component           | Fixed-Gamma       | -            | -       |  0.72 |  0.26 |      0.51 |  0.64 |
| component           | Full              | -            | -       |  0.74 |  0.28 |      0.53 |  0.61 |
| component           | No-Copula         | -            | -       |  0.71 |  0.24 |      0.50 |  0.66 |
| component           | No-Guard          | -            | -       |  0.72 |  0.23 |      0.48 |  0.66 |
| component           | Otsu-Only         | -            | -       |  0.74 |  0.25 |      0.51 |  0.63 |
| component           | Quantile-Anchor   | -            | -       |  0.73 |  0.24 |      0.49 |  0.67 |
| parameter           | L=1               | L            | 1.0     |  0.72 |  0.27 |      0.52 |  0.62 |
| parameter           | L=10              | L            | 10.0    |  0.73 |  0.26 |      0.51 |  0.62 |
| parameter           | L=3               | L            | 3.0     |  0.73 |  0.27 |      0.52 |  0.62 |
| parameter           | L=5               | L            | 5.0     |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | L=7               | L            | 7.0     |  0.73 |  0.26 |      0.51 |  0.62 |
| parameter           | anchor_level=0.01 | anchor_level | 0.01    |  0.74 |  0.27 |      0.53 |  0.62 |
| parameter           | anchor_level=0.03 | anchor_level | 0.03    |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | anchor_level=0.05 | anchor_level | 0.05    |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | anchor_level=0.1  | anchor_level | 0.1     |  0.73 |  0.26 |      0.52 |  0.62 |
| parameter           | beta=0.6          | beta         | 0.6     |  0.74 |  0.27 |      0.52 |  0.61 |
| parameter           | beta=0.7          | beta         | 0.7     |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | beta=0.8          | beta         | 0.8     |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | beta=0.9          | beta         | 0.9     |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | c=0.5             | c            | 0.5     |  0.74 |  0.27 |      0.53 |  0.62 |
| parameter           | c=1.0             | c            | 1.0     |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | c=2.0             | c            | 2.0     |  0.74 |  0.28 |      0.52 |  0.62 |
| parameter           | delta=0.25        | delta        | 0.25    |  0.74 |  0.27 |      0.51 |  0.62 |
| parameter           | delta=0.5         | delta        | 0.5     |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | delta=0.75        | delta        | 0.75    |  0.74 |  0.27 |      0.52 |  0.61 |
| parameter           | delta=1.0         | delta        | 1.0     |  0.73 |  0.27 |      0.52 |  0.62 |
| parameter           | eta=0.0           | eta          | 0.0     |  0.73 |  0.27 |      0.52 |  0.61 |
| parameter           | eta=0.25          | eta          | 0.25    |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | eta=0.5           | eta          | 0.5     |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | eta=0.75          | eta          | 0.75    |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | eta=1.0           | eta          | 1.0     |  0.73 |  0.26 |      0.52 |  0.62 |
| parameter           | k_multiplier=0.5  | k_multiplier | 0.5     |  0.73 |  0.28 |      0.53 |  0.61 |
| parameter           | k_multiplier=1.0  | k_multiplier | 1.0     |  0.74 |  0.28 |      0.53 |  0.61 |
| parameter           | k_multiplier=1.5  | k_multiplier | 1.5     |  0.74 |  0.26 |      0.53 |  0.60 |
| parameter           | k_multiplier=2.0  | k_multiplier | 2.0     |  0.72 |  0.28 |      0.51 |  0.61 |



### Mechanism-Level Profile of Top-Risk Modules


| Mechanism                |   Share (%) |   Mean Contribution |   Defect Density (%) |   Defect Lift |
|:-------------------------|------------:|--------------------:|---------------------:|--------------:|
| Structural Burden        |       35.00 |                0.38 |                29.50 |          1.21 |
| Evolutionary Instability |       26.30 |                0.25 |                26.70 |          1.26 |
| Coordination Complexity  |       12.60 |                0.18 |                36.60 |          1.72 |
| Dependency Exposure      |       26.10 |                0.49 |                44.60 |          1.99 |



### Mechanism Agreement Profile Among Top-Risk Modules


| Agreement Level   |   Top-Risk Share (%) |   Defect Density (%) |   Defect Lift |
|:------------------|---------------------:|---------------------:|--------------:|
| 0                 |                 2.92 |                19.59 |          0.80 |
| 1                 |                24.66 |                24.19 |          0.99 |
| 2                 |                42.11 |                31.63 |          1.30 |
| 3+                |                30.31 |                40.70 |          1.67 |
