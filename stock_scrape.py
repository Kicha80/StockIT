import requests

# Define the endpoint URL for the News API
url = "https://newsapi.org/v2/top-headlines"

# Specify the parameters for your request, including your API key, country, category, and keyword
params = {
    "apiKey": "30bd19ffe3fc40c7bd199544bb554eeb",
    "country": "in",  # Country code for India
    "category": "business",  # You can specify a category like "business" for business news
    "q": "stock",  # Keyword filter to include only headlines containing the word "stock"
}

# Make a GET request to the News API
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract and print the headlines
    articles = data["articles"]
    for article in articles:
        title = article["title"]
        print(title)
else:
    # Print an error message if the request failed
    print("Error:", response.status_code)