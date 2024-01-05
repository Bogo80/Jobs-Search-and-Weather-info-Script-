# Jobs-Search-and-Weather-info-Script-
# Description
This Python script fetches job postings from the Arbeitnow API and retrieves weather information for each job's location using the Tomorrow.io API. For each job, it prints the job title, city, and key weather information such as temperature and wind speed.

Features
Fetches job postings from Arbeitnow API.
Retrieves weather information for each job's location.
Displays job title, city, temperature, and wind speed.

# Requirements
Python 3
requests library
```bash
pip install requests
```

# Usage
Replace "your_key" in the script with your actual API key from Tomorrow.io.

Run the script in your Python environment:
``` bash
 python script_name.py
```

# Configuration
The script is currently set to fetch the first 15 job postings. Modify the script if you need to change this limit.
Make sure to use a valid API key from Tomorrow.io for fetching weather data.

