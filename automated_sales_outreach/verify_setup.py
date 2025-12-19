import sys
import os

# Add current directory to path so we can import src
sys.path.append(os.getcwd())

print("Checking imports...")
try:
    from src.config import FREE_MODELS, SENDER_EMAIL
    print(f"✅ src.config loaded. SENDER: {SENDER_EMAIL}")
    
    from src.clients import get_brevo_api_instance
    print("✅ src.clients loaded.")
    
    from src.tools import send_email
    print("✅ src.tools loaded.")
    
    from src.agents import AGENT_DEFINITIONS
    print(f"✅ src.agents loaded. Agents: {[n for n, _ in AGENT_DEFINITIONS]}")
    
    from src.utils import run_with_fallback
    print("✅ src.utils loaded.")
    
    from src.agent_tools import ask_professional_sales_agent
    print("✅ src.agent_tools loaded.")
    
    print("\nALL IMPORTS SUCCESSFUL! The modular structure is valid.")

except Exception as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)
