#Import all required libraries
from rich import *
from pydantic import BaseModel
from rich.panel import Panel
from agents import Agent, Runner, function_tool
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'research-agents'))
from research_agents.InitialAnalysisAgent import get_initial_analysis 
from research_agents.WebSearch import search_serpapi
from research_agents.SearchAgent import scraper_summarizer
from rich.markdown import Markdown
from research_agents.SynthesisAgent import getSynthesis
from rich.console import Console

async def main():
  mainDirective = "" #This would contain the main direction of our research
  initial_queries = [] #This would contain the queries on the basis of which the research report would be generated

  print()
  print("Welcome to [green] Deep Research [white] by ChatGPT")

  mainQuery = input("What would you like to research: ") #Obtaining user's research topic
  print(Panel(f"[yellow] Starting Deep Research on: [white]{mainQuery}")) 
  #the "rich" library makes it easy for us to style and provide a better overall UI, despite being on the terminal.

  inital_analysis = await get_initial_analysis(mainQuery) #calling the Analysis Agent

  mainDirective = inital_analysis.thoughts #Directive
  initial_queries = inital_analysis.initial_queries #Queries

  print(Panel("[green] Finished Analysis"))
  print()
  print(f"[yellow] Direction of our research: [white]{mainDirective}")
  print()
  print(f"[yellow] Initial Research Queries:")
  for query in initial_queries:
    print(f"- {query}")
  print("[blue] Conducting follow-up research")
  print()
  print(Panel("[blue] Web Search"))

  to_scrape = {}
  links = ""
  
  for query in initial_queries:
    arr_links = search_serpapi(query) #We use the SERP API to access Google search results, via 
    to_scrape[f"{query}"] = arr_links #Setting up dictionary input to Synthesis Agent
    for link in arr_links:
      links+=f"- {link}\n" #Keeping tracks of 
    print(f"Found references for query: {query}")
  print()

  combined_summaries = ""

  for query in to_scrape:
    scrapedSummary = await scraper_summarizer({"title": query, "urls": to_scrape[query]}) 
    #For each research query, we scrape the top websites' content and summarize findings for our report, via our  Search Agent
    combined_summaries+=f"""

    Research Search Queries: {query}
    Summary of information from Top Websites pertaining to this query: {scrapedSummary}

    """ #We will provide this to our Synthesis Agent to be able to generate a report out of

  combined_summaries+=f"""

  All websites used: {links}
  """ #We include all our websites used
  final_synthesis = await getSynthesis(combined_summaries) #The Synthesis Agent will be able to concise all of our findings into a research report
  console = Console()
  markdown = Markdown(final_synthesis)
  console.print(markdown)

if __name__ == "__main__":
  import asyncio
  asyncio.run(main())
