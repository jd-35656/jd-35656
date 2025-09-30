import json
from pathlib import Path

# Define constants for file paths and markers
README_FILE = Path("README.md")
SOCIAL_LINKS_FILE = Path("assets/socialLinks.json")

START_MARKER = "<!-- SOCIAL MEDIAS LINKS START -->"
END_MARKER = "<!-- SOCIAL MEDIAS LINKS END -->"

# Read JSON file with social media links using pathlib
data = json.loads(SOCIAL_LINKS_FILE.read_text())


# Function to generate the HTML for social media links
def generate_markdown(links):
    markdown = '<div align="center">\n'
    for link in links:
        markdown += f'  <a href="{link["url"]}" target="_blank" rel="noopener noreferrer" aria-label="{link["platform"]}">\n'
        markdown += f'    <img src="{link["image"]}" alt="{link["alt"]}" width="70px" height="70px" />\n'
        markdown += "  </a>\n"
    markdown += "</div>\n"
    return markdown


# Generate the social media links in Markdown
social_media_markdown = generate_markdown(data["socialLinks"])

# Ensure the README file exists before proceeding
if README_FILE.exists():
    # Read the Markdown file to replace the social media section using pathlib
    content = README_FILE.read_text()

    # Check if the markers exist in the content
    if START_MARKER in content and END_MARKER in content:
        # Find the section to replace
        before = content.split(START_MARKER)[0]
        after = content.split(END_MARKER)[1]

        # Rebuild the content with the new social media links
        new_content = (
            f"{before}{START_MARKER}\n{social_media_markdown}{END_MARKER}{after}"
        )

        # Write the updated content back to the README.md file using pathlib
        README_FILE.write_text(new_content)
        print("Social media links updated successfully!")
    else:
        print(f"Markers not found in {README_FILE}.")
else:
    print(f"{README_FILE} does not exist.")
