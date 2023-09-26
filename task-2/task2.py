#!/usr/bin/python3
import os
import platform
import psutil
import sys
import cpuinfo
import subprocess

# Get and print the byte order
byte_order = sys.byteorder
print("Byte Order:", byte_order, "endian")

# Virtualization
try:
    lscpu_output = subprocess.check_output(["lscpu"], universal_newlines=True)
    virtualization = (
        "Supported" if "Virtualization: VT-x" in lscpu_output else "Not Supported"
    )
except subprocess.CalledProcessError:
    virtualization = "Not Supported"

# Extract CPUs count
CPUs = os.cpu_count()

try:
    # CPU frequency
    cpu_info = psutil.cpu_freq()
    print(f"Current frequency: {cpu_info.current:.2f} Mhz")
    print(f"Minimum frequency: {cpu_info.min:.2f} Mhz")
    print(f"Maximum frequency: {cpu_info.max:.2f} Mhz")

except FileNotFoundError:
    print("CPU info not available on this system")

print("Name of the operating system:", os.name)
print("Name of the OS system:", platform.system())
print("Model Name: ", platform.node())
print("Platform Name: ", platform.platform())

# print results
print("Total CPUs count:", CPUs)
print(f"thread count per core: {psutil.cpu_count() // psutil.cpu_count(logical=False)}")


# Get CPU information
cpu_info = cpuinfo.get_cpu_info()

# Display cache sizes
print(f"L1i Cache Size: ", cpu_info.get("l1_instruction_cache_size", "No info"))
print(f"L1d Cache Size: ", cpu_info.get("l1_data_cache_size", "No info"))
print(f"L2 Cache Size: ", cpu_info.get("l2_cache_size", "No info"))
print(f"L3 Cache Size: ", cpu_info.get("l3_cache_size", "No info"))

# Distributor ID, Distributor Description, Distributor codename
with open("/etc/os-release", "r") as os_release_file:
    os_release_info = {}
    for line in os_release_file:
        key, value = line.strip().split("=")
        os_release_info[key] = value.strip('"')

print(f"Distributor ID:",os_release_info.get("ID", ""))
print(f"Distributor Description:",os_release_info.get("PRETTY_NAME", ""))
print(f"Distributor codename:",os_release_info.get("VERSION_CODENAME", ""))