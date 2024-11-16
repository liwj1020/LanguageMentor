import gradio as gr
from tabs.scenario_tab import create_scenario_tab
from tabs.conversation_tab import create_conversation_tab
from tabs.vocab_tab import create_vocab_tab
from utils.logger import LOG

def main():
    with gr.Blocks(title="LanguageMentor 英语私教") as language_mentor_app:
        create_scenario_tab()
        create_conversation_tab()
        create_vocab_tab()
    
    # 启动应用，使用环境变量配置
    language_mentor_app.launch(
        server_name="0.0.0.0",  # 允许外部访问
        server_port=7860,       # 明确指定端口
        share=False             # 在容器中运行时不需要share
    )

if __name__ == "__main__":
    main()
