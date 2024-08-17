import csv
import random

# Define lists for random data generation
first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sarah", "David", "Anna", "Robert", "Jessica"]
last_names = ["Doe", "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Martinez"]
domains = ["example.com", "test.com", "demo.com"]
linkedin_base = "https://www.linkedin.com/in/"

# Define consistent mappings
degree_role_industry_map = {
    "Business, Economics and Management Sciences": {
        "roles": ["Business Analyst", "Financial Analyst", "Marketing Manager", "Operations Manager", "Consultant"],
        "industries": ["Business", "Finance", "Marketing", "Consulting"]
    },
    "Computer and Information Sciences": {
        "roles": ["Software Engineer", "Data Scientist", "System Administrator", "Web Developer", "IT Consultant"],
        "industries": ["IT", "Finance", "Healthcare", "Education"]
    },
    "Law": {
        "roles": ["Lawyer", "Legal Advisor", "Compliance Officer", "Paralegal"],
        "industries": ["Legal", "Corporate", "Government"]
    },
    "Agriculture, Agricultural Operations & Related Sciences": {
        "roles": ["Agricultural Manager", "Food Scientist", "Agronomist", "Farm Manager"],
        "industries": ["Agriculture", "Food Production", "Environmental Science"]
    },
    "Architecture and the Built Environment": {
        "roles": ["Architect", "Urban Planner", "Construction Manager", "Structural Engineer"],
        "industries": ["Architecture", "Construction", "Real Estate", "Urban Planning"]
    },
    "Physical Sciences": {
        "roles": ["Physicist", "Lab Technician", "Research Scientist", "Materials Scientist"],
        "industries": ["Research", "Healthcare", "Energy", "Environmental Science"]
    },
    "Mathematics and Statistics": {
        "roles": ["Data Analyst", "Statistician", "Quantitative Analyst", "Actuary"],
        "industries": ["Finance", "Insurance", "IT", "Research"]
    },
    "Psychology": {
        "roles": ["Clinical Psychologist", "Counselor", "Human Resources Manager", "Research Psychologist"],
        "industries": ["Healthcare", "Education", "Human Resources", "Research"]
    },
    "Chemical Engineering": {
        "roles": ["Chemical Engineer", "Process Engineer", "Quality Control Engineer", "Project Manager"],
        "industries": ["Chemical Engineering", "Pharmaceuticals", "Food Production", "Environmental Science"]
    },
    "Civil Engineering": {
        "roles": ["Civil Engineer", "Construction Manager", "Structural Engineer", "Urban Planner"],
        "industries": ["Civil Engineering", "Construction", "Real Estate", "Urban Planning"]
    },
    "Electrical Engineering": {
        "roles": ["Electrical Engineer", "Project Engineer", "Network Engineer", "Software Engineer"],
        "industries": ["Electrical Engineering", "IT", "Energy", "Manufacturing"]
    },
    "Mechanical Engineering": {
        "roles": ["Mechanical Engineer", "Product Manager", "Process Engineer", "Manufacturing Engineer"],
        "industries": ["Mechanical Engineering", "Automotive", "Aerospace", "Manufacturing"]
    },
    "Industrial Engineering": {
        "roles": ["Industrial Engineer", "Operations Manager", "Supply Chain Manager", "Project Manager"],
        "industries": ["Industrial Engineering", "Manufacturing", "Logistics", "Consulting"]
    }
}

technical_roles = ["Software Engineer", "Data Scientist", "System Administrator", "Web Developer", "IT Consultant", "Physicist", "Lab Technician", "Research Scientist", "Materials Scientist", "Data Analyst", "Statistician", "Quantitative Analyst", "Actuary", "Chemical Engineer", "Process Engineer", "Quality Control Engineer", "Project Engineer", "Network Engineer", "Mechanical Engineer", "Product Manager", "Industrial Engineer", "Operations Manager", "Supply Chain Manager"]
non_technical_roles = ["Business Analyst", "Financial Analyst", "Marketing Manager", "Operations Manager", "Consultant", "Lawyer", "Legal Advisor", "Compliance Officer", "Paralegal", "Agricultural Manager", "Food Scientist", "Agronomist", "Farm Manager", "Architect", "Urban Planner", "Construction Manager", "Structural Engineer", "Clinical Psychologist", "Counselor", "Human Resources Manager", "Research Psychologist"]

genders = ["Male", "Female", "Other"]
knowledge_fields = ["IT", "Chemical Engineering", "Industrial Engineering", "Electrical Engineering", "Civil Engineering", "Mechanical Engineering", "Business", "Marketing", "Logistics", "Maths", "Statistics", "Investments", "Insurance", "Biochemistry"]
areas_of_responsibility = ["Product", "Sales and marketing", "Operations"]
topics_and_industries = ["Artificial Intelligence", "B2B / Enterprise", "Blockchain", "Marketplace", "Real Estate / Proptech", "Climate / Sustainability"]
impact_areas = ["Circular economy", "Early childhood development", "Infrastructure", "Nutrition", "Healthcare", "Education", "Communications", "Agriculture", "Finance", "Energy"]

# Function to generate random choices
def random_choices(lst, num_choices=1):
    return random.sample(lst, k=num_choices)

# Create the CSV file
file_path = 'dummy_signups_consistent.csv'
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "First Name", "Last Name", "Email", "LinkedIn", "University degree and field of study",
        "Employment industry", "Employment role in above mentioned industries", "Are you technical?", 
        "Gender", "Age", "Do you have a cofounder?", "When do you want to start working on a startup full-time?", 
        "Fields of knowledge", "Level of expertise in fields mentioned above on a 6 - 10 scale", 
        "Which areas of a startup are you willing to take responsibility for?", 
        "Which topics and industries are you interested in?", "Impact areas of interest?"
    ])
    
    for _ in range(100):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f"{first_name.lower()}.{last_name.lower()}@{random.choice(domains)}"
        linkedin = f"{linkedin_base}{first_name.lower()}{last_name.lower()}"
        
        degree = random.choice(list(degree_role_industry_map.keys()))
        industries = random_choices(degree_role_industry_map[degree]["industries"], num_choices=random.randint(1, 3))
        roles = []
        for industry in industries:
            available_roles = degree_role_industry_map[degree]["roles"]
            roles.extend(random_choices(available_roles, num_choices=1))
        roles = list(set(roles))  # Remove duplicate roles
        if len(roles) > 2:
            roles = random_choices(roles, num_choices=2)
        
        is_technical = "Yes" if any(role in technical_roles for role in roles) else "No"
        gender = random.choice(genders)
        age = random.randint(20, 35)
        has_cofounder = random.choice(["Yes", "No"])
        start_time = random.randint(1, 24)
        
        # Knowledge fields related to the industry
        relevant_fields = [field for field in knowledge_fields if any(industry.split()[0].lower() in field.lower() for industry in industries)]
        if not relevant_fields:
            num_choices = random.randint(1, 3)
            relevant_fields = random_choices(knowledge_fields, num_choices=num_choices)
        else:
            num_choices = random.randint(1, min(3, len(relevant_fields)))
            relevant_fields = random_choices(relevant_fields, num_choices=num_choices)
        
        expertise_level = random.randint(6, 10)
        responsibility_area = ", ".join(random_choices(areas_of_responsibility, num_choices=random.randint(1, 2)))
        interested_topics = ", ".join(random_choices(topics_and_industries, num_choices=random.randint(1, 3)))
        impact_area = ", ".join(random_choices(impact_areas, num_choices=random.randint(1, 3)))
        
        writer.writerow([
            first_name, last_name, email, linkedin, degree, ", ".join(industries), ", ".join(roles), is_technical, 
            gender, age, has_cofounder, start_time, ", ".join(relevant_fields), expertise_level, 
            responsibility_area, interested_topics, impact_area
        ])

print(f"CSV file generated at {file_path}")