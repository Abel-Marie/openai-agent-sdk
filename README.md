# 🤖 AI Sales Outreach Agent

An advanced, multi-agent AI system designed to automate and personalize cold sales outreach.

This application uses a team of specialized AI agents to generate high-quality email drafts, select the best one, and handle the final sending process via the Brevo API.

![AI Sales Agent Demo](demo_video_placeholder.mp4) 
*(See `demo_video.mp4` for a walkthrough)*

## 🌟 Features

*   **Multi-Agent Generation**: Three distinct agents (Professional, Engaging, Busy) generate unique drafts in parallel.
*   **Intelligent Selection**: A specialized "Sales Picker" agent reviews all drafts and selects the most effective one.
*   **Dynamic Personalization**:
    *   **Recipient Details**: Specify Name, Email, and Context/Info for each campaign.
    *   **Sender Details**: Customize the "From" Name and Email on the fly.
*   **Two-Step Verification**:
    1.  **Generate & Pick**: Create drafts and auto-select the winner.
    2.  **Finalize & Preview**: Generate the specific Subject Line and HTML Body for review.
    3.  **Send**: Dispatch the real email only when approved.
*   **Robust Architecture**: Built with `openai-agents-sdk` and `gradio` for a responsive UI.

## 🚀 Getting Started

### Prerequisites

*   Python 3.12+
*   `uv` (recommended) or `pip`
*   **API Keys**:
    *   `GEMINI_API_KEY` or `GOOGLE_API_KEY` (for AI models)
    *   `BREVO_API_KEY` (for sending emails)

### Installation

1.  **Clone the repository** (if applicable) or navigate to the project folder.
2.  **Install dependencies**:
    ```bash
    uv sync
    # OR
    pip install -r requirements.txt
    ```
3.  **Configure Environment**:
    Create a `.env` file in the root directory:
    ```ini
    GOOGLE_API_KEY=your_google_api_key
    BREVO_API_KEY=your_brevo_api_key
    # OPENROUTER_API_KEY=your_key (Optional)
    ```

### Running the App

1.  Start the application:
    ```bash
    uv run python automated_sales_outreach/app.py
    ```
2.  Open your browser at `http://127.0.0.1:7860`.

## 📖 Usage Guide

1.  **Fill Sender Details**: Enter your Name and Email (e.g., "Alice", "alice@company.com").
2.  **Fill Recipient Details**: Enter the Prospect's Name, Email, and relevant Context (e.g., "CTO looking for AI tools").
3.  **Set Campaign Goal**: Describe what you want to achieve (e.g., "Schedule a demo for our new compliance software").
4.  **Generate Drafts**: Click the button to let the 3 agents work.
5.  **Pick Best Draft**: The AI will analyze the options and choose the strongest one.
6.  **Finalize**: Click to generate the final Subject Line and HTML body.
7.  **Review**: Edit the Subject or Body in the text boxes if needed.
8.  **Send**: Click "Send Email (Real!)" to dispatch via Brevo.

## 📂 Project Structure

*   `automated_sales_outreach/app.py`: Main application entry point (Gradio UI).
*   `automated_sales_outreach/src/`:
    *   `agents.py`: Definitions of the AI agents (Professional, Engaging, Busy, Picker).
    *   `tools.py`: Tools for sending emails (`send_html_email`).
    *   `utils.py`: Helper functions for agent orchestration.
    *   `config.py`: Environment configuration and defaults.

## 🛠️ Troubleshooting

*   **API Rate Limits**: If using free models, you may encounter rate limits. The app handles this gracefully by showing errors, but waiting a minute usually resolves it.
*   **Email Not Sending**: Check your `BREVO_API_KEY` and ensure the Sender Email is authorized in your Brevo account if in sandbox mode.

---
