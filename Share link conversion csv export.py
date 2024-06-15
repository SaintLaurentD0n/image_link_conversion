#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

def convert_drive_link(share_link):
    # Extract the file ID from the share link
    file_id = share_link.split('/')[5]
    # Create the direct access link
    direct_link = f'https://drive.google.com/uc?id={file_id}'
    return direct_link

# Example list of image names and their share links
image_data = [
    ("image1", "https://drive.google.com/file/d/1PPdZw3XQA4MHNu9ySDuZdGdfTf5HQtiS/view?usp=sharing"),
    # Add more images and links as needed
]

# Convert the links and create a list of dictionaries for CSV export
converted_data = []
for image_name, share_link in image_data:
    direct_link = convert_drive_link(share_link)
    converted_data.append({
        "Image Name": image_name,
        "Original Share Link": share_link,
        "Converted Direct Link": direct_link
    })

# Specify the CSV file name
csv_file = 'converted_drive_links.csv'

# Write the data to a CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Image Name", "Original Share Link", "Converted Direct Link"])
    writer.writeheader()
    for row in converted_data:
        writer.writerow(row)

print(f"Converted links have been saved to {csv_file}")


# In[ ]:




