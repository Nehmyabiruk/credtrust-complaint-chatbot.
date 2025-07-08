```python
import gradio as gr
from src.rag_pipeline import rag_chain

def get_response(query):
    result = rag_chain({"query": query})
    return result["result"], [doc.page_content for doc in result["source_documents"]]

interface = gr.Interface(
    fn=get_response,
    inputs=gr.Textbox(lines=2, placeholder="Enter your query here..."),
    outputs=[gr.Textbox(label="Response"), gr.Textbox(label="Source Documents")],
    title="CredTrust Complaint Analysis Chatbot",
    description="Enter a query to get insights from customer complaints."
)

interface.launch()
```
