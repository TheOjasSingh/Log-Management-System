
# Log Management System

The Log Management System is a Python-based application for managing and querying log data. It includes components for ingesting logs, querying logs based on various criteria, and providing a command-line interface (CLI) for user interaction.


## Features

- Log Ingestion: Easily ingest logs from multiple sources into designated log files.
- Query Interface: Search logs based on log level, log message, timestamp, and metadata source.
- CLI Interface: Interactive command-line interface for querying logs and performing log management tasks.
- Scalable and Efficient: Designed to handle high volumes of logs efficiently.
- Flexible Configuration: Easily configure logging levels and file paths for each log source.


## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/log-management-system.git
```
2. Navigate to the project directory:

```bash
cd log-management-system
```
3. Install dependencies:

```bash
pip install -r requirements.txt
```
## Usage/Examples

Log Ingestion
- To ingest logs into the system, use the log_ingestor/log_ingestor.py module. Example usage:
```bash
python log_ingestor/log_ingestor.py --log-dir logs
```
Query Interface
- To query logs, use the query_interface/query_interface.py module. Example usage:
```bash
python query_interface/query_interface.py --log-dir logs --level error
```
CLI Interface
- To interact with the CLI interface, run the main.py script without any additional arguments. Example usage:
```bash
python main.py --log-dir logs
```
