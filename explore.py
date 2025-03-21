import requests
import time

BASE_URL = "http://35.200.185.69:8000/v1/autocomplete"

def test_query(query):
    try:
        response = requests.get(BASE_URL, params={"query": query}, timeout=10)
        if response.status_code == 429:
            retry_after = int(response.headers.get("Retry-After", 1))
            print(f"Rate limited. Waiting {retry_after}s...")
            time.sleep(retry_after)
            return test_query(query)
        print(f"Query: {query}")
        print(f"Status: {response.status_code}")
        print(f"Headers: {response.headers}")
        print(f"Response: {response.text}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error for {query}: {e}")

if __name__ == "__main__":
    for q in ["a", "ab", "abc", "b"]:
        test_query(q)