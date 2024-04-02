import pandas as pd
import os
import re

# Read the Excel file
excel_file = "C:\\Users\\aniket.gupta\\Downloads\\ghgh.xlsx"  # Replace with the path to your Excel file
df = pd.read_excel(excel_file)

# Function to extract paths from URLs
def extract_path(url):
    if pd.isnull(url):
        return None  # Return None for missing URLs
    # Extract path from URL
    match = re.match(r"https?://[^/]+(/[^#?]*)", url)
    if match:
        return match.group(1)  # Return path if URL is valid
    return None  # Return None for invalid URLs

# Extract paths from 'Status Page URL' and 'Summary URL' columns, you can rename the column as per your sheet
df['Status Page Path'] = df['Status Page URL'].apply(extract_path)
df['Summary Path'] = df['Summary URL'].apply(extract_path)

# Generate redirection rules
redirections = []
for _, row in df.iterrows():
    if row['Status Page Path']:
        redirections.append({
            "source": row['Status Page Path'],
            "destination": "/archive/superseded-standards",
            "permanent": True
        })
    if row['Summary Path']:
        redirections.append({
            "source": row['Summary Path'],
            "destination": "/archive/superseded-standards",
            "permanent": True
        })

# Count how many redirection rules are written
redirections_count = len(redirections)

# Write redirection rules to a JavaScript file
output_file = "redirections.js"
with open(output_file, 'w') as f:
    f.write("module.exports = [\n")
    for rule in redirections:
        f.write(f"\t{{\n\t\tsource: \"{rule['source']}\",\n\t\tdestination: \"{rule['destination']}\",\n\t\tpermanent: {rule['permanent']}\n\t}},\n")
        # Include the "permanent" tag in each redirection rule
    f.write("];\n")


print(f"Redirection rules written to {os.path.abspath(output_file)}")
print(f"Total redirection rules written: {redirections_count}")
