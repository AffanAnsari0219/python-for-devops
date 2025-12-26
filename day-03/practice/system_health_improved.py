import psutil  # type: ignore


def check_cpu_threshold():
    try:
        cpu_threshold = int(input("Enter the CPU Threshold in % : "))

        if cpu_threshold > 100 or cpu_threshold < 0:
            print("Enter the threshold between 0 and 100. Exiting.")
            return
        else:
            print("Checking...")

        current_cpu_utilization = psutil.cpu_percent(1)
        current_disk_usage = psutil.disk_usage('/')
        current_ram_usage = psutil.virtual_memory()

        print("\nSystem Health Status:")
        print(f"CPU Utilization : {current_cpu_utilization}%")
        print(f"Disk Usage     : {current_disk_usage.percent}%")
        print(f"RAM Usage      : {current_ram_usage.percent}%")

        if current_cpu_utilization >= cpu_threshold:
            print("Alert!!! Email sent...")
        else:
            print("\nCPU in Safe State :)\n")

    except ValueError:
        print("Invalid input! Please enter a numeric value for CPU threshold.")

    except Exception as error:
        print("Something went wrong:", error)


check_cpu_threshold()
