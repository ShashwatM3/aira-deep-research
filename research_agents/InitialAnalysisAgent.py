from rich import *
from pydantic import BaseModel
from rich.panel import Panel
from agents import Agent, Runner, function_tool, trace

class analysisOutput(BaseModel):
  thoughts: str
  initial_queries: list[str]

analysis_agent = Agent(
  name="Analysis Agent",
  instructions="""
You are a research planning agent. Your goal is to generate a concise, strategic research direction that will guide the entire deep research process.

Given a user's high-level research query, your task is to:
1. Restate the goal clearly.
2. Identify what angles or aspects the research will focus on.
3. Specify trusted source types to prioritize.
4. Anticipate any major challenges in finding or verifying information.
5. Explain how those challenges will be addressed.
6. Finally, generate 3 focused search queries that the system will use to retrieve information.

Return the output in the following format:

Thoughts:
A 4–5 sentence paragraph summarizing all key aspects above in plain language. This paragraph defines the overall research direction and will be used to guide subsequent agent behaviors.

Generated Search Queries: [<query 1>, <query 2>, <query 3>]
These search queries must focus on providing the best information to contribute to the research direction, and when answered, should form end-to-end deep research content.
""",
  output_type=analysisOutput
)

async def get_initial_analysis(userQuery):
  with trace("Initial Analysis Agent -- Workflow Step 1"):
    result = await Runner.run(analysis_agent, userQuery)
    analysis = result.final_output
    return analysis