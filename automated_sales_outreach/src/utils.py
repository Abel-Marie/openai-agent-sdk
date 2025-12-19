import asyncio
from agents import Agent, Runner
from .config import FREE_MODELS

async def run_with_fallback(agent_name, instructions, message, tools=None, handoffs=None):
    last_error = None

    for model in FREE_MODELS:
        print(f"🔁 {agent_name} → Trying model: {model}")

        agent = Agent(
            name=agent_name,
            instructions=instructions,
            tools=tools or [],
            handoffs=handoffs or [],
            model=model,
        )

        try:
            result = await Runner.run(agent, message)
            print(f"✅ {agent_name} succeeded with {model}\n")
            return result.final_output

        except Exception as e:
            last_error = e
            print(f"⚠️ {agent_name} failed on {model}")
            print(f"Reason: {e}\n")
            await asyncio.sleep(0.5)

    print(f"❌ {agent_name}: all free models failed.")
    raise last_error

async def run_agent_with_fallback(agent_name, instructions, message):
    # Wrapper for simple agent run (compatible with notebook structure)
    return await run_with_fallback(agent_name, instructions, message)
