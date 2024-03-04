#!/usr/local/bin/python3

# 1. Create a script that accepts the file name and puts its extension to output. If there is no extension - an exception should be raised. 
import os, sys, argparse, subprocess
try:
    fajl = sys.argv[1]
    if fajl.find('.') == None or fajl.find('.') < 0:
        # print("test")
        raise(ValueError)
    print(fajl.split('.')[-1])
except (ValueError):
    print(ValueError)

# 2. Given a list of integers. Remove duplicates from the list and create a tuple. Find the minimum and maximum number.
    
list_w_duplicates = [3,1,4,3,2,2,2,3,1,1,4,5,6,7]
tuples = tuple(set(list_w_duplicates))
print(tuples)
print("Min:", tuples[0], "Max:", tuples[-1])

# 3. Create a script that reads the access log from a file. 
# The name of the file is provided as an argument.
# An output of the script should provide the total number of different 
# User Agents and then provide statistics with the number 
# of requests from each of them.

#########
# 3.
# dict = {}
# with open(sys.argv[1], 'r') as f:
    
#     lines = f.readlines()
#     for line in lines:
#         logfile = line.split(" ")
#         if logfile[2].find("GET")  or logfile[2].find("POST"):
#             if logfile[0] in dict:
#                 dict[logfile[0]] += 1
#             else:
#                 dict[logfile[0]] = 1

# for i in dict:
#     print(i, dict[i])

# 4. Given an input string, count occurrences of all characters 
# within a string
# (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2).
    
dict = {}
for char in sys.argv[1]:
    if char in dict:
        dict[char] +=1
    else:
        dict[char] = 1

for elem in dict:
    print(elem, dict[elem])

# 5. Write a script that gets system information like distro info,
# memory(total, used, free), CPU info (model, core numbers, speed), 
# current user, system load average, and IP address. Use arguments for
# specifying resources. (For example, -d for distro -m for memory, -c for CPU,
#  -u for user info, -l for load average, -i for IP address).


    
parser = argparse.ArgumentParser(description='Basic system information')

parser.add_argument('--distro', '-d', action= 'store_true', help='distro info')
parser.add_argument('--memory', '-m', action= 'store_true', help='memory: total, used, free')
parser.add_argument('--user', '-u', action= 'store_true', help='user information')
parser.add_argument('--cpu', '-c', action= 'store_true', help='memory: total, used, free') 
parser.add_argument('--load', '-l', action= 'store_true', help='system load average')
parser.add_argument('--ipaddr', '-i', action= 'store_true', help='IP address')

args = parser.parse_args() #returns a namespace or an actual action if it exists

if args.distro == True:
    print("Distro information:")
    di = subprocess.run(["system_profiler", "SPSoftwareDataType"], check=True, capture_output=True)
    modelInfo = subprocess.run(['egrep', '-i', "version"],
                              input=di.stdout, capture_output=True)
    print(modelInfo.stdout.decode('utf-8').strip())

   
if args.memory == True:
    mem = subprocess.run(["df", "-hl"], check=True, capture_output=True)
    memInfo = subprocess.run(['grep', '-i', "/dev/disk1s5s1"], input=mem.stdout, capture_output=True)
    str = memInfo.stdout.decode('utf-8').strip()
    print("Filesystem               Size        Used        Available")
    lines = str.split(" ")
    result = ""
    for i in range(10):
        result += lines[i]
        result += "   "
    print(result)
if args.user == True:
    print("Current user:")
    subprocess.run(["whoami"])
if args.cpu == True:
    print("CPU information:")
    cpu = subprocess.run(["system_profiler", "SPHardwareDataType"], check=True, capture_output=True)
    cpuInfo = subprocess.run(['egrep', '-i', " 'processor|core|cache' "],
                              input=cpu.stdout, capture_output=True)
    print(cpuInfo.stdout.decode('utf-8').strip())

if args.load == True:
    print("System load average: ")
    subprocess.run(["sysctl", "-n" , "vm.loadavg"])
if args.ipaddr == True:
    print("Public IP address: ") 
    ipaddr = subprocess.run(["curl", "ifconfig.me"], capture_output=True)
    print(ipaddr.stdout.decode('utf-8').strip())