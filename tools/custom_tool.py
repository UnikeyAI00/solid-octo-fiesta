from crewai_tools import tool
import requests
from bs4 import BeautifulSoup

@tool
def web_scraping_tool():
    """Scrapes the RBI website for the latest Notifications, Master Circulars, and Master Directions."""
    url = "https://www.rbi.org.in/Scripts/NotificationUser.aspx"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    notifications = []
    for link in soup.find_all("a", href=True):
        if "Notification" in link.text or "Master Circular" in link.text or "Master Direction" in link.text:
            notifications.append({"title": link.text.strip(), "url": link["href"]})

    return str(notifications)
  
import google.generativeai as genai
import os
from crewai_tools import tool

# Set up Google Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@tool
def text_summarization_tool(text: str):
    """Uses Google Gemini API to summarize long regulatory texts into key compliance obligations."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Summarize the following regulatory text: {text}")
    return response.text

@tool
def risk_analysis_tool(text: str):
    """Uses Google Gemini API to analyze regulatory text and extract key risk mitigation steps."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Identify risk mitigation measures from this regulatory text: {text}")
    return response.text
