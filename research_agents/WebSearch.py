from serpapi import GoogleSearch
import os

def search_serpapi(query: str, max_results=4):
    params = {
        "q": query,
        "api_key": os.getenv("SERPAPI_KEY"),
        "num": max_results
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    links = []
    for result in results.get("organic_results", [])[:max_results]:
        link = result.get("link")
        if link:
            links.append(link)
    
    return links