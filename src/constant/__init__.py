#constant to define constants in the pipeline
from pathlib import Path

 # Project root and main folders
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"
MODELS_DIR = PROJECT_ROOT / "models"
LOGS_DIR = PROJECT_ROOT / "logs"

# Raw input (original file in data/raw/)
RAW_DATA_FILE = "insurance.csv"
RAW_DATA_PATH = RAW_DIR / RAW_DATA_FILE

# Ingested artifact output (what ingestion writes)
INGESTED_TRAIN_FILE = "train.csv"
INGESTED_TRAIN_PATH = ARTIFACTS_DIR / INGESTED_TRAIN_FILE

# Model and log paths
BEST_MODEL_FILENAME = "best_insurance_model.pkl"
BEST_MODEL_PATH = MODELS_DIR / BEST_MODEL_FILENAME
DEFAULT_LOG_FILE = "app.log"
DEFAULT_LOG_PATH = LOGS_DIR / DEFAULT_LOG_FILE