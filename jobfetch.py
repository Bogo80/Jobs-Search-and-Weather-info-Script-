import requests

def fetch_job_postings():
    url = "https://arbeitnow.com/api/job-board-api"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch job postings")

def fetch_weather_info(city):
    # Replace with your API key for Tomorrow.io
    api_key = "your_key"
    url = f"https://api.tomorrow.io/v4/timelines?location={city}&fields=temperature,windSpeed&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch weather for {city}")

def main():
    job_postings = fetch_job_postings()
    # Process only the first 3 job postings (due to 25 api calls limit on Tomowro.io )
    for job in job_postings['data'][:3]:
        city = job['location']
        job_title = job['title']
        try:
            weather_info = fetch_weather_info(city)
            # Adjust the following line based on the structure of weather data
            temperature = weather_info['data']['timelines'][0]['intervals'][0]['values']['temperature']
            wind_speed = weather_info['data']['timelines'][0]['intervals'][0]['values']['windSpeed']
            print(f"Job Title: {job_title}, City: {city}, Temperature: {temperature} °C, Wind Speed: {wind_speed} m/s")
        except Exception as e:
            print(f"Error fetching weather for {city}: {e}")

if __name__ == "__main__":
    main()
