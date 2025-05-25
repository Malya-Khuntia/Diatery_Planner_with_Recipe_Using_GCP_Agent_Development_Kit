from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from Diatery_Planner.Tools import spoonacular_tool
from Diatery_Planner.Sub_agents.Recipe_Finder.prompt import RECIPE_FINDER_INSTR

recipe_finder_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="recipe_finder_agent",
    description="Agent to find recipes or generate meal plans using Spoonacular API",
    instruction=RECIPE_FINDER_INSTR,
    tools=[FunctionTool(func=spoonacular_tool)]
)