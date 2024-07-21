from datetime import datetime

def stop_work(start_time, generate_report, get_current_user, project_name, reports_path, create_project_folder):
    if start_time:
        # Record the end time and calculate elapsed time
        end_time = datetime.now()
        elapsed_time = (end_time - start_time).total_seconds() / 3600  # in hours
        cost = elapsed_time * 50  # $50 per hour
        
        # Debug statements
        print(f"Work stopped at: {end_time}")
        print(f"Start time: {start_time}")
        print(f"Elapsed time (hours): {elapsed_time:.2f}")
        print(f"Cost calculated: ${cost:.2f}")
        
        # Generate report
        print(f"Generating report for project: {project_name}")
        generate_report(elapsed_time, cost, project_name, reports_path, get_current_user, create_project_folder)
        print("Report generation function called.")
    else:
        print("Work not started. No start time provided.")
