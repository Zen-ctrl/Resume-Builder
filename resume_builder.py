import os

def get_input(prompt):
    return input(prompt).strip()

def format_duration(start, end):
    return f"{start} - {end}"

def format_job_description(description, metrics, impact):
    return f"{description}, {metrics}, {impact}"

def main():
    print("Resume Builder")
    print("Please provide the following information to create your resume:")

    name = get_input("Full Name: ")
    email = get_input("Email: ")
    phone = get_input("Phone: ")

    skills = get_input("Enter your skills (separated by commas): ").split(',')
    interests = get_input("Enter your interests (separated by commas): ").split(',')

    job_history = []

    while True:
        company = get_input("Enter the company name (or 'q' to quit): ")
        if company.lower() == 'q':
            break

        job_title = get_input(f"Enter the job title for {company}: ")
        start_date = get_input(f"Enter the start date (mm/yyyy) for {company}: ")
        end_date = get_input(f"Enter the end date (mm/yyyy) for {company} (Enter 'Present' if currently working): ")

        job_duration = format_duration(start_date, end_date)

        print("For the job description, follow the Google XYZ format:")
        description = get_input("What you've accomplished] X: ")
        metrics = get_input("The qualitative results] Y : ")
        impact = get_input("The skills or experience you utilized to achieve the outcome] Z: ")

        job_description = format_job_description(description, metrics, impact)

        job_history.append((company, job_title, job_duration, job_description))

    resume_filename = f"{name.replace(' ', '_')}_Resume.txt"

    with open(resume_filename, 'w') as f:
        f.write(f"{name}\n{email}\n{phone}\n\n")
        f.write("Skills:\n")
        for skill in skills:
            f.write(f"  - {skill.strip()}\n")
        
        f.write("\nInterests:\n")
        for interest in interests:
            f.write(f"  - {interest.strip()}\n")
        
        f.write("\nExperience:\n")
        for company, job_title, job_duration, job_description in job_history:
            f.write(f"{job_title}, {company}\n")
            f.write(f"{job_duration}\n")
            f.write(f"{job_description}\n\n")

    print(f"\nResume saved as {resume_filename}")

if __name__ == "__main__":
    main()
