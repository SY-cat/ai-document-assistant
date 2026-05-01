import gradio as gr
import subprocess
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent import DocumentAgent

# Initialize agent
agent = DocumentAgent(name="DocAssist")

def process_input(user_input):
    """Process user input and return agent response"""
    if not user_input.strip():
        return "请输入指令..."
    
    try:
        response = agent.process_command(user_input)
        return response
    except Exception as e:
        return f"❌ 错误: {str(e)}"

def clear_history():
    """Clear conversation history"""
    agent.conversation_history = []
    agent.memory = __import__('agent.memory', fromlist=['AgentMemory']).AgentMemory()
    return "", "历史记录已清空！"

with gr.Blocks(
    title="AI Document Assistant Agent",
    theme=gr.themes.Soft(),
    css="""
    .header { text-align: center; margin-bottom: 20px; }
    .footer { text-align: center; margin-top: 20px; color: #666; font-size: 12px; }
    """
) as demo:
    
    gr.HTML("""
    <div class="header">
        <h1>🤖 AI Document Assistant Agent</h1>
        <p>基于 AI Agent 的智能文档处理助手 — 支持文档总结、智能搜索、内容生成、文档对比</p>
    </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(
                label="对话",
                height=500,
                type="messages"
            )
        
        with gr.Column(scale=1):
            gr.Markdown("### 💡 示例指令")
            gr.Markdown("""
            - `总结 quarterly_report.pdf`
            - `搜索所有提到预算的内容`
            - `生成项目状态报告`
            - `对比 doc1.pdf 和 doc2.pdf`
            - `提取文档中的关键信息`
            """)
            
            clear_btn = gr.Button("🗑️ 清空对话", variant="secondary")
    
    with gr.Row():
        txt_input = gr.Textbox(
            label="输入指令",
            placeholder="输入你的指令，例如：总结文档...",
            lines=2
        )
    
    with gr.Row():
        submit_btn = gr.Button("🚀 发送", variant="primary")
        gr.Markdown("项目源码：https://github.com/SY-cat/ai-document-assistant")
    
    # Event handlers
    def user_message(user_input, history):
        return "", history + [{"role": "user", "content": user_input}]
    
    def bot_response(history):
        user_msg = history[-1]["content"]
        bot_msg = process_input(user_msg)
        history.append({"role": "assistant", "content": bot_msg})
        return history
    
    txt_input.submit(
        user_message,
        [txt_input, chatbot],
        [txt_input, chatbot],
        queue=False
    ).then(
        bot_response,
        chatbot,
        chatbot
    )
    
    submit_btn.click(
        user_message,
        [txt_input, chatbot],
        [txt_input, chatbot],
        queue=False
    ).then(
        bot_response,
        chatbot,
        chatbot
    )
    
    clear_btn.click(
        lambda: ([], ""),
        None,
        [chatbot, txt_input],
        queue=False
    )
    
    gr.HTML("""
    <div class="footer">
        <p>📦 开源项目：<a href="https://github.com/SY-cat/ai-document-assistant" target="_blank">github.com/SY-cat/ai-document-assistant</a></p>
        <p>⚡ Powered by AI Agent | Built with Gradio</p>
    </div>
    """)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,  # This creates a public link!
        debug=True
    )
