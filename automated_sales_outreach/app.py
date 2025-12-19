import gradio as gr
import asyncio
from src.agents import AGENT_DEFINITIONS, sales_picker_instructions
from src.utils import run_agent_with_fallback, run_with_fallback
from src.tools import send_html_email
from src.agent_tools import (
    ask_professional_sales_agent,
    ask_engaging_sales_agent,
    ask_busy_sales_agent,
    ask_subject_writer,
    ask_html_converter
)

# --- Logic Functions for Gradio ---

async def generate_drafts(prompt, rec_name, rec_info, send_name, send_email):
    """ Generates 3 drafts in parallel, enriching prompt with recipient and sender info """
    
    sender_context = f"\nSender Name: {send_name}" if send_name else ""
    enriched_prompt = f"{prompt}\n\nRecipient Information:\nName: {rec_name}\nDetails: {rec_info}{sender_context}"
    
    results = await asyncio.gather(
        *[
            run_agent_with_fallback(name, instructions, enriched_prompt)
            for name, instructions in AGENT_DEFINITIONS
        ]
    )
    return results[0], results[1], results[2]

async def pick_best_draft(draft1, draft2, draft3):
    """ Picks the best draft from the 3 inputs """
    if not (draft1 and draft2 and draft3):
        return "Please generate drafts first."
    
    emails = f"Cold sales emails:\n\nEmail 1:\n{draft1}\n\nEmail 2:\n{draft2}\n\nEmail 3:\n{draft3}"
    best = await run_with_fallback(
        agent_name="Sales Picker",
        instructions=sales_picker_instructions,
        message=emails,
    )
    return best

async def finalize_draft(best_draft):
    """ Takes the best draft, adds subject, and returns editable preview inputs """
    if not best_draft:
        return "No draft selected.", "Failed"

    # Generate Subject
    subject = await run_with_fallback("Subject Writer", "Write a catchy subject line.", best_draft)
    
    # Convert to HTML (Initial pass)
    html_body = await run_with_fallback("HTML Converter", "Convert text to HTML.", best_draft)
    
    return subject, html_body

async def send_final_email(subject, html_body, rec_email, rec_name, send_email, send_name):
    """ Takes the finalized subject/body and sends it """
    
    # Note: Using the actual tool here to send with dynamic recipient and sender
    result = send_html_email(
        subject=subject, 
        html_body=html_body, 
        to_email=rec_email, 
        to_name=rec_name,
        from_email=send_email,
        from_name=send_name
    )
    
    return str(result)

# --- Gradio UI Layout ---

with gr.Blocks(title="AI Sales Agent") as demo:
    gr.Markdown("# 🤖 AI Sales Outreach Agent")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 1. Sender Details")
            send_name = gr.Textbox(label="Sender Name", placeholder="e.g. Alice Smith")
            send_email = gr.Textbox(label="Sender Email", placeholder="e.g. alice@company.com")

            gr.Markdown("### 2. Recipient Details")
            rec_name = gr.Textbox(label="Recipient Name", placeholder="e.g. John Doe")
            rec_email = gr.Textbox(label="Recipient Email", placeholder="e.g. john@example.com")
            rec_info = gr.Textbox(label="Recipient Info / Context", placeholder="e.g. CTO at TechCorp, interested in AI security", lines=3)
        
        with gr.Column(scale=2):
            gr.Markdown("### 3. Campaign Prompt")
            prompt_input = gr.Textbox(label="Campaign Goal", value="Write a cold email about our AI compliance tool.", lines=5)
            generate_btn = gr.Button("Generate Drafts", variant="primary")
    
    gr.Markdown("### 4. Draft Generation")
    with gr.Row():
        draft1_out = gr.Textbox(label="Professional Agent Draft", lines=10)
        draft2_out = gr.Textbox(label="Engaging Agent Draft", lines=10)
        draft3_out = gr.Textbox(label="Busy Agent Draft", lines=10)
    
    pick_btn = gr.Button("Pick Best Draft", variant="secondary")
    best_draft_out = gr.Textbox(label="Selected Best Draft", lines=10)
    
    gr.Markdown("### 5. Finalize & Send")
    finalize_btn = gr.Button("Finalize (Create Subject & HTML)", variant="secondary")
    
    with gr.Row():
        final_subject = gr.Textbox(label="Final Subject Line", lines=1)
        # Note: HTML Preview is now an input so user can edit if needed
        final_html = gr.Textbox(label="Final Email Body (HTML)", lines=5)
    
    send_btn = gr.Button("Send Email (Real!)", variant="stop")
    send_status = gr.Textbox(label="Send Status")

    # Event Wiring
    generate_btn.click(
        fn=generate_drafts,
        inputs=[prompt_input, rec_name, rec_info, send_name, send_email],
        outputs=[draft1_out, draft2_out, draft3_out]
    )
    
    pick_btn.click(
        fn=pick_best_draft,
        inputs=[draft1_out, draft2_out, draft3_out],
        outputs=[best_draft_out]
    )
    
    finalize_btn.click(
        fn=finalize_draft,
        inputs=[best_draft_out],
        outputs=[final_subject, final_html]
    )
    
    send_btn.click(
        fn=send_final_email,
        inputs=[final_subject, final_html, rec_email, rec_name, send_email, send_name],
        outputs=[send_status]
    )

if __name__ == "__main__":
    demo.launch()
