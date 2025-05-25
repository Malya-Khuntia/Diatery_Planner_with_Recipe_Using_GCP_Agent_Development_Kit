from google.adk.agents import Agent

from Diatery_Planner.Sub_agents.User_Requirement.prompt import USER_REQUIREMENT_INSTR

user_requirement_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="user_requirement_agent",
    description="Agent to gather user dietary preferences and constraints",
    instruction=USER_REQUIREMENT_INSTR
)