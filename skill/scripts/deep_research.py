#!/usr/bin/env python3
"""
深度研究自动化脚本 (Deep Research Script)
用于路径B — 真实人物人格提炼的增强信息搜集

用法（在 execute_code 中调用）:
    from hermes_tools import terminal, web_search, web_extract, read_file, write_file

    # 或直接作为 skill_view 的脚本引用
    # skill_view(name='soul-file-generator', file_path='scripts/deep_research.py')
"""

import json
import re
from datetime import datetime


# ============================================================
# 阶段1：基础画像
# ============================================================

def phase1_basic_profile(person_name, search_fn, extract_fn):
    """
    建立人物的基本事实框架
    
    参数:
        person_name: 人物姓名
        search_fn: 搜索函数 (web_search 或 mcp搜索)
        extract_fn: 全文提取函数 (web_extract)
    
    返回:
        dict: 基本信息卡
    """
    profile = {
        "name": person_name,
        "basic_info": {},
        "timeline": [],
        "achievements": [],
        "sources": []
    }
    
    # 搜索基本信息
    queries = [
        f"{person_name} 简介 生平 成就",
        f"{person_name} 维基百科 OR 百度百科",
    ]
    
    for q in queries:
        results = search_fn(q)
        if results:
            # 提取最相关的URL
            urls = []
            for r in results.get("results", results.get("data", {}).get("web", [])):
                url = r.get("url", r.get("link", ""))
                title = r.get("title", "")
                # 优先提取百科类页面
                if any(k in url.lower() for k in ["wiki", "baike", "edu.cn"]):
                    urls.append(url)
            
            if urls:
                extracted = extract_fn(urls[:3])
                for item in extracted.get("results", []):
                    if item.get("content"):
                        profile["sources"].append({
                            "url": item["url"],
                            "title": item.get("title", ""),
                            "type": "百科/官网",
                            "content_length": len(item["content"])
                        })
    
    return profile


# ============================================================
# 阶段2：深度素材搜集
# ============================================================

# 人物类型 → 搜索词模板映射
SEARCH_TEMPLATES = {
    "scholar": [
        "{name} 演讲 致辞 原文",
        "{name} 毕业典礼 OR 开学典礼 OR 教师节 讲话",
        "{name} 院士 OR 教授 学术 观点 理念",
        "{name} 采访 对话 专访",
        "{name} 演讲 视频 bilibili OR youtube",
    ],
    "entrepreneur": [
        "{name} CEO OR 创始人 演讲 访谈",
        "{name} 产品发布 OR 年会 致辞",
        "{name} 商业理念 OR 管理哲学",
        "{name} 创业故事 成长经历",
        "{name} 演讲 视频 youtube",
    ],
    "writer": [
        "{name} 作品 风格 写作理念",
        "{name} 访谈 对话 创作谈",
        "{name} 散文 OR 随笔 OR 博客",
        "{name} 获奖感言",
        "{name} 演讲 视频",
    ],
    "politician": [
        "{name} 演讲 讲话 政策",
        "{name} 记者会 OR 新闻发布会 文字实录",
        "{name} 专访 深度访谈",
        "{name} 回忆录 OR 自传 OR 传记",
        "{name} 演讲 视频",
    ],
    "general": [
        "{name} 演讲 致辞 原文",
        "{name} 采访 专访 对话",
        "{name} 访谈 视频",
        "{name} 评价 怎么样",
        "{name} 著作 OR 论文 OR 代表作",
    ],
}


def phase2_deep_collection(person_name, person_type, search_fn, extract_fn, zread_fn=None):
    """
    多渠道深度素材搜集
    
    参数:
        person_name: 人物姓名
        person_type: 人物类型 (scholar/entrepreneur/writer/politician/general)
        search_fn: 搜索函数
        extract_fn: 全文提取函数
        zread_fn: 深度阅读函数(可选)
    
    返回:
        dict: 收集到的所有素材
    """
    templates = SEARCH_TEMPLATES.get(person_type, SEARCH_TEMPLATES["general"])
    all_materials = {
        "speeches": [],      # 演讲全文
        "interviews": [],    # 访谈记录
        "reports": [],       # 新闻报道
        "videos": [],        # 视频信息
        "others": [],        # 其他
        "stats": {
            "total_searches": 0,
            "total_extractions": 0,
            "total_words": 0,
        }
    }
    
    for template in templates:
        query = template.format(name=person_name)
        results = search_fn(query)
        all_materials["stats"]["total_searches"] += 1
        
        if not results:
            continue
        
        # 收集URL
        urls_to_extract = []
        web_results = results.get("results", results.get("data", {}).get("web", []))
        
        for r in web_results[:5]:
            url = r.get("url", r.get("link", ""))
            title = r.get("title", "")
            snippet = r.get("snippet", r.get("content", r.get("description", "")))
            
            # 跳过不相关的URL
            if not url or person_name not in (title + snippet):
                continue
            
            # 分类
            if "视频" in title or "youtube" in url.lower() or "bilibili" in url.lower():
                all_materials["videos"].append({
                    "title": title, "url": url, "snippet": snippet,
                    "type": "video"
                })
            elif any(k in title for k in ["演讲", "致辞", "讲话", "典礼"]):
                urls_to_extract.append(url)
            elif any(k in title for k in ["访谈", "专访", "对话", "采访"]):
                urls_to_extract.append(url)
            else:
                urls_to_extract.append(url)
        
        # 批量提取全文
        if urls_to_extract:
            extracted = extract_fn(urls_to_extract[:5])
            all_materials["stats"]["total_extractions"] += len(urls_to_extract[:5])
            
            for item in extracted.get("results", []):
                content = item.get("content", "")
                if not content:
                    continue
                
                all_materials["stats"]["total_words"] += len(content)
                
                material = {
                    "url": item.get("url", ""),
                    "title": item.get("title", ""),
                    "content": content,
                    "content_length": len(content),
                    "type": _classify_content(item.get("title", ""), content),
                }
                
                # 分类存储
                if material["type"] == "speech":
                    all_materials["speeches"].append(material)
                elif material["type"] == "interview":
                    all_materials["interviews"].append(material)
                elif material["type"] == "report":
                    all_materials["reports"].append(material)
                else:
                    all_materials["others"].append(material)
    
    return all_materials


def _classify_content(title, content):
    """根据标题和内容判断素材类型"""
    title_lower = title.lower()
    if any(k in title_lower for k in ["演讲", "致辞", "讲话", "典礼", "lecture", "speech"]):
        return "speech"
    if any(k in title_lower for k in ["访谈", "专访", "对话", "采访", "interview"]):
        return "interview"
    if any(k in title_lower for k in ["报道", "新闻", "评价", "评论", "news", "report"]):
        return "report"
    return "other"


# ============================================================
# 阶段3：内容分析辅助函数
# ============================================================

def extract_quotes(text, person_name, min_length=15, max_count=20):
    """
    从文本中提取该人物的原话/金句
    
    查找模式：
    - "某某说：'...'"
    - "某某表示：'...'"
    - 引号内的独立语句
    """
    quotes = []
    
    # 模式1：XX说/表示/指出："..."
    pattern1 = rf'{person_name}[说表示指出强调认为写道称]*[：:，,]?\s*[""「]([^""」]+)[""」]'
    for match in re.finditer(pattern1, text):
        quote = match.group(1).strip()
        if min_length <= len(quote) <= 200:
            quotes.append(quote)
    
    # 模式2：独立引号句（可能是演讲原文）
    pattern2 = r'[""「]([^""」]{15,}?)[""」]'
    for match in re.finditer(pattern2, text):
        quote = match.group(1).strip()
        if quote not in quotes and min_length <= len(quote) <= 200:
            quotes.append(quote)
    
    return quotes[:max_count]


def extract_rhetorical_devices(text):
    """检测修辞手法"""
    devices = {
        "排比": 0,
        "设问": 0,
        "引用": 0,
        "比喻": 0,
    }
    
    # 排比：连续3个以上相同句式
    parallelism = re.findall(r'([^。，！？\n]{5,20})[，,]\1[，,]\1', text)
    devices["排比"] = len(parallelism)
    
    # 设问：问号后紧跟回答
    questions = re.findall(r'[？?][^？?。]{10,50}[。！]', text)
    devices["设问"] = len(questions)
    
    # 引用：引号内的名人名言
    citations = re.findall(r'[如若]——?[""「]([^""」]+)[""」]', text)
    devices["引用"] = len(citations)
    
    # 比喻："像""如同""仿佛"
    metaphors = re.findall(r'[像如]([^。，！？\n]{3,15})[一样般]', text)
    devices["比喻"] = len(metaphors)
    
    return devices


def analyze_speech_structure(text):
    """分析演讲/文章结构"""
    structure = {
        "opening": "",
        "closing": "",
        "main_points": [],
        "total_paragraphs": 0,
        "avg_paragraph_length": 0,
    }
    
    paragraphs = [p.strip() for p in text.split('\n') if p.strip() and len(p.strip()) > 20]
    structure["total_paragraphs"] = len(paragraphs)
    
    if paragraphs:
        structure["avg_paragraph_length"] = sum(len(p) for p in paragraphs) / len(paragraphs)
        structure["opening"] = paragraphs[0][:200]
        structure["closing"] = paragraphs[-1][:200]
    
    return structure


# ============================================================
# 阶段5：研究报告生成
# ============================================================

def generate_research_report(person_name, profile, materials, quality_scores):
    """生成深度研究报告（Markdown格式）"""
    
    report = f"""# 深度研究报告：{person_name}

生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}

## 研究概况

| 指标 | 数值 |
|------|------|
| 搜索次数 | {materials['stats']['total_searches']} |
| 全文提取数 | {materials['stats']['total_extractions']} |
| 视频信息数 | {len(materials['videos'])} |
| 总素材字数（估算） | {materials['stats']['total_words']:,} |

## 素材分类统计

| 类型 | 数量 |
|------|------|
| 演讲全文 | {len(materials['speeches'])} |
| 访谈记录 | {len(materials['interviews'])} |
| 新闻报道 | {len(materials['reports'])} |
| 视频信息 | {len(materials['videos'])} |
| 其他 | {len(materials['others'])} |

## 信息质量评分

| 维度 | 评分 |
|------|------|
| 素材丰富度 | {quality_scores.get('richness', 'N/A')} |
| 一手资料占比 | {quality_scores.get('primary_ratio', 'N/A')} |
| 渠道多样性 | {quality_scores.get('channel_diversity', 'N/A')} |
| 时序覆盖 | {quality_scores.get('temporal_coverage', 'N/A')} |
| 交叉验证 | {quality_scores.get('cross_validation', 'N/A')} |

## 素材清单

| # | 类型 | 标题 | 字数 | 质量 |
|---|------|------|------|------|
"""
    
    idx = 1
    for material_type in ["speeches", "interviews", "reports", "others"]:
        for m in materials[material_type]:
            title = m.get("title", "无标题")[:40]
            length = m.get("content_length", 0)
            quality = "一手" if material_type in ["speeches", "interviews"] else "二手"
            report += f"| {idx} | {material_type} | {title} | {length:,} | {quality} |\n"
            idx += 1
    
    return report


# ============================================================
# 工具适配层 — 确保脚本可以对接不同的搜索工具
# ============================================================

def make_search_fn(tool_type="mcp_web_search_prime"):
    """
    创建搜索函数适配器
    
    支持：
    - "mcp_web_search_prime" — 智谱搜索MCP
    - "web_search" — Hermes内置搜索
    - "mcp_MiniMax" — MiniMax搜索
    """
    # 这个函数需要在 execute_code 中使用 hermes_tools 来实现
    # 此处只定义接口
    pass


# ============================================================
# 主流程入口
# ============================================================

def run_deep_research(person_name, person_type="general"):
    """
    执行完整的深度研究流程
    
    参数:
        person_name: 人物姓名
        person_type: 人物类型
    
    返回:
        dict: 包含所有研究结果的字典
    
    注意：此函数需要在 Hermes execute_code 环境中运行，
    因为它依赖 hermes_tools 中的工具函数。
    
    使用示例：
    
    from hermes_tools import web_search, web_extract
    
    # 手动执行各阶段
    profile = phase1_basic_profile("张希", web_search, web_extract)
    materials = phase2_deep_collection("张希", "scholar", web_search, web_extract)
    
    # 分析素材
    for speech in materials["speeches"]:
        quotes = extract_quotes(speech["content"], "张希")
        devices = extract_rhetorical_devices(speech["content"])
        structure = analyze_speech_structure(speech["content"])
    
    # 生成报告
    report = generate_research_report("张希", profile, materials, quality_scores)
    print(report)
    """
    pass
