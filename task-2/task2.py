#!/usr/bin/python3
import subprocess


output = subprocess.run(['lscpu'], stdout=subprocess.PIPE, text=True)
output_text = output.stdout
#print(output_text)

output_dist= subprocess.run('lsb_release -a', stdout=subprocess.PIPE, text=True, shell=True)
output_dist_info = output_dist.stdout

cpu_info = {}
dist_info = {}

for line in output_text.splitlines():
    key, value = line.strip().split(":")
    cpu_info[key] = value.strip()
    

print(f"Byte Order:",cpu_info.get("Byte Order", "")) # value exists so returns byte order otherwise returns empty string
print(f"CPU(s):",cpu_info.get("CPU(s)", ""))
print(f"Model Name:",cpu_info.get("Model name", ""))
print(f"CPU Max frequency:",cpu_info.get("CPU max MHz", ""))
print(f"CPU Min frequency:",cpu_info.get("CPU min MHz", ""))
print(f"Virtualization:",cpu_info.get("Virtualization", ""))
print(f"L1i cache size:",cpu_info.get("L1i cache", ""))
print(f"L1d cache size:",cpu_info.get("L1d cache", ""))
print(f"L2 cache size:",cpu_info.get("L2 cache", ""))
print(f"L3 cache size:",cpu_info.get("L3 cache", ""))
print(f"Thread(s) per core:",cpu_info.get("Thread(s) per core", ""))


for line in output_dist_info.splitlines():
    key, value = line.strip().split(":")
    dist_info[key] = value.strip()

print(f"Distributor ID:",dist_info.get("Distributor ID", ""))
print(f"Distributor Description:",dist_info.get("Description", ""))
print(f"Distributor codename:",dist_info.get("Codename", ""))
