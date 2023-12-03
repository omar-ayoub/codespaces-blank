from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.chat_models import ChatOpenAI


def lookup(name: str) -> str:
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    template = """given the full name {name_of_person} I want you to get me a link to their Linkedin profile page.
                          Your answer should contain only a URL"""
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func="?",
            description="useful for when you need get the Linkedin Page URL",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    propmt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    linkedin_profile_url = agent.run(propmt_template.format_prompt(name_of_person=name))

    return linkedin_profile_url
