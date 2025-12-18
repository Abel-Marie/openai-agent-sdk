import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, trace

#Load environment variables from .env file
load_dotenv(override=True)

# Create the agent
agent = Agent(
    name = "Jokster",
    instructions = "You are a joke teller",,
    model = "litellm/gemini/gemini-2.5-flash-lite"
)

async def main():
    """Run the agent to tell a joke."""
    with trace("Telling a joke"):
        result = await Runner.run(agent, "Tell me a joke about computers.")
        print("Final Output:\n", result.final_output)

# Execute the main function
if __name__ == "__main__":
    asyncio.run(main())