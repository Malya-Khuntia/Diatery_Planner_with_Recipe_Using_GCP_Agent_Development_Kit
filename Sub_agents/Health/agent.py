from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from Diatery_Planner.Tools import get_spoonacular_service
from Diatery_Planner.Sub_agents.Health.prompt import HEALTH_INSTR

# def get_nutritional_info_wrapper(recipe_id):
#     # Ensure recipe_id is an integer
#     try:
#         recipe_id = int(recipe_id)
#     except (ValueError, TypeError):
#         return {"error": f"Invalid recipe_id: {recipe_id}. Must be an integer."}
    
#     service = get_spoonacular_service()
#     return service.get_nutritional_info(recipe_id)

# nutritional_tool = FunctionTool(func=get_nutritional_info_wrapper)

health_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="health_agent",
    description="Agent to analyze nutritional content and ensure health constraints",
    instruction=HEALTH_INSTR,
    tools=[]
)