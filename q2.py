import requests
from time import sleep 


def download_urls(urls):
    # Initialize a dictionary to store the results
    results = {}
    
    for url in urls:
        retries = 3
        for attempt in range(retries):
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
                results[url] = response.text
                print(f"Successfully downloaded content from {url}")
                break  # Exit the retry loop if the download is successful
            
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred for {url}: {http_err}")
            except requests.exceptions.ConnectionError as conn_err:
                print(f"Connection error occurred for {url}: {conn_err}")
            except requests.exceptions.Timeout as timeout_err:
                print(f"Timeout error occurred for {url}: {timeout_err}")
            except requests.exceptions.RequestException as req_err:
                print(f"An error occurred for {url}: {req_err}")
            
            if attempt < retries - 1:
                print(f"Retrying ({attempt + 1}/{retries})...")
                sleep(2)  # Wait for 2 seconds before retrying
    
    return results

# Example usage
urls = [
    "https://www.example.com",
    "https://www.nonexistentwebsite.xyz",
    "https://www.httpbin.org/status/404"
]

downloaded_content = download_urls(urls)

# Print the results
for url, content in downloaded_content.items():
    print(f"\nContent from {url}:\n{content[:200]}...")  # Print the first 200 characters of the content
