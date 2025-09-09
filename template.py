import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define project structure
list_of_files = [

    # GitHub workflow (optional future CI/CD)
    ".github/workflows/.gitkeep",

    # Source code (pipelines + components)
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/prepare_base_model.py",
    "src/components/prepare_callbacks.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",

    "src/pipeline/__init__.py",
    "src/pipeline/stage_01_data_ingestion.py",
    "src/pipeline/stage_02_prepare_base_model.py",
    "src/pipeline/stage_03_training.py",
    "src/pipeline/stage_04_evaluation.py",
    "src/pipeline/prediction.py",

    "src/config/__init__.py",
    "src/config/configuration.py",

    "src/utils/__init__.py",
    "src/utils/common.py",

    "src/logging/__init__.py",

    "src/entity/__init__.py",
    "src/constants/__init__.py",

    # Notebooks
    "notebooks/01_data_ingestion.ipynb",
    "notebooks/02_prepare_base_model.ipynb",
    "notebooks/03_prepare_callbacks.ipynb",
    "notebooks/04_training.ipynb",
    "notebooks/05_model_evaluation.ipynb",
    "notebooks/trials.ipynb",

    # Data, experiments, results, research
    "data/.gitkeep",
    "experiments/.gitkeep",
    "results/.gitkeep",
    "research/.gitkeep",

    # Configs
    "config/config.yaml",
    "config/params.yaml",

    # Deployment (optional, for industry reuse)
    "deploy/app.py",
    "deploy/Dockerfile",
    "deploy/setup.py",
    "deploy/setup.cfg",
    "deploy/tox.ini",
    "deploy/requirements.txt",

    # Tests
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",

    # Project-level files
    "environment.yml",
    "pyproject.toml",
    "main.py",
    "README.md"
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
        logging.info(f"{filename} already exists")

