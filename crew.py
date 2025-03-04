import os
from crewai import Agent, Task, Crew, Process
from tools.custom_tool import web_scraping_tool, text_summarization_tool, risk_analysis_tool

os.environ["GEMINI_API_KEY"] = "your-gemini-api-key"

# Create Agents
regulatory_scraper = Agent.from_config("config/agents.yaml", agent_name="regulatory_scraper", tools=[web_scraping_tool])
risk_analyst = Agent.from_config("config/agents.yaml", agent_name="risk_analyst", tools=[text_summarization_tool, risk_analysis_tool])
compliance_writer = Agent.from_config("config/agents.yaml", agent_name="compliance_writer")

# Create Tasks
scrape_rbi_task = Task.from_config("config/tasks.yaml", task_name="scrape_rbi_task", agent=regulatory_scraper)
analyze_compliance_task = Task.from_config("config/tasks.yaml", task_name="analyze_compliance_task", agent=risk_analyst)
generate_report_task = Task.from_config("config/tasks.yaml", task_name="generate_report_task", agent=compliance_writer)

# Form the Crew
crew = Crew(
    agents=[regulatory_scraper, risk_analyst, compliance_writer],
    tasks=[scrape_rbi_task, analyze_compliance_task, generate_report_task],
    process=Process.sequential
)

def run_crew():
    return crew.kickoff()
