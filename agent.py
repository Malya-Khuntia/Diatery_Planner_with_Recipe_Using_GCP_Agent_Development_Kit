from google.adk.agents import Agent

from Diatery_Planner.Sub_agents.User_Requirement.agent import user_requirement_agent
from Diatery_Planner.Sub_agents.Recipe_Finder.agent import recipe_finder_agent
from Diatery_Planner.Sub_agents.Health.agent import health_agent
from Diatery_Planner.Sub_agents.Final.agent import final_agent
from Diatery_Planner.prompt import ROOT_AGENT_INSTR

root_agent = Agent(
    model="gemini-2.0-flash-exp",
    name="root_agent",
    description="A personalized recipe and dietary planning agent",
    instruction=ROOT_AGENT_INSTR,
    sub_agents=[
        user_requirement_agent,
        recipe_finder_agent,
        health_agent,
        final_agent
    ]
)