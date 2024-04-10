from typing import Generator, List

import gradio as gr
import ollama


def format_history(
    msg: str, history: List[List[str]], system_prompt: str
) -> List[dict]:
    chat_history = [{"role": "system", "content": system_prompt}]
    for query, response in history:
        chat_history.append({"role": "user", "content": query})
        chat_history.append({"role": "assistant", "content": response})
    chat_history.append({"role": "user", "content": msg})
    return chat_history


def generate_response(
    msg: str, history: List[List[str]], system_prompt: str
) -> Generator[str, None, None]:
    chat_history = format_history(msg, history, system_prompt)
    response = ollama.chat(model="gemma:2b", stream=True, messages=chat_history)
    message = ""
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        message += token
        yield message


chatbot = gr.ChatInterface(
    generate_response,
    chatbot=gr.Chatbot(avatar_images=("user.jpg", "chatbot.png"), height="64vh"),
    additional_inputs=[
        gr.Textbox("Behave as if you are professional writer.", label="System Prompt")
    ],
    title="gemma-2 (2B) Chatbot using 'Ollama'",
    description="Feel free to ask any question.",
    theme="soft",
    submit_btn="⬅ Send",
    retry_btn="🔄 Regenerate Response",
    undo_btn="↩ Delete Previous",
    clear_btn="🗑️ Clear Chat",
)

chatbot.launch()
