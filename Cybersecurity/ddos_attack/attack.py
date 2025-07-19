#!/usr/bin/env python3

import subprocess
import shutil
import os
import sys

def check_root():
    if os.geteuid() != 0:
        print("❌ Please run this script with sudo or as root.")
        sys.exit(1)

def check_tool(tool):
    return shutil.which(tool) is not None

def install_instructions(tool, package):
    print(f"❌ {tool} is not installed.")
    print(f"👉 Install it using: sudo apt install {package}")
    sys.exit(1)

def run_ab_test():
    target = input("🔗 Target URL (e.g., http://192.168.1.10/): ")
    requests = input("📦 Total number of requests (default 100): ") or "100"
    concurrency = input("⚡ Concurrency level (default 10): ") or "10"

    print(f"\n🚀 Running ab -n {requests} -c {concurrency} {target}")
    try:
        subprocess.run(["ab", "-n", requests, "-c", concurrency, target], check=True)
    except subprocess.CalledProcessError:
        print("❌ Error running Apache Benchmark.")

def run_hping_test():
    ip = input("🌐 Target IP address: ")
    port = input("🔌 Target port (default 80): ") or "80"
    count = input("📤 Number of packets (default 100): ") or "100"
    flood = input("🌊 Use flood mode? (yes/no, default no): ") or "no"

    hping_cmd = ["hping3", "-S", "-p", port, "-c", count, ip]

    if flood.lower() in ["y", "yes"]:
        hping_cmd = ["hping3", "-S", "-p", port, "--flood", ip]

    print(f"\n🚀 Running: {' '.join(hping_cmd)}")
    try:
        subprocess.run(hping_cmd)
    except subprocess.CalledProcessError:
        print("❌ Error running hping3.")

def main():
    check_root()

    if not check_tool("ab"):
        install_instructions("ab", "apache2-utils")

    if not check_tool("hping3"):
        install_instructions("hping3", "hping3")

    print("\n🎯 Select test type:")
    print("1️⃣  HTTP Benchmark (ab)")
    print("2️⃣  TCP SYN Attack (hping3)")
    choice = input("Choose (1 or 2): ")

    if choice == "1":
        run_ab_test()
    elif choice == "2":
        run_hping_test()
    else:
        print("❌ Invalid selection.")

if __name__ == "__main__":
    main()
