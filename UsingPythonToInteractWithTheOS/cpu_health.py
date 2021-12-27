import shutil
import psutil


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    #find percent of disk space currently free
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    #this function returns the average amount of the CPU being used over the given second interval (1 in this case)
    usage = psutil.cpu_percent(1)
    return usage < 75


if not check_disk_usage("/") and not check_cpu_usage():
    print("You don't have enough disk space, and your cpu usage is too high!")
elif not check_disk_usage("/"):
    print("You don't have enough disk space!")
elif not check_cpu_usage():
    print("Your cpu usage is too high!")
else:
    print("Computer is healthy!")