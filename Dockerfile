# 使用 Python 3.11 作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# 暴露端口 (Gradio 默认使用 7860)
EXPOSE 7860

# 启动命令
CMD ["python", "src/main.py"] 