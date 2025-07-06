<h2>Setting up AIRA — AI Research Assistant
<h3>Terminal-based Multi-Agent AI Tool for Generating Deep Research Reports</h3>

AIRA is a modular, multi-agent system built in Python that mimics how a human researcher works. It takes a user-defined topic and generates a comprehensive, structured research report by:
- Decomposing the query into focused subtopics
- Automatically performing intelligent web searches
- Scraping relevant content from top sources
- Summarizing and synthesizing key insights
- Delivering a polished, browser-rendered report

<h3>Setting up the Tool</h3>
Once you clone this repository, you must create and activate a Virtual Environment<br/>
<code>python -m venv .venv</code> (You only need to do this once)<br/>
<code>source .venv/bin/activate</code>
<br/><br/>
Install the necessary libraries<br/>
<code>pip install -r requirements.txt</code>
<br/><br/>
Export the necessary API keys<br/>
<code>export OPENAI_API_KEY=sk-......</code>
<code>export SERPAPI_KEY=...........</code>
