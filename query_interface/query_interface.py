import os
import json
from datetime import datetime

class LogQueryInterface:
    def __init__(self, log_dir):
        self.log_dir = log_dir

    def search_logs(self, query):
        result = []
        for log_file in os.listdir(self.log_dir):
            with open(os.path.join(self.log_dir, log_file), "r") as f:
                for line in f:
                    log_data = json.loads(line)
                    if self._matches_query(log_data, query):
                        result.append(log_data)
        return result

    def _matches_query(self, log_data, query):
        for key, value in query.items():
            if key == "timestamp":
                if not self._check_timestamp(log_data["timestamp"], value):
                    return False
            elif key == "level":
                if log_data["level"] != value:
                    return False
            elif key == "log_string":
                if value not in log_data["log_string"]:
                    return False
            elif key == "metadata.source":
                if log_data["metadata"]["source"] != value:
                    return False
        return True

    def _check_timestamp(self, log_timestamp, query_timestamp):
        log_time = datetime.fromisoformat(log_timestamp[:-1]) 
        query_time = datetime.fromisoformat(query_timestamp[:-1])
        return log_time >= query_time


