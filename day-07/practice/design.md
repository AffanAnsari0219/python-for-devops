Day07 - This design is for system_health_improved.py file for Day-03
=====================================================================

To Do:
Write down:
    What is the problem?
    What input does it need?
    What output should it give?
    What steps are involved?

What is the problem?
    We do not know what is the current health of the system.

What input does it need?
    From user it needs the basic % he thinks the system is curretly using. Its should be above 0 and below 100. Only in Numbers. If provided with anything else, error message should be printed.

What output should it give?
    It should provide the current CPU / RAM / DISK usage if user has provided correct input. If not then it will exit the code.

What steps are involved?
    The Steps are as follows:

STEP 1: The first thing we do is import psutil library.
#code#
import psutil
The above command won't work until you install/download the library.
#code#
pip install psutil

STEP 2: Creating a function as below under which all the body will be written.
#code#
def check_cpu_threshold()

STEP 3: Use of error handling concept of try: / exclude
#code#
try:

STEP 4: Take the input from user and check if the Number is above 0 and below 100
        If not then return with a error message. Else go ahead with the code.
#code#
cpu_threshold = int(input("Enter the CPU Threshold in % : "))

        if cpu_threshold > 100 or cpu_threshold < 0:
            print("Enter the threshold between 0 and 100. Exiting.")
            return
        else:
            print("Checking...")

STEP 5 - Taking current CPU / RAM / DISK usage
#code#
        current_cpu_utilization = psutil.cpu_percent(1)
        current_disk_usage = psutil.disk_usage('/')
        current_ram_usage = psutil.virtual_memory()

STEP 6 - Printing the same
#code#
        print("\nSystem Health Status:")
        print(f"CPU Utilization : {current_cpu_utilization}%")
        print(f"Disk Usage     : {current_disk_usage.percent}%")
        print(f"RAM Usage      : {current_ram_usage.percent}%")

STEP 7 - To check if the threshold provided by user is less or more, and print any 
        alert/safe message
#code#
        if current_cpu_utilization >= cpu_threshold:
            print("Alert!!! Email sent...")
        else:
            print("\nCPU in Safe State :)\n"

STEP 8: To print except
#code#
        except ValueError:
            print("Invalid input! Please enter a numeric value for CPU threshold.")

        except Exception as error:
            print("Something went wrong:", error)

STEP 9: Calling the function
#code#
check_cpu_threshold()