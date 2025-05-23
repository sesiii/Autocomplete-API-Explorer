#!/bin/bash
echo "Probing endpoints..."
curl -v "http://35.200.185.69:8000/"  # Root
curl -v "http://35.200.185.69:8000/v1/"
curl -v "http://35.200.185.69:8000/v2/"
curl -v "http://35.200.185.69:8000/v3/"
curl -v "http://35.200.185.69:8000/v4/autocomplete?query=a"
curl -v "http://35.200.185.69:8000/docs"
curl -v "http://35.200.185.69:8000/openapi.json"
curl -v "http://35.200.185.69:8000/autocomplete?query=a"
curl -v "http://35.200.185.69:8000/v1/names?query=a"
curl -v "http://35.200.185.69:8000/v1/full"
curl -v "http://35.200.185.69:8000/v2/full"
curl -v "http://35.200.185.69:8000/v3/full"
curl -v "http://35.200.185.69:8000/v2/list"
curl -v "http://35.200.185.69:8000/v3/list"
curl -v "http://35.200.185.69:8000/v1/autocomplete?query=a&limit=20"
curl -v "http://35.200.185.69:8000/v2/autocomplete?query=a&limit=20"
curl -v "http://35.200.185.69:8000/v3/autocomplete?query=a&limit=30"
curl -v -X POST "http://35.200.185.69:8000/v1/autocomplete?query=a"