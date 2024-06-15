#!/usr/bin/env python
# coding: utf-8

# In[3]:


def convert_drive_link(share_link):
    # Extract the file ID from the share link
    file_id = share_link.split('/')[5]
    # Create the direct access link
    direct_link = f'https://drive.google.com/uc?id={file_id}'
    return direct_link

# Example usage
share_links = [
    'https://drive.google.com/file/d/1PPdZw3XQA4MHNu9ySDuZdGdfTf5HQtiS/view?usp=sharing',
    # Add more links as needed
]

direct_links = [convert_drive_link(link) for link in share_links]

for link in direct_links:
    print(link)
    


# In[ ]:




