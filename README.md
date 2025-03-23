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

## Findings
- **Rate Limits**: Hits `429 Too Many Requests` after ~50 requests/minute. `Retry-After` header suggests 1s wait.
- **Approach**: Added retry logic with 1s delay to handle rate limits.

## Progress
- Added `extract_names.py` to fetch names using two-letter prefixes.
- Strategy: Query `aa` to `zz`, stop branch if no results.
- Initial test: Works but slow (~676 requests).

## Findings
- No pagination params (`limit`, `offset`) work.


## Approach
1. Explored `/v1/autocomplete` with `explore.py`.
2. Probed endpoints with `probe_endpoints.sh`.
3. Handled rate limits with retries.
4. Built `extract_names.py` for v1, v2, v3 using prefix queries.

## Findings
- **Endpoints**:
  - `/`: Hints at versions and guessing endpoints.
  - `/v1/autocomplete`: 10 results, ~6,710 names.
  - `/v2/autocomplete`: 12 results, different dataset.
  - `/v3/autocomplete`: 15 results, symbols/spaces.
  - **Failed**: `/docs`, `/list`, `/v1/full`, `/v2/full`, `/v3/full`, `/v1/names`, `/v2/list`, `/v3/list`, `/v4/autocomplete`, etc. (404).
- **Constraints**:
  - Rate limit: `429`, ~50/min, `Retry-After: 1s`.
  - No pagination (`limit`, `offset` ignored).
  - `/v1/autocomplete`: GET only (`405` on POST).
- **Tested**: See `script.sh` for all attempts.

## Results
- **v1**: 6,720 names(702 requests).
- **v2**: 3991 names(639 requests).
- **v3**: 3732 names(664 requests).


## Files
- `explore.py`: Initial tests.
- `probe_endpoints.sh`: Endpoint probing.
- `extract_names.py`: Full extraction.
- `names_v1.txt`, `names_v2.txt`, `names_v3.txt`: Results.

## Setup
- `pip install requests`
- Run: `python extract_names.py`