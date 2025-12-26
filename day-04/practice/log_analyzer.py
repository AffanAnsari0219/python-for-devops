def analyze_logs():
    try:
        file = open("app.log", "r")
        lines = file.readlines()
        file.close()

        info = 0
        warning = 0
        error = 0

        if not lines:
            print("Log file is empty")
            return

        for line in lines:
            if "INFO" in line:
                info += 1
            elif "WARNING" in line:
                warning += 1
            elif "ERROR" in line:
                error += 1

        print("Log Summary")
        print("INFO:", info)
        print("WARNING:", warning)
        print("ERROR:", error)

        output = open("log_summary.txt", "w")
        output.write("Log Summary\n")
        output.write(f"INFO: {info}\n")
        output.write(f"WARNING: {warning}\n")
        output.write(f"ERROR: {error}\n")
        output.close()

    except FileNotFoundError:
        print("app.log file not found")
        return

analyze_logs()