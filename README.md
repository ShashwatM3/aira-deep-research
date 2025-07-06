<h2>Setting up AIRA — AI Research Assistant</h2>
<h3>Terminal-based Multi-Agent AI Tool for Generating Deep Research Reports</h3>

<p><strong>AIRA</strong> is a modular, multi-agent system built in Python that mimics how a human researcher works. It takes a user-defined topic and generates a comprehensive, structured research report by:</p>

<ul>
  <li>Decomposing the query into focused subtopics</li>
  <li>Automatically performing intelligent web searches</li>
  <li>Scraping relevant content from top sources</li>
  <li>Summarizing and synthesizing key insights</li>
  <li>Delivering a polished, browser-rendered report</li>
</ul>

<p><strong>Output Format:</strong> Terminal + HTML report saved to <code>report.html</code> in the same directory</p>

<h3>Complete Workflow</h3>
<img src="https://raw.githubusercontent.com/ShashwatM3/chatgpt-deep-research/main/assets/workflow.jpeg" alt="AIRA Workflow" width="600"/>

<h2>Setup (~ 4 minutes)</h2>

<h3>1. Clone and Navigate to the Project</h3>
<pre><code>git clone https://github.com/ShashwatM3/chatgpt-deep-research.git
cd chatgpt-deep-research</code></pre>

<h3>2. Set up Virtual Environment</h3>
<p>You only need to do this once:</p>
<pre><code>python -m venv .venv   # Windows</code></pre>
<pre><code>python3 -m venv .venv   # macOS/Linux</code></pre>
<p>Activate it every time:</p>
<pre><code>source .venv/bin/activate   # macOS/Linux</code></pre>
<pre><code>.venv\Scripts\activate      # Windows</code></pre>

<h3>3. Install the necessary libraries</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>4. Export the necessary API keys</h3>
<p>Run these every time you start the virtual environment:</p>
<pre><code># macOS/Linux
export OPENAI_API_KEY=sk-......
export SERPAPI_KEY=.........</code></pre>

<pre><code># Windows (Command Prompt)
set OPENAI_API_KEY=sk-......
set SERPAPI_KEY=.........</code></pre>

<p><strong>Alternative:</strong> Create a <code>.env</code> file with the keys and load it into your script <code>python-dotenv</code></p>
<pre><code>OPENAI_API_KEY=sk-......
SERPAPI_KEY=.........</code></pre>
<pre><code>from dotenv import load_dotenv
load_dotenv()</code></pre>
<strong>Note: The SERP API Key can be obtained by registering on <a href="https://serpapi.com/">https://serpapi.com/</a></strong>

<h3>5. Run the script</h3>
<pre><code>python Main.py   # Windows</code></pre>
<pre><code>python3 Main.py  # macOS/Linux</code></pre>

<h3>Troubleshooting Tips</h3>
<ul>
  <li>Ensure your virtual environment is activated before running scripts.</li>
  <li>If you see <code>ModuleNotFoundError</code>, rerun <code>pip install -r requirements.txt</code>.</li>
</ul>

<p>Happy Researching with <strong>AIRA</strong>!</p>
