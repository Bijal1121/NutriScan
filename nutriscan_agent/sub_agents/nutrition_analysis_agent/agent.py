"""
Nutrition Analysis Agent

This agent gets the list of food items present in the image.
This agent carries out the processing and tell the nutrient facts about the food items in the image
"""

from google.adk.agents import LlmAgent

nutrition_analysis_agent = LlmAgent(
    name="nutrition_analysis_agent",
    model="gemini-2.5-flash",
    instruction="""You are a Nutrition Analysis Agent.
    
    Your task is to output the nutrition values of each of the food items in the list.
    You have to mention the total content of:
    > carbohydrates
    > fats
    > sodium
    > protein
    """,
    description="Analyses the food items and mentions it nutrient facts",
    output_key="nutrient_facts",
)