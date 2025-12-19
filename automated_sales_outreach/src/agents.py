from agents import Agent

instructions1 = "You are a sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write professional, serious cold emails."

instructions2 = "You are a humorous, engaging sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write witty, engaging cold emails that are likely to get a response."

instructions3 = "You are a busy sales agent working for ComplAI, \
a company that provides a SaaS tool for ensuring SOC2 compliance and preparing for audits, powered by AI. \
You write concise, to the point cold emails."

AGENT_DEFINITIONS = [
    ("Professional Sales Agent", instructions1),
    ("Engaging Sales Agent", instructions2),
    ("Busy Sales Agent", instructions3),
]

sales_picker_instructions = (
    "You are a strict output filter. You pick the best cold sales email from the given options.\n"
    "1. Read all provided email drafts.\n"
    "2. Select ONLY one best email.\n"
    "3. Output strictly the content of that chosen email and nothing else.\n"
    "4. Do NOT include phrases like 'Here is the best one' or 'Subject:'. Just the body text.\n"
    "5. Do NOT output multiple emails."
)

manager_instructions = """
You are a Sales Manager.
1. Use sales_agent1, sales_agent2, and sales_agent3 to generate 3 drafts.
2. Pick the best one.
3. Use send_email to send ONLY the best one.
"""

# Handoff Specialist Agents
subject_writer = Agent(
    name="Subject Writer",
    instructions="Write a catchy subject line."
)

html_converter = Agent(
    name="HTML Converter",
    instructions="Convert text to HTML."
)
