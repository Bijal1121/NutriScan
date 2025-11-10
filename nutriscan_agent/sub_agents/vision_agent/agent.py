"""
Vision Agent

This is agent receives an image from the user. It then scans for food items in the
given image.
"""

from google.adk.agents import LlmAgent

vision_agent = LlmAgent(
    name="vision_agent",
    model="gemini-2.5-flash",
    instruction="""You are a Food Vision Agent.
    
    Your task is to scan for food items in the given image.
    
    The output should only be a list of food items in the image.
    
    Example output: banana, waffles
    """,
    description="Detects the food items in the given image",
    output_key="food_items",
)