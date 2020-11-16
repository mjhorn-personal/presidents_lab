import requests


def search_presidents():
    # url for api
    url = "https://api.duckduckgo.com"

    # get request for presidents
    resp = requests.get(url + "/?q=presidents of the United States&format=json")

    # convert response to json data
    rsp_data = resp.json()

    # add text fields to list of presidents
    presidents = []
    for result in rsp_data['RelatedTopics']:
        presidents.append(result['Text'])
    return presidents