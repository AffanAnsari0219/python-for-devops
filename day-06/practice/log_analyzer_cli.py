import argparse


class LogAnalyzer:
    def __init__(self, log_file, output_file, level=None):
        self.log_file = log_file
        self.output_file = output_file
        self.level = level
        self.info = 0
        self.warning = 0
        self.error = 0

    def run(self):
        """Read logs, count messages, filter by level, print and save summary."""
        try:
            with open(self.log_file, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"{self.log_file} not found")
            return

        if not lines:
            print("Log file is empty")
            return

        # Count log levels
        for line in lines:
            if "INFO" in line:
                self.info += 1
            elif "WARNING" in line:
                self.warning += 1
            elif "ERROR" in line:
                self.error += 1

        # Apply level filter if provided
        if self.level:
            self.level = self.level.upper()
            if self.level == "INFO":
                self.warning = self.error = 0
            elif self.level == "WARNING":
                self.info = self.error = 0
            elif self.level == "ERROR":
                self.info = self.warning = 0

        # Print summary
        print("Log Summary")
        print(f"INFO: {self.info}")
        print(f"WARNING: {self.warning}")
        print(f"ERROR: {self.error}")

        # Save summary to file
        with open(self.output_file, "w") as f:
            f.write("Log Summary\n")
            f.write(f"INFO: {self.info}\n")
            f.write(f"WARNING: {self.warning}\n")
            f.write(f"ERROR: {self.error}\n")


def main():
    parser = argparse.ArgumentParser(description="Simple CLI Log Analyzer")
    parser.add_argument("--file", required=True, help="Path to log file")
    parser.add_argument("--out", default="log_summary.txt", help="Output file")
    parser.add_argument("--level", choices=["INFO", "WARNING", "ERROR"], help="Optional level filter")
    args = parser.parse_args()

    LogAnalyzer(args.file, args.out, args.level).run()


if __name__ == "__main__":
    main()
