#!/usr/bin/python3
import platform
import os
import subprocess

# Byte order
byte_order = platform.architecture()[0]

# Core
core = os.cpu_count()

# Model name, CPU max frequency, and CPU min frequency
with open("/proc/cpuinfo", "r") as cpu_info_file:
    cpu_info = cpu_info_file.read()
    model_name = [
        line.split(":")[-1].strip()
        for line in cpu_info.splitlines()
        if "model name" in line
    ][0]
    cpu_max_freq = [
        line.split(":")[-1].strip()
        for line in cpu_info.splitlines()
        if "cpu MHz" in line
    ][0]
    cpu_min_freq = [
        line.split(":")[-1].strip()
        for line in cpu_info.splitlines()
        if "cpu MHz" in line
    ][-1]

# Cache sizes (L1i, L1d, L2, L3)
with open("/sys/devices/system/cpu/cpu0/cache/index0/size", "r") as cache_file:
    l1i_cache_size = cache_file.read().strip()

with open("/sys/devices/system/cpu/cpu0/cache/index1/size", "r") as cache_file:
    l1d_cache_size = cache_file.read().strip()

with open("/sys/devices/system/cpu/cpu0/cache/index2/size", "r") as cache_file:
    l2_cache_size = cache_file.read().strip()

with open("/sys/devices/system/cpu/cpu0/cache/index3/size", "r") as cache_file:
    l3_cache_size = cache_file.read().strip()

# Thread(s) per core
threads_per_core = os.sched_getaffinity(0)

# Distributor ID, Distributor Description, Distributor codename
with open("/etc/os-release", "r") as os_release_file:
    os_release_info = {}
    for line in os_release_file:
        key, value = line.strip().split("=")
        os_release_info[key] = value.strip('"')

distributor_id = os_release_info.get("ID", "")
distributor_description = os_release_info.get("PRETTY_NAME", "")
distributor_codename = os_release_info.get("VERSION_CODENAME", "")

# Get virtualization support using lscpu command
try:
    lscpu_output = subprocess.check_output(["lscpu"], universal_newlines=True)
    virtualization = (
        "Supported" if "Virtualization: VT-x" in lscpu_output else "Not Supported"
    )
except subprocess.CalledProcessError:
    virtualization = "Not Supported"

# Display the parameters, including virtualization support
print(f"Byte order: {byte_order}")
print(f"Core: {core}")
print(f"Model name: {model_name}")
print(f"CPU max Frequency: {cpu_max_freq} MHz")
print(f"CPU min frequency: {cpu_min_freq} MHz")
print(f"Virtualization: {virtualization}")
print(f"L1i cache size: {l1i_cache_size}")
print(f"L1d cache size: {l1d_cache_size}")
print(f"L2 cache size: {l2_cache_size}")
print(f"L3 cache size: {l3_cache_size}")
print(f"Thread(s) per core: {len(threads_per_core)}")
print(f"Distributor ID: {distributor_id}")
print(f"Distributor Description: {distributor_description}")
print(f"Distributor codename: {distributor_codename}")
