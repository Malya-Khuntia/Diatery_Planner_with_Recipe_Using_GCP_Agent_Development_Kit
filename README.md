# Diatery_Planner - Personalized Recipe and Dietary Planning Agent 🍴🥗

## Overview 🌟
**Diatery_Planner** is an AI-powered agent system designed to assist users in finding recipes and creating personalized dietary plans. It leverages the [Spoonacular API](https://spoonacular.com/food-api) to fetch recipe data and incorporates user preferences, health conditions, and dietary restrictions to provide tailored recommendations. The system can either provide a single recipe or develop a full dietary plan, considering factors like calorie intake, protein content, allergies, and medical conditions such as diabetes. 🥄🍽️

## Scenario Description 📋
The agent system supports the following use cases:
- **Single Recipe Request** 🍗: If the user requests only a recipe (e.g., "Give me a recipe for chicken curry"), the agent fetches and returns a suitable recipe using the Spoonacular API.
- **Full Dietary Plan** 📅: If the user requests a dietary plan (e.g., "I need a weekly diet plan for weight loss, I'm allergic to nuts, and I have diabetes"), the agent:
  - Gathers user requirements (dietary goals, cuisine preferences, allergies, health conditions). 📝
  - Finds recipes that match these requirements or generates a meal plan. 🔍
  - Analyzes the recipes for nutritional content (calories, protein, sugar levels). 📊
  - Ensures the plan avoids allergens and adheres to health constraints (e.g., low sugar for diabetics). 🚫
  - Finalizes the plan by ensuring it meets user goals and preferences. ✅

## System Architecture 🏗️
The system follows a hierarchical agent structure, as depicted in the provided diagram, with a root agent coordinating multiple sub-agents to handle specific tasks. The Spoonacular API is used as the primary data source for recipes and nutritional information. 🌐

### Directory Structure 📁
The file hierarchy, as shown in the provided image, is organized as follows:
- **APP/**: Root directory of the application. 🏠
  - **Diatery_Planner/**: Root directory of the agents. 🤖
    - **Sub_agents/**: Contains sub-agent implementations. 🧩
      - **Final/**: Handles final validation and output of the dietary plan or recipe. ✔️
        - `agent.py`: Defines the `final_agent`.
        - `prompt.py`: Instructions for the `final_agent`.
        - `__init__.py`: Package initialization.
      - **Health/**: Analyzes recipes for nutritional content and health constraints. 🩺
        - `agent.py`: Defines the `health_agent`.
        - `prompt.py`: Instructions for the `health_agent`.
        - `__init__.py`: Package initialization.
      - **Recipe_Finder/**: Finds recipes or generates meal plans using the Spoonacular API. 🔎
        - `agent.py`: Defines the `recipe_finder_agent`.
        - `prompt.py`: Instructions for the `recipe_finder_agent`.
        - `__init__.py`: Package initialization.
      - **User_Requirement/**: Gathers user preferences and constraints. 📋
        - `agent.py`: Defines the `user_requirement_agent`.
        - `prompt.py`: Instructions for the `user_requirement_agent`.
        - `__init__.py`: Package initialization.
    - **Tools/**: Contains utility tools for API integration and other functionalities. 🛠️
      - `spoonacular.py`: Defines the Spoonacular API wrapper.
   - `__init__.py`: Package initialization.
   - `agent.py`: Defines the root agent.
   - `prompt.py`: Instructions for the root agent.
   - `.env`: Environment configuration file. 🔑

### Agent Flow 🔄
The agent flow, as illustrated in the provided diagram (Chef.drawio.png), is as follows:
1. **Root Agent** 🌳:
   - Entry point for user queries.
   - Receives the initial user requirement and passes it to the User_Requirement SubAgent.
   - Coordinates the overall process, delegating tasks to sub-agents based on the request type.

2. **User_Requirement SubAgent** 📝:
   - Collects and processes user preferences and constraints, including:
     - Dietary goals (e.g., weight loss, muscle gain). 🎯
     - Cuisine preferences (e.g., Italian, Indian). 🍝
     - Diet type (e.g., vegetarian, keto). 🥗
     - Available ingredients. 🥕
     - Allergies (e.g., nuts, dairy). 🚫
     - Protein goals (e.g., 100g/day). 💪
     - Other conditions (e.g., diabetes). 🩺
   - Determines whether the user is requesting a single recipe or a full dietary plan.
   - Passes the processed requirements to the Recipe_Finder SubAgent.

3. **Recipe_Finder SubAgent** 🔍:
   - Uses the Spoonacular API to find recipes or generate meal plans that match the user’s requirements.
   - For a single recipe request, it searches for a recipe (e.g., using the API’s recipe search endpoint) and returns the result. 🍴
   - For a dietary plan, it generates a meal plan (e.g., using the API’s Generate Meal Plan endpoint) or compiles a list of recipes based on the requirements. 📅
   - Passes the output to the Health SubAgent.

4. **Health SubAgent** 🩺:
   - Analyzes the nutritional content of the selected recipes or meal plan (e.g., calories, protein, sugar levels). 📊
   - Ensures compliance with user constraints:
     - Avoids allergens specified by the user (e.g., excludes nuts). 🚫
     - Adjusts for health conditions (e.g., limits sugar for diabetic users by selecting low-carb options). 🥗
   - Passes the analyzed data to the Final SubAgent.

5. **Final SubAgent** ✅:
   - Validates the final output (single recipe or dietary plan).
   - Ensures the output matches the user’s requirements and preferences.
   - Allows for refinement if the output does not fully meet the user’s needs. 🔄
   - Returns the finalized result to the Root Agent for delivery to the user.

### Spoonacular API Integration 🌐
The system uses the Spoonacular API for:
- **Recipe Search** 🔎: Fetching recipes based on user preferences (e.g., cuisine, diet type) using endpoints like `/recipes/complexSearch`.
- **Meal Plan Generation** 📅: Creating dietary plans with parameters like time frame (day/week), target calories, diet, and excluded ingredients using the `/mealplanner/generate` endpoint.
- **Nutritional Information** 📊: Retrieving data on calories, protein, sugar, and other nutrients for each recipe using endpoints like `/recipes/{id}/nutritionWidget.json`.
- **Ingredient Analysis** 🥕: Checking for allergens in recipes by analyzing ingredient lists.

**API Key** 🔑: The API key is stored in the environment configuration (`.env` file) and accessed by the tools module.

## Key Features ✨
- **Recipe Search** 🔍: Provides recipes based on user preferences using the Spoonacular API.
- **Dietary Planning** 📅: Creates a full dietary plan with nutritional analysis, supporting daily or weekly plans.
- **Allergy Management** 🚫: Excludes recipes containing user-specified allergens (e.g., nuts, dairy).
- **Health Condition Support** 🩺: Adjusts recipes for conditions like diabetes by prioritizing low-sugar or low-carb options.
- **Nutritional Tracking** 📊: Calculates total calorie and protein intake for dietary plans, ensuring alignment with user goals.

## Implementation Details 🛠️
The system is built using the Google ADK, with a modular design inspired by the provided travel concierge system. Each sub-agent has its own `agent.py` and `prompt.py` files, defining its logic and instructions. The `Tools` directory houses the Spoonacular API wrapper, similar to the `places.py` in the travel concierge system.

### Agent Configuration 🤖
The following table summarizes the agents and their roles:

| **Agent Name**          | **Role**                                         | **Tools Used**               | **Model**             |
|-------------------------|--------------------------------------------------|------------------------------|-----------------------|
| Root Agent 🌳           | Coordinates the process, delegates tasks         | None (uses sub-agents)       | gemini-2.0-flash-001  |
| User_Requirement Agent 📝 | Gathers user preferences and constraints       | None                         | gemini-2.0-flash-exp      |
| Recipe_Finder Agent 🔍  | Finds recipes or generates meal plans            | `spoonacular_api_tool`       | gemini-2.0-flash-exp      |
| Health Agent 🩺         | Analyzes nutritional content, health constraints | `spoonacular_api_tool`       | gemini-2.0-flash-exp      |
| Final Agent ✅          | Validates and finalizes the output               | None                         | gemini-2.0-flash-exp      |

### Tool Configuration 🛠️
The following table describes the primary tool:

| **Tool Name**         | **Purpose**                                       | **Implementation**           |
|-----------------------|---------------------------------------------------|------------------------------|
| Spoonacular API Tool 🌐 | Fetches recipes, meal plans, and nutritional data | Wrapper in `spoonacular.py`  |

### Prompt Design ✍️
Each sub-agent has specific instructions defined in its `prompt.py` file:
- **User_Requirement Agent** 📝: Instructed to extract dietary goals, allergies, and health conditions from the user’s query and determine the request type (recipe or plan).
- **Recipe_Finder Agent** 🔍: Instructed to use the Spoonacular API to search for recipes or generate meal plans based on provided parameters.
- **Health Agent** 🩺: Instructed to analyze nutritional data, exclude allergens, and adjust for health conditions.
- **Final Agent** ✅: Instructed to validate the output and ensure it meets user requirements, with provisions for refinement.

## Development Plan 📅
The development will proceed in the following order to ensure a structured and modular implementation:
1. **Tools Module** 🛠️:
   - Create `spoonacular.py` to wrap the Spoonacular API, with functions for recipe search, meal plan generation, and nutritional analysis.
   - Implement environment variable handling for the API key (stored in `.env`). 🔑
2. **User_Requirement SubAgent** 📝:
   - Develop `agent.py` and `prompt.py` to process user queries and extract requirements.
   - Ensure the agent can distinguish between recipe and dietary plan requests.
3. **Recipe_Finder SubAgent** 🔍:
   - Develop `agent.py` and `prompt.py` to interface with the Spoonacular API tool.
   - Implement logic for single recipe searches and meal plan generation.
4. **Health SubAgent** 🩺:
   - Develop `agent.py` and `prompt.py` to analyze nutritional data and enforce health constraints.
   - Include logic for allergen exclusion and health condition adjustments.
5. **Final SubAgent** ✅:
   - Develop `agent.py` and `prompt.py` to validate and finalize the output.
   - Implement refinement logic if the output does not meet requirements.
6. **Root Agent** 🌳:
   - Develop the main `agent.py` and `prompt.py` to coordinate sub-agents.
   - Integrate all sub-agents and ensure seamless flow from user query to final output.

## Dependencies 📦
- **Google ADK** 🤖: For agent development and orchestration.
- **Spoonacular API** 🌐: For recipe and nutritional data ([Spoonacular API](https://spoonacular.com/food-api)).
- **requests** 📡: Python library for making API calls, used in the tools module.
- **Python 3.8+** 🐍: For compatibility with ADK and API libraries.

## Installation Steps 🚀
Follow these steps to set up the Diatery_Planner project on your local machine:

1. **Create a Virtual Environment** 🏕️  
   First, create a virtual environment to isolate the project dependencies. Run the following command in your terminal:  
   ```bash
   python3 -m venv diatery_env
   ```

2. **Activate the Virtual Environment** ✅  
   Activate the virtual environment to ensure the project uses its isolated dependencies:  
   - On macOS/Linux:  
     ```bash
     source diatery_env/bin/activate
     ```
   - On Windows:  
     ```bash
     diatery_env\Scripts\activate
     ```

3. **Clone the Repository** 📥  
   Clone the Diatery_Planner repository from GitHub to your local machine:  
   ```bash
   git clone https://github.com/your-username/diatery_planner.git
   ```

4. **Navigate to the Project Directory** 📂  
   Move into the project directory:  
   ```bash
   cd diatery_planner
   ```

5. **Install Dependencies** 📦  
   Install the required Python packages listed in the `requirements.txt` file:  
   ```bash
   pip install -r requirements.txt
   ```
   *Note*: Ensure you have a `requirements.txt` file with dependencies like `requests` and any Google ADK libraries. If not, you can create one with:  
   ```bash
   echo "requests" > requirements.txt
   ```

6. **Set Up the Environment Variables** 🔑  
   Create a `.env` file in the project root directory and add your Spoonacular API key:  
   ```bash
   echo "SPOONACULAR_API_KEY=your_spoonacular_api_key" > .env
   ```
   Replace `your_spoonacular_api_key` with your actual Spoonacular API key. You can obtain one by signing up at [Spoonacular](https://spoonacular.com/food-api).

7. **Run the Application with ADK Web** 🌐  
   Start the Diatery_Planner application using the Google ADK web interface:  
   ```bash
   adk web
   ```
   This will launch the application, and you can access it via your browser (typically at `http://localhost:8080`).

## Considerations and Limitations ⚠️
- **API Limitations** 📉: The Spoonacular API has usage limits (e.g., daily request quotas), which may require careful management or a paid plan for extensive use.
- **Nutritional Precision** 📊: While the API provides macronutrient data (calories, protein, etc.), it may not offer detailed metrics like glycemic index, which could be relevant for conditions like diabetes. The system will rely on diet types (e.g., low-carb) for such cases.
- **User Input** 📝: The system assumes users provide complete requirements in their queries (e.g., calorie goals, allergies). Additional logic for handling incomplete inputs may be needed in future iterations.
- **Modularity** 🧩: The modular design allows for future additions, such as memory management (similar to `memory.py` in the travel concierge) to store user preferences across sessions.

## Comparison with Travel Concierge 🔄
The Diatery_Planner system is inspired by the travel concierge system provided in the attachments:
- **Similarities** 🤝:
  - Both use a hierarchical agent structure with a root agent coordinating sub-agents.
  - Both integrate external APIs (Google Maps Places for travel, Spoonacular for recipes).
  - Both employ modular designs with separate directories for sub-agents and tools.
- **Differences** ⚖️:
  - Diatery_Planner has a more complex flow due to the need to handle two distinct request types (recipe vs. plan) and perform nutritional analysis.
  - The travel concierge relies on sub-agents for inspiration and news, while Diatery_Planner focuses on user requirements, recipe finding, and health analysis.
  - Diatery_Planner uses a single API (Spoonacular) for most functionalities, whereas the travel concierge uses multiple tools (Google Maps, search).

## Next Steps 🚀
The development will proceed by building each component in the order outlined above. The first step is to create the `spoonacular.py` file in the `Tools` directory to wrap the Spoonacular API. Subsequent steps will involve implementing each sub-agent and the root agent. If additional features (e.g., session memory, user interaction for incomplete inputs) are desired, they can be incorporated later. 🌟

## License 📜
This project is licensed under the Apache License, Version 2.0.