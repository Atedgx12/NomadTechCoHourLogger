import os
from datetime import datetime

def generate_report(hours, cost, project_name, reports_path, get_current_user, create_project_folder):
    user = get_current_user()
    report = f"User: {user}\nProject: {project_name}\nHours: {hours:.2f}\nCost: ${cost:.2f}"

    print("Generating report...")
    print(f"Report content:\n{report}")
    print(f"User: {user}")
    print(f"Project Name: {project_name}")
    print(f"Hours: {hours:.2f}")
    print(f"Cost: ${cost:.2f}")

    project_folder = create_project_folder(reports_path, project_name)
    print(f"Project folder created at: {project_folder}")
    
    report_filename = f'report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    report_path = os.path.join(project_folder, report_filename)
    print(f"Report will be saved to: {report_path}")

    with open(report_path, "w") as file:
        file.write(report)
    print("Report successfully written to file.")
