# Diabetes Digital Twin

A proof-of-concept healthcare Digital Twin for **Type 2 Diabetes**, built for the Happiest Health Reimagining and Reforming Healthcare in India Summit 2026 (Bengaluru).

## Problem Statement

Build a PoC Digital Twin for one chronic or lifestyle condition prevalent in India. The twin must fuse simulated EHR data with wearable time-series data, predict an adverse event, and present the result in a conceptual doctor dashboard.

## Approach

1. **EHR data:** Synthea-style patient records (patients, conditions, observations, medications, encounters), loaded and cleaned in `src/load_ehr.py`.
2. **Wearable data:** simulated time series (glucose, heart rate, steps) generated in `src/simulate_wearables.py`.
3. **Fusion:** EHR and wearable data merged per patient in `src/fuse_data.py`.
4. **Prediction:** an XGBoost model predicts an adverse event for Type 2 Diabetes patients (`src/train_model.py`, `src/evaluate.py`).
5. **Dashboard:** a Streamlit doctor dashboard (`app/dashboard.py`).

## Architecture

See [`docs/architecture.pdf`](docs/architecture.pdf).

## Data

- The EHR data follows the [Synthea](https://github.com/synthetichealth/synthea) CSV format and is fully synthetic.
- The raw CSVs are **not included in this repository** because `observations.csv` exceeds GitHub's 100 MB file limit. To run the project, place the five files (`patients.csv`, `conditions.csv`, `observations.csv`, `medications.csv`, `encounters.csv`) in `data/raw/`.
- **Note:** the Synthea data used here is US-based (Massachusetts). It serves as a stand-in for the PoC, and the pipeline works with any EHR data in the same format.

## Setup

```bash
git clone https://github.com/Suresh2005-gs/diabetes-digital-twin.git
cd diabetes-digital-twin
pip install -r requirements.txt
```

Then add the CSV files to `data/raw/` as described above.

## Usage

Run commands will be added here once the pipeline scripts are complete.

## Results

To be added after model training and evaluation.

## Demo and Presentation

- Demo video: to be added (see `docs/demo_link.md`)
- Presentation: [`docs/presentation.pdf`](docs/presentation.pdf)

## License

See the [`LICENSE`](LICENSE) file.