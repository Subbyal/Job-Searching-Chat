from serpapi import GoogleSearch

def serpapi_search(query):
    search_params = {
        "q": query + " jobs",
        "api_key": "2571163e947b2a303758f118289932369c6a27eeb1700b900832492ce6b23b43"
    }
    search = GoogleSearch(search_params)
    result = search.get_dict()
    return result.get("organic_results", [])

# Example usage
job_title = "software engineer job"
serpapi_results = serpapi_search(job_title)
print(serpapi_results)
