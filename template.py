import os
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define project structure
list_of_files = [
    # Core directories
    "data/.gitkeep",
    "notebooks/.gitkeep",
    "experiments/.gitkeep",
    "results/.gitkeep",

    # Source code
    "src/__init__.py",
    "src/models.py",
    "src/utils/__init__.py",
    "src/utils/common.py",

    # Components (modular tasks)
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/preprocessing.py",
    "src/components/feature_extraction.py",
    "src/components/model_training.py",
    "src/components/model_evaluation.py",

    # Pipeline scripts
    "src/pipeline/__init__.py",
    "src/pipeline/stage_01_data_ingestion.py",
    "src/pipeline/stage_02_preprocessing.py",
    "src/pipeline/stage_03_training.py",
    "src/pipeline/stage_04_evaluation.py",

    # Configs
    "config/config.yaml",
    "params.yaml",

    # Environment + dependencies
    "requirements.txt",
    "environment.yml",

    # Documentation
    "README.md",

    # Example research notebook
    "notebooks/01_data_exploration.ipynb",
    "notebooks/02_model_baseline.ipynb",
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
