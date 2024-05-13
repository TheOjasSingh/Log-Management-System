import logging
import os
import json
from datetime import datetime

class LogIngestor:
    def __init__(self, log_dir):
        self.log_dir = log_dir
        self._setup_logging()

    def _setup_logging(self):
        os.makedirs(self.log_dir, exist_ok=True)
        logging.basicConfig(level=logging.INFO)

    def log(self, api_name, level, log_string, metadata=None):
        log_data = {
            "level": level,
            "log_string": log_string,
            "timestamp": self._get_current_time(),
            "metadata": metadata or {}
        }
        log_file = os.path.join(self.log_dir, f"{api_name}.log")
        with open(log_file, "a") as f:
            f.write(json.dumps(log_data) + "\n")

    def _get_current_time(self):
        return datetime.utcnow().isoformat()

# Example Usage
ingestor = LogIngestor("logs")
