import streamlit as st
from streamlit.components.v1 import html

# 设置页面配置
st.set_page_config(
    page_title="游戏工具导航",
    page_icon="🎮",
    layout="centered"
)

# 注入复制功能所需的JavaScript
copy_js = """
<script>
function copyAppUrl(url, appName) {
    // 方法1: 使用现代Clipboard API
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(url)
            .then(() => {
                alert("✓ 已复制【" + appName + "】链接！\\n\\n链接已保存到剪贴板，请在浏览器中粘贴访问。");
            })
            .catch(err => {
                // 如果现代API失败，回退到传统方法
                fallbackCopyText(url, appName);
            });
    } else {
        // 方法2: 传统方法作为备选
        fallbackCopyText(url, appName);
    }
}

function fallbackCopyText(url, appName) {
    // 创建临时输入框
    var textArea = document.createElement("textarea");
    textArea.value = url;
    textArea.style.position = "fixed";
    textArea.style.left = "-999999px";
    textArea.style.top = "-999999px";
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    
    try {
        var successful = document.execCommand('copy');
        if (successful) {
            alert("✓ 已复制【" + appName + "】链接！\\n\\n链接已保存到剪贴板，请在浏览器中粘贴访问。");
        } else {
            alert("⚠️ 复制失败，请手动选择并复制链接：\\n\\n" + url);
        }
    } catch (err) {
        alert("⚠️ 复制失败，请手动选择并复制链接：\\n\\n" + url);
    }
    
    document.body.removeChild(textArea);
}
</script>
"""

st.markdown(copy_js, unsafe_allow_html=True)

# 自定义CSS样式
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
        margin: 20px 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .app-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(0,0,0,0.15);
    }
    
    .app-title {
        font-size: 1.4rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 8px;
    }
    
    .app-description {
        font-size: 0.95rem;
        color: #666;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    
    .button-container {
        display: flex;
        gap: 12px;
        margin-top: 5px;
    }
    
    .app-link {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 8px 16px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        text-align: center;
        flex: 1;
        border: none;
        cursor: pointer;
    }
    
    .app-link:hover {
        background: #764ba2;
        color: white;
        text-decoration: none;
        transform: translateY(-1px);
    }
    
    .copy-btn {
        display: inline-block;
        background: #10B981;
        color: white;
        padding: 8px 16px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        text-align: center;
        flex: 1;
        border: none;
        cursor: pointer;
    }
    
    .copy-btn:hover {
        background: #0da271;
        transform: translateY(-1px);
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
    
    .wechat-tip {
        text-align: center;
        margin: 25px 0 15px 0;
        padding: 12px;
        background-color: #fff8e1;
        border-radius: 8px;
        font-size: 0.9rem;
        color: #333;
        border-left: 4px solid #ffc107;
        line-height: 1.6;
    }
    
    .tip-icon {
        font-size: 1.1rem;
        margin-right: 6px;
    }
</style>
""", unsafe_allow_html=True)

# 应用标题
st.markdown("""
<div class="header">
    <h1 style="margin:0;">🎮 游戏工具导航</h1>
</div>
""", unsafe_allow_html=True)

# 微信环境提示
st.markdown("""
<div class="wechat-tip">
    <span class="tip-icon">📱</span>
    <strong>微信内访问提示：</strong>如果"打开应用"按钮无法正常跳转，请使用"复制链接"按钮，然后将链接粘贴到手机浏览器中打开。
</div>
""", unsafe_allow_html=True)

# 您的3个应用信息（请替换为您的实际链接）
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
    
    # 创建卡片HTML - 现在有两个按钮
    card_html = f"""
    <div class="app-card">
        <div class="app-title">
            {app["icon"]} {app["name"]}
            <span class="status-badge {status_class}">{status_text}</span>
        </div>
        <div class="app-description">
            {app["description"]}
        </div>
        
        <div class="button-container">
            <!-- 原有的打开应用按钮 -->
            <a href="{app["url"]}" target="_blank" class="app-link">
                打开应用 →
            </a>
            
            <!-- 新增的复制链接按钮 -->
            <button class="copy-btn" onclick="copyAppUrl('{app["url"]}', '{app["name"]}')">
                复制链接
            </button>
        </div>
    </div>
    """
    
    # 渲染卡片
    html(card_html)
