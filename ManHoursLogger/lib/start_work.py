from datetime import datetime

def start_work():
    # Record the current time as the start time
    start_time = datetime.now()
    
    # Debug statements to trace the function execution
    print("Starting work...")
    print(f"Start time recorded: {start_time}")
    
    return start_time
