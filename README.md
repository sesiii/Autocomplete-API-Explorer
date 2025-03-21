# Autocomplete API Explorer

## Overview
This project aims to explore and extract all names from an undocumented autocomplete API at `http://35.200.185.69:8000`. The goal is to discover its behavior, handle constraints, and document findings.

## Setup
- Python 3.x
- Dependencies: `requests` (`pip install requests`)

## Plan
1. Test the known endpoint: `/v1/autocomplete?query=<string>`.
2. Explore API behavior and constraints.
3. Build an extraction script.
4. Document discoveries.


## Progress
- Created `explore.py` to test `/v1/autocomplete` endpoint.
- Initial findings:
  - Accepts `query` param (e.g., `query=a`).
  - Returns JSON: `{"version": "v1", "count": X, "results": [...]}`.
  - Max 10 results per request.