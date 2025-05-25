from google.adk.agents import Agent

from Diatery_Planner.Sub_agents.Final.prompt import FINAL_INSTR

final_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="final_agent",
    description="Agent to validate and finalize the recipe or dietary plan output",
    instruction=FINAL_INSTR
)