import argparse
from query_interface.query_interface import LogQueryInterface


def main():
    parser = argparse.ArgumentParser(description="Query Interface for Logs")
    parser.add_argument("--log-dir", required=True, help="Directory containing log files")
    parser.add_argument("--level", help="Filter logs by level (info, error, success)")
    parser.add_argument("--log-string", help="Search logs by log message string")
    parser.add_argument("--source", help="Filter logs by metadata source")
    parser.add_argument("--start-time", help="Filter logs from this start time (ISO 8601 format)")
    parser.add_argument("--end-time", help="Filter logs until this end time (ISO 8601 format)")
    args = parser.parse_args()

    query = {}
    if args.level:
        query["level"] = args.level
    if args.log_string:
        query["log_string"] = args.log_string
    if args.source:
        query["metadata.source"] = args.source
    if args.start_time:
        query["timestamp"] = args.start_time
    if args.end_time:
        query["timestamp"] = args.end_time

    query_interface = LogQueryInterface(args.log_dir)
    result = query_interface.search_logs(query)
    for log in result:
        print(log)

if __name__ == "__main__":
    main()
