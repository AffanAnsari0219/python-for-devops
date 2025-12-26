import psutil # type: ignore

def check_cpu_threshold():
    cpu_threshold = int(input("Enter the CPU Threshold in % : "))
    if cpu_threshold > 100:
        print("Enter the threshold under 100%. Exiting.")
    else:
        print("Checking...")

    current_cpu_utilization = psutil.cpu_percent(1)
    current_disk_usage = psutil.disk_usage('/')
    current_ram_usage = psutil.virtual_memory()

    print("Your current CPU Utilization is :",current_cpu_utilization)
    print("Your current Disk Usage is :",current_disk_usage)
    print("Your current RAM Usage is :",current_ram_usage)

    if current_cpu_utilization >= cpu_threshold:
        print("Alert!!! Email sent...")
    else:
        print("CPU in Safe State :)")

check_cpu_threshold()

times = int(input("How many times do you want to run the program again? (enter a number)"))
for i in range(times):
    check_cpu_threshold()