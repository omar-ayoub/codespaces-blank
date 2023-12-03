from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

import requests
from agents.linkedin_lookuup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
import os
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    
    linkedin_profile_url = linkedin_lookup_agent(name="Eden Marco")
    
    


    summery_template = """
        give the linkedin information {information} about a person from i want you to create :
        1. a short summary
        2. Two interesting facts about him
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summery_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)


    print(chain.run(information=linkedin_data))



