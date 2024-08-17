import random
import csv
from faker import Faker

# Initialize the Faker generator
fake = Faker()

# Options for different fields
genders = ["Male", "Female", "Other"]
universities = ["UCT", "SU", "UP", "UKZN", "UWC", "Wits", "NWU"]
net_worth_options = ["<15m", "R15m+", "R30m+", "R50m+", "R100m+", "R200m+"]
sources_of_wealth = ["Entrepreneurship", "Corporate leadership", "Inheritance", 
                     "Investments", "Entertainment and Sports", "Professional Services"]
technical_fields = ["IT", "Chemical Engineering", "Industrial Engineering", 
                    "Electrical Engineering", "Civil Engineering", "Mechanical Engineering", 
                    "Maths", "Statistics", "Biochemistry"]
non_technical_fields = ["Business", "Marketing", "Logistics", "Investments", "Insurance"]
fields_of_expertise = technical_fields + non_technical_fields
support_offerings = ["funding", "business mentorship", "technical support", 
                     "industry connections", "investor connections"]
impact_areas = ["Circular economy", "Early childhood development", "Infrastructure", 
                "Nutrition", "Healthcare", "Education", "Communications", 
                "Agriculture", "Finance", "Energy"]

# Uncommon first and last names lists
uncommon_first_names = [
    "Aldous", "Balthazar", "Cedric", "Daphne", "Eulalia", "Ferdinand",
    "Galadriel", "Hermione", "Icarus", "Jocasta", "Kael", "Lysandra",
    "Morgana", "Nereus", "Oberon", "Persephone", "Quillon", "Rhiannon",
    "Sable", "Thaddeus", "Ulric", "Vesper", "Wystan", "Xanthe", "Yara", "Zephyr"
]

uncommon_last_names = [
    "Ashford", "Blackwood", "Crimson", "Drexel", "Everhart", "Fitzroy",
    "Grimshaw", "Hawke", "Ivy", "Jernigan", "Kingsley", "Lancaster",
    "Moriarty", "Nightshade", "Orwell", "Peregrine", "Quill", "Ravenwood",
    "Sterling", "Thorne", "Underwood", "Vanderbilt", "Whitley", "Xanthos", "Yarrow", "Zayne"
]

# Function to generate random age above 30
def generate_age():
    return random.randint(31, 70)

# Ensure half of the investors offer funding support
num_investors = 50
num_funding_investors = num_investors // 2

samples = []
funding_investors = 0

for _ in range(num_investors):
    first_name = random.choice(uncommon_first_names)
    last_name = random.choice(uncommon_last_names)
    gender = random.choice(genders)
    age = generate_age()
    email = fake.email()
    linkedin = fake.url()
    university = random.choice(universities)
    net_worth = random.choice(net_worth_options)
    wealth_sources = ", ".join(random.sample(sources_of_wealth, k=random.randint(1, 2)))  # Each investor can have 1 to 2 sources of wealth
    
    # Select fields of expertise
    expertise_fields = random.sample(fields_of_expertise, k=random.randint(1, 3))  # Select 1 to 3 fields of expertise
    
    # Determine if the investor is technical based on their fields of expertise
    technical = "Yes" if any(field in technical_fields for field in expertise_fields) else "No"

    # Ensure technical support is only offered if the investor is technical
    support_types = random.sample(support_offerings, k=random.randint(1, 3))
    if "technical support" in support_types and technical == "No":
        support_types.remove("technical support")
    
    # Ensure if funding is offered, at least 2 other supports are also offered
    if funding_investors < num_funding_investors:
        if "funding" not in support_types:
            support_types.append("funding")
        if "funding" in support_types and len(support_types) < 3:
            additional_supports = random.sample(
                [support for support in support_offerings if support not in support_types],
                k=2 - (len(support_types) - 1)
            )
            support_types.extend(additional_supports)
        funding_investors += 1
    else:
        support_types = [support for support in support_types if support != "funding"]

    support_types = ", ".join(support_types)
    expertise_fields = ", ".join(expertise_fields)
    impact_interests = ", ".join(random.sample(impact_areas, k=random.randint(1, 3)))  # Select 1 to 3 impact areas of interest

    sample = {
        "Name": first_name,
        "Surname": last_name,
        "Gender": gender,
        "Age": age,
        "Email": email,
        "Linkedin": linkedin,
        "University attended": university,
        "Are you technical?": technical,
        "Net worth": net_worth,
        "Source of wealth": wealth_sources,
        "Fields of expertise": expertise_fields,
        "Type of support offering": support_types,
        "Impact areas of interest": impact_interests
    }
    samples.append(sample)

# Specify the CSV file name
csv_file = "angel_investor_profiles.csv"

# Write the samples to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=samples[0].keys())
    writer.writeheader()
    writer.writerows(samples)

print(f"CSV file '{csv_file}' has been generated.")