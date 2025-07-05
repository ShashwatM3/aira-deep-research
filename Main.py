from rich import *
from pydantic import BaseModel
from rich.panel import Panel
from agents import Agent, Runner, function_tool

class analysisOutput(BaseModel):
  thoughts: str
  initial_queries: list[str]

analysis_agent = Agent(
  name="Analysis Agent",
  instructions="""
You are a research planning agent. Given a user's high-level research query, your task is to:
1. Think through how to approach this research:  
   - What types of sources or perspectives will be relevant?  
   - What challenges might arise in finding reliable or comprehensive information?  
   - How will you address or overcome those challenges?

2. Generate 3 focused search queries that would help gather the most relevant and diverse information needed to answer the main question.

Below are the two fields you would have to map to the required output format

Thoughts:
<Your strategic thoughts go here, including research plan, key aspects, challenges, and mitigation>

Generated Search Queries: [<query 1>, <query 2>, <query 3>]
""",
  output_type=analysisOutput
)

async def main():
  print("Welcome to [green] Deep Research [white] by ChatGPT")

  mainQuery = input("What would you like to research: ")
  result = await Runner.run(analysis_agent, mainQuery)
  print(f"Analysis result: {result}")

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())