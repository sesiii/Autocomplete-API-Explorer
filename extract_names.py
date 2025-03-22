import requests
import time
import string
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()

BASE_URLS = {
    "v1": "http://35.200.185.69:8000/v1/autocomplete",
    "v2": "http://35.200.185.69:8000/v2/autocomplete",
    "v3": "http://35.200.185.69:8000/v3/autocomplete"
}
CHARACTERS = string.ascii_lowercase

def fetch_names(query, base_url, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(base_url, params={"query": query}, timeout=10)
            if response.status_code == 200:
                return response.json().get("results", [])
            elif response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 1))
                logger.info(f"Rate limited at {base_url}. Waiting {retry_after}s...")
                time.sleep(retry_after)
                continue
            else:
                logger.error(f"Error {response.status_code} for '{query}' at {base_url}")
                return []
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error for '{query}' at {base_url}: {e}")
            if attempt < retries - 1:
                logger.info(f"Retrying '{query}' at {base_url} ({attempt+1}/{retries})...")
                time.sleep(2)
                continue
            return []
    return []

def extract_all_names(base_url, version):
    all_names = set()
    request_count = 0
    max_results = {"v1": 10, "v2": 12, "v3": 15}[version]
    
    for c in CHARACTERS:
        names = fetch_names(c, base_url)
        all_names.update(names)
        request_count += 1
        logger.info(f"{version} Prefix '{c}': {len(names)}/{max_results} names, Total: {len(all_names)}")
        time.sleep(1)
    
    for c1 in CHARACTERS:
        for c2 in CHARACTERS:
            query = c1 + c2
            names = fetch_names(query, base_url)
            prev_count = len(all_names)
            all_names.update(names)
            request_count += 1
            if len(names) < max_results and len(names) > 0:
                logger.info(f"{version} Prefix '{query}': {len(names)}/{max_results} names (fewer than max), Total: {len(all_names)}")
            elif len(all_names) > prev_count:
                logger.info(f"{version} Prefix '{query}': Added {len(all_names) - prev_count} new names, Total: {len(all_names)}")
            if len(names) == 0:
                logger.info(f"{version} Prefix '{query}': No names, stopping this branch")
                break
            time.sleep(1)
    
    return all_names, request_count

if __name__ == "__main__":
    for version, base_url in BASE_URLS.items():
        logger.info(f"\nStarting extraction for {version}")
        names, req_count = extract_all_names(base_url, version)
        logger.info(f"\n{version} Final Results:")
        logger.info(f"Total unique names: {len(names)}")
        logger.info(f"Total requests: {req_count}")
        with open(f"names_{version}.txt", "w") as f:
            f.write("\n".join(sorted(names)))
        logger.info(f"Saved to names_{version}.txt")