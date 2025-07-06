<h2>Setting up AIRA — AI Research Assistant
<h3>Terminal-based Multi-Agent AI Tool for Generating Deep Research Reports</h3>

AIRA is a modular, multi-agent system built in Python that mimics how a human researcher works. It takes a user-defined topic and generates a comprehensive, structured research report by:
- Decomposing the query into focused subtopics
- Automatically performing intelligent web searches
- Scraping relevant content from top sources
- Summarizing and synthesizing key insights
- Delivering a polished, browser-rendered report
- Output Formats: Terminal AND as a webpage
<h2>Complete workflow</h2><img src="https://raw.githubusercontent.com/ShashwatM3/chatgpt-deep-research/main/assets/workflow.jpeg" alt="AIRA Workflow" width="600"/>
<h2>Setup</h2>
<h3>1. Set up Virtual Environment</h3>
Once you clone this repository, you must create and activate a Virtual Environment<br/>
<code>python -m venv .venv</code> — You only need to do this once<br/> (python3 for Mac users)
<code>source .venv/bin/activate</code> — Do this every time
<h3>2. Install the necessary libraries</h3>
<code>pip install -r requirements.txt</code>
<h3>3. Export the necessary API keys</h3>
To be done everytime you start up your virtual env<br/>
<code>export OPENAI_API_KEY=sk-......</code><br/>
<code>export SERPAPI_KEY=...........</code><br/>
<br/>Alternatively, you could create a .env file and load it in your script
<h3>4. Run the script</h3>
<code>python Main.py</code> (python3 for Mac users)
