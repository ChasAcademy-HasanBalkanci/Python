import psutil

active_monitoring = {"cpu": False, "memory": False, "disk": False}

def start_monitoring():
    print("Monitoring started.")
    active_monitoring["cpu"] = True
    active_monitoring["memory"] = True
    active_monitoring["disk"] = True

def list_active_monitoring():
    if not any(active_monitoring.values()):
        print("No active monitoring.")
    else:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_info = psutil.disk_usage('/')
        
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_info.percent}% ({memory_info.used / (1024 ** 3):.2f} GB used)")
        print(f"Disk Usage: {disk_info.percent}% ({disk_info.used / (1024 ** 3):.2f} GB used)")
