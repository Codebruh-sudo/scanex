# scanner/config_loader.py
import yaml

def load_config(path="config/scanner_config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)
