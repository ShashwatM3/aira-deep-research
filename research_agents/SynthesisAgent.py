from agents import Agent, Runner, trace

synthesis_agent = Agent(
    name="Synthesis Agent",
    instructions=(
    "You are a research report writer. You will receive an original query followed by multiple summaries "
    "of web search results. Your task is to create a comprehensive report that addresses the original query "
    "by combining the information from the search results into a coherent whole. "
    "The report should be well-structured, informative, and directly answer the original query. "
    "Focus on providing actionable insights and practical information. "
    "Aim for up to 5-6 pages with clear sections and a conclusion. "
    "Important: Use markdown formatting with headings and subheadings. Have a table of contents in the beginning of the report that links to each section."
    "Try and include in-text citations to the sources used to create the report with a source list at the end of the report. Include all websites provided"
    ),
    model="gpt-4o",
)

async def getSynthesis(combined_summary):
  with trace("Synthesis Agent -- Workflow Step 3"):
    result = await Runner.run(synthesis_agent, combined_summary)
    return result.final_output 