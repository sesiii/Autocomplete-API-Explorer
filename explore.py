import requests

BASE_URL = "http://35.200.185.69:8000/v1/autocomplete"

def test_query(query):
    response = requests.get(BASE_URL, params={"query": query})
    print(f"Query: {query}")
    print(f"Status: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Response: {response.text}\n")

if __name__ == "__main__":
    test_query("a")
    test_query("ab")
    test_query("")  