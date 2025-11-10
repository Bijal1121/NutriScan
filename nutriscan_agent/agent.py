"""
NutriScan Agent

This is the root Sequential agent. It consist of internal sub-agents to perform specialized tasks.
"""

from google.adk.agents import SequentialAgent

from .sub_agents.vision_agent import vision_agent
from .sub_agents.nutrition_analysis_agent import nutrition_analysis_agent

# the root sequential agent
root_agent = SequentialAgent(
    name="NutriScanPipeline",
    sub_agents=[vision_agent, nutrition_analysis_agent],
    description=
    """
    This is the pipeline that scans for food items from the submitted image and gets it nutrient facts.
    """,
)