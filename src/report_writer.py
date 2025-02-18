from crewai import Agent
from langchain_openai import ChatOpenAI

class ReportWriter:
    @staticmethod
    def create(llm: ChatOpenAI) -> Agent:
        return Agent(
            role='Report Writer',
            goal='Create comprehensive blockchain research reports',
            backstory="""You are an experienced technical writer specializing in blockchain technology. 
            You excel at creating clear, well-structured reports that effectively communicate complex 
            technical concepts and market analyses.""",
            tools=[],
            allow_delegation=False,
            llm=llm,
            verbose=True
        )