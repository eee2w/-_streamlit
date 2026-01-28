import streamlit as st
from streamlit.components.v1 import html

# 设置页面配置
st.set_page_config(
    page_title="游戏工具导航",
    page_icon="🎮",
    layout="centered"
)

# 自定义CSS样式 (为可点击的div增加了指针样式)
st.markdown("""
<style>
    .header {
        text-align: center;
        padding: 20px 0;
        margin-bottom: 30px;
    }
    
    .app-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .app-card:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.15);
    }
    
    .app-title {
        font-size: 1.4rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 5px;
    }
    
    .app-description {
        font-size: 0.95rem;
        color: #666;
        margin-bottom: 15px;
    }
    
    /* 修改：将 .app-link 从 a 标签的样式改为 div 的样式，并保留指针 */
    .app-link {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 8px 16px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        transition: background 0.3s ease;
        cursor: pointer; /* 关键：让div显示为可点击的手型指针 */
    }
    
    .app-link:hover {
        background: #764ba2;
        color: white;
        text-decoration: none;
    }
    
    .status-badge {
        display: inline-block;
        font-size: 0.75rem;
        font-weight: 500;
        margin-left: 8px;
        color: #666;
        vertical-align: middle;
    }
    
    .status-online {
        color: #10B981;
    }
    
    .status-dev {
        color: #F59E0B;
    }
    
    .feedback-note {
        text-align: center;
        margin-top: 40px;
        padding: 15px;
        background-color: #f8f9fa;
        border-radius: 10px;
        font-size: 0.9rem;
        color: #666;
        border-left: 4px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# 应用标题
st.markdown("""
<div class="header">
    <h1 style="margin:0;">🎮 游戏工具导航</h1>
</div>
""", unsafe_allow_html=True)

# 您的应用信息列表
apps = [
    {
        "name": "资源计算器",
        "url": "https://azbapcbtjvkpq8esq5q8f2.streamlit.app/",
        "description": "计算包裹内资源总量",
        "icon": "📊",
        "status": "online"
    },
    {
        "name": "神兵玉石消耗计算",
        "url": "https://eu5fctgjsakgp8strse8ku.streamlit.app/",
        "description": "计算神兵玉石升级消耗以及活动积分兑换是否充足",
        "icon": "⚔️",
        "status": "online"
    },
    {
        "name": "积分兑换神兵玉石材料自动推荐",
        "url": "https://cenpecvplwojqgxvtn5y5n.streamlit.app/",
        "description": "智能推荐活动积分如何兑换神兵玉石材料",
        "icon": "📅",
        "status": "online"
    }
]

# 显示应用卡片
for app in apps:
    # 状态标签
    status_text = "（可使用）" if app["status"] == "online" else "（开发中）"
    status_class = "status-online" if app["status"] == "online" else "status-dev"
    
    # 创建卡片HTML
    # 关键修改：将 <a> 标签替换为具有 onclick 事件的 <div>
    card_html = f"""
    <div class="app-card">
        <div class="app-title">
            {app["icon"]} {app["name"]}
            <span class="status-badge {status_class}">{status_text}</span>
        </div>
        <div class="app-description">
            {app["description"]}
        </div>
        <!-- 核心改动：用 div 替代 a 标签，通过 onclick 跳转 -->
        <div class="app-link" onclick="window.open('{app["url"]}', '_blank');">
            打开应用 →
        </div>
    </div>
    """
    # 渲染卡片
    html(card_html)

# 添加管理员反馈提示
st.markdown("""
<div class="feedback-note">
    <strong>💡 提示：</strong> 遇到问题或需要功能改进，请找管理员反馈
</div>
""", unsafe_allow_html=True)
