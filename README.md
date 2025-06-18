# Thesis-Policy-Assessment-QT-EWMA

This repository contains all code, data, and documentation supporting the master’s thesis **“Assessing Mobility Policies A Priori: A Change Detection Methodology Using Traffic Simulation”**. The core contribution is a framework that integrates microscopic traffic simulation with a nonparametric sequential change-detection algorithm (QT-EWMA) to evaluate, in advance, the efficacy and detection delays of proposed urban mobility interventions.

---

## 📂 Repository Structure

```
Thesis-Policy-Assessment-QT-EWMA/
│
├── README.md
│
├── data/
│   ├── raw/                 # Original simulator outputs and input definitions
│   └── preprocessed/        # Cleaned, normalized, and reshaped datasets ready for analysis
│
├── docs/                    # Detailed project documentation, figures, and results
│
├── src/                     # Source code and experiment notebooks
│   ├── __pycache__/         # Python cache (ignore)
│   ├── eann/                # Manuscript and scripts for EANN conference paper
│   ├── old/                 # Legacy or deprecated code
│   ├── quanttree/           # # Placeholder: see below for implementation
│   ├── febagni_scripts.py   # Utility functions (data loaders, common routines)
│   ├── THESIS-data_sequential_preprocessing.ipynb  
│   ├── THESIS-QT-EWMA-Policy-1.ipynb  
│   ├── THESIS-QT-EWMA-Policy-2.ipynb  
│   └── THESIS-QT-EWMA-Policy-3.ipynb  
```

### External QuantTree Implementation

Instead of including the QuantTree source here, this repository points to the official implementation:
> **QuantTree**  
> https://github.com/diegocarrera89/quantTree

Clone or install that repo to provide the `quanttree` module required by the notebooks.

---

## 🚀 Quick Start

This project runs smoothly on **Google Colab**, leveraging free GPU/CPU resources. To reproduce each experiment:

1. **Open the notebook**

   * Go to [Google Colab](https://colab.research.google.com).
   * Select **File → Open notebook → GitHub**.
   * Paste this repository URL:

     ```
     https://github.com/yourusername/Thesis-Policy-Assessment-QT-EWMA
     ```
   * Choose the notebook you wish to run (e.g. `THESIS-QT-EWMA-Policy-1.ipynb`).

2. **Mount Google Drive (optional)**
   If you wish to persist outputs or use larger datasets:

   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

3. **Accessing the data**
   On each notebook, the path to the data should be adapted depending on where the files were put.

4. **Execute the notebook**
   Run cells sequentially. Preprocessing will load raw data from `data/raw/`, transform it into `data/preprocessed/`, and then perform QT-EWMA experiments for the selected policy.

---

## 🛠 Dependencies

All experiments rely on:

* Python ≥ 3.7
* NumPy
* Pandas
* Matplotlib
* SciPy
* Jupyter
* scikit-learn
* `quanttree` (included in `src/quanttree/`)

---

## 📝 Notebooks

* **Data preprocessing**:
  `THESIS-data_sequential_preprocessing.ipynb`
  Cleans, normalizes, and reshapes simulator output into a time-series format suitable for QT-EWMA.

* **Policy experiments**:
  `THESIS-QT-EWMA-Policy-[1|2|3].ipynb`
  Runs the full pipeline—load data, build QuantTree histogram, apply QT-EWMA, compute detection delays—for each policy scenario.

---

## 📖 Documentation

* **`docs/`**
  Contains detailed method descriptions, theoretical background, and complete experimental results.
* **EANN paper**
  Located under `src/eann/`, with LaTeX source and final PDF.
