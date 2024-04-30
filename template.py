import os
from pathlib import Path 
list_of_files =[
    ".github/workflows",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb",
    "src/logger/__init__.py",
    "src/exception/__init__.py",
    "src/logger/logging.py",
    "src/exception/exception.py"
]

for i in list_of_files:
    i = Path(i)
    file_dir,filename = os.path.split(i)
    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        
    
    if(not os.path.exists(i)) or (os.path.getsize(i)==0):
        with open(i,"w") as f:
            pass

