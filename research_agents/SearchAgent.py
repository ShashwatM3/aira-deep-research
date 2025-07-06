from agents import Agent, Runner, function_tool, trace
from bs4 import BeautifulSoup
from typing import List
import requests

@function_tool
def scrapeUrls(title: str, urls: List[str]) -> str:
    """
    Scrapes the content of the given URLs and returns the combined plain text.

    Args:
        title (str): The research topic or title.
        urls (List[str]): List of URLs.

    Returns:
        str: Combined text from all web pages.
    """
    combined_text = f"Title: {title}\n\n"

    for i, url in enumerate(urls):
        try:
            response = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(response.text, "html.parser")

            for tag in soup(["script", "style", "nav", "footer", "header", "form", "noscript"]):
                tag.decompose()

            text = soup.get_text(separator="\n")
            lines = [line.strip() for line in text.splitlines() if line.strip()]
            cleaned_text = "\n".join(lines[:50])  # limit to first 50 lines

            combined_text += f"--- Source {i+1} ---\n{cleaned_text}\n\n"

        except Exception as e:
            combined_text += f"--- Source {i+1} ---\nFailed to scrape {url}: {e}\n\n"

    return combined_text


search_agent = Agent(
  name="Search Agent",
  instructions= (
    "You are a research assistant. You are given a set of 3 URLs and a title, as a dictionary. You will analyze "
    "all the 3 URLs, and produce a concise summary of the information. The summary must be 4-5 paragraphs"
    "Capture the main points. Write succinctly, no need to have complete sentences or perfect "
    "grammar. This will be consumed by someone synthesizing a report, so it's vital you capture the "
    "essence and ignore any fluff. Do not include any additional commentary other than the summary "
    "itself."
  ),
  tools=[scrapeUrls]
)

async def scraper_summarizer(input_data):
  # sample input_data = {
  #     "title": "What are the long-term effects of social media use on teenage mental health?",
  #     "urls": [
  #         "https://www.cureus.com/articles/176889-the-impact-of-social-media-on-the-mental-health-of-adolescents-and-young-adults-a-systematic-review",
  #         "https://www.mayoclinic.org/healthy-lifestyle/tween-and-teen-health/in-depth/teens-and-social-media-use/art-20474437",
  #         "https://www.yalemedicine.org/news/social-media-teen-mental-health-a-parents-guide"
  #     ]
  # }
  
  # Format the input as a string that the agent can understand
  formatted_input = f"Title: {input_data['title']}\nURLs: {', '.join(input_data['urls'])}"
  with trace("Search Agent Workflow -- Workflow Step 2"):
    result = await Runner.run(search_agent, formatted_input)
    return result.final_output