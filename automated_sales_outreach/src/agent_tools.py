from agents import function_tool
from .utils import run_with_fallback
from .agents import AGENT_DEFINITIONS, subject_writer, html_converter

# Helper to find instructions by name
def get_instructions(name):
    for n, i in AGENT_DEFINITIONS:
        if n == name:
            return i
    return ""

@function_tool
async def ask_professional_sales_agent(message: str):
    """ Ask the Professional Sales Agent to write a cold email. """
    instructions = get_instructions("Professional Sales Agent")
    return await run_with_fallback("Professional Sales Agent", instructions, message)

@function_tool
async def ask_engaging_sales_agent(message: str):
    """ Ask the Engaging Sales Agent to write a cold email. """
    instructions = get_instructions("Engaging Sales Agent")
    return await run_with_fallback("Engaging Sales Agent", instructions, message)

@function_tool
async def ask_busy_sales_agent(message: str):
    """ Ask the Busy Sales Agent to write a cold email. """
    instructions = get_instructions("Busy Sales Agent")
    return await run_with_fallback("Busy Sales Agent", instructions, message)

@function_tool
async def ask_subject_writer(message: str):
    """ Ask the Subject Writer to create a subject line. """
    return await run_with_fallback("Subject Writer", subject_writer.instructions, message)

@function_tool
async def ask_html_converter(message: str):
    """ Ask the HTML Converter to convert text to HTML. """
    return await run_with_fallback("HTML Converter", html_converter.instructions, message)
