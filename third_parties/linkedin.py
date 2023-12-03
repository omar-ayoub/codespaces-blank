import os
import requests



def scrape_linked_profile(linkedin_profile_url:str):
    """
    scrap information from linkedin profile,Manually scrap information from linkedin profile
    """
    api_endpoint = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    response = requests.get(api_endpoint,params={"url":linkedin_profile_url},headers=header_dic)

    return response