import asyncio
import sys
import os

# Ensure we can import from src
sys.path.append(os.getcwd())

from src.utils import run_agent_with_fallback
from src.agents import AGENT_DEFINITIONS

async def main():
    print("Testing agent execution...")
    try:
        # Test just the first agent
        name, instructions = AGENT_DEFINITIONS[0]
        print(f"Testing agent: {name}")
        # Use a very simple prompt
        result = await run_agent_with_fallback(name, instructions, "Say hello")
        print(f"Result: {result}")
    except Exception as e:
        print(f"Execution failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
