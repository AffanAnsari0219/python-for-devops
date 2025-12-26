class LogAnalyzer:
    def __init__(self, log_file, output_file):
        self.log_file = log_file
        self.output_file = output_file
        self.info = 0
        self.warning = 0
        self.error = 0

    def read_logs(self):
        try:
            file = open(self.log_file, "r")
            lines = file.readlines()
            file.close()

            if not lines:
                print("Log file is empty")
                return []

            return lines

        except FileNotFoundError:
            print(f"{self.log_file} file not found")
            return []

    def analyze_logs(self, lines):
        for line in lines:
            if "INFO" in line:
                self.info += 1
            elif "WARNING" in line:
                self.warning += 1
            elif "ERROR" in line:
                self.error += 1

    def print_and_save_summary(self):
        print("Log Summary")
        print("INFO:", self.info)
        print("WARNING:", self.warning)
        print("ERROR:", self.error)

        file = open(self.output_file, "w")
        file.write("Log Summary\n")
        file.write(f"INFO: {self.info}\n")
        file.write(f"WARNING: {self.warning}\n")
        file.write(f"ERROR: {self.error}\n")
        file.close()


# Program execution starts here
analyzer = LogAnalyzer("app.log", "log_summary.txt")
log_lines = analyzer.read_logs()
analyzer.analyze_logs(log_lines)
analyzer.print_and_save_summary()