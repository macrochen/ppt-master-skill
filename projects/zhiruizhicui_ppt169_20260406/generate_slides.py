#!/usr/bin/env python3
"""
生成高端植萃身体护理系列 PPT 的 SVG 页面
风格：奢华美妆、自然纯净、优雅留白
"""

import os

PROJECT_DIR = "/Users/shi/.agents/skills/ppt-master-skill/projects/zhiruizhicui_ppt169_20260406/svg_output"

# 画布尺寸：16:9 (1280x720)
WIDTH = 1280
HEIGHT = 720

# 配色方案
COLORS = {
    'bg_cream': '#FAF8F5',
    'bg_ivory': '#F8F6F0',
    'gold': '#C9A962',
    'gold_light': '#D4BC7E',
    'forest': '#2D4A3E',
    'forest_light': '#4A6B5A',
    'text_dark': '#2C2C2C',
    'text_gray': '#6B6B6B',
    'text_light': '#9B9B9B',
}

def create_slide_1_cover():
    """封面页"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{COLORS['bg_ivory']}"/>
      <stop offset="100%" style="stop-color:{COLORS['bg_cream']}"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{COLORS['gold']}"/>
      <stop offset="100%" style="stop-color:{COLORS['gold_light']}"/>
    </linearGradient>
  </defs>
  
  <!-- 背景 -->
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bgGrad)"/>
  
  <!-- 装饰线条 -->
  <line x1="200" y1="300" x2="400" y2="300" stroke="{COLORS['gold']}" stroke-width="1" opacity="0.6"/>
  <line x1="880" y1="300" x2="1080" y2="300" stroke="{COLORS['gold']}" stroke-width="1" opacity="0.6"/>
  
  <!-- 主标题 -->
  <text x="{WIDTH/2}" y="280" font-family="Noto Serif SC, serif" font-size="64" 
        fill="{COLORS['forest']}" text-anchor="middle" font-weight="300" letter-spacing="8">
    植愈身心，原生奢养
  </text>
  
  <!-- 副标题 -->
  <text x="{WIDTH/2}" y="340" font-family="Noto Sans SC, sans-serif" font-size="24" 
        fill="{COLORS['text_gray']}" text-anchor="middle" letter-spacing="4">
    纯天然植萃身体护理系列企划汇报
  </text>
  
  <!-- 分隔装饰 -->
  <circle cx="{WIDTH/2}" cy="420" r="3" fill="{COLORS['gold']}"/>
  <line x1="{WIDTH/2-60}" y1="420" x2="{WIDTH/2-10}" y2="420" stroke="{COLORS['gold']}" stroke-width="0.5"/>
  <line x1="{WIDTH/2+10}" y1="420" x2="{WIDTH/2+60}" y2="420" stroke="{COLORS['gold']}" stroke-width="0.5"/>
  
  <!-- 底部文案 -->
  <text x="{WIDTH/2}" y="520" font-family="Noto Serif SC, serif" font-size="18" 
        fill="{COLORS['text_light']}" text-anchor="middle" letter-spacing="6" font-style="italic">
    跨越山海的全球植萃寻香之旅
  </text>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">01</text>
</svg>'''
    return svg

def create_slide_2_toc():
    """目录页"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['bg_cream']}"/>
  
  <!-- 标题 -->
  <text x="120" y="140" font-family="Noto Serif SC, serif" font-size="36" 
        fill="{COLORS['forest']}" font-weight="300">目录</text>
  <text x="120" y="165" font-family="Noto Sans SC, sans-serif" font-size="14" 
        fill="{COLORS['gold']}" letter-spacing="3">CONTENTS</text>
  
  <!-- 章节列表 -->
  <g transform="translate(120, 240)">
    <!-- 章节1 -->
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="14" 
          fill="{COLORS['gold']}" letter-spacing="2">01</text>
    <text x="60" y="0" font-family="Noto Sans SC, sans-serif" font-size="22" 
          fill="{COLORS['text_dark']}" font-weight="300">品牌核心理念与核心优势</text>
    <text x="60" y="28" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['text_gray']}">全球植萃故事</text>
    
    <!-- 章节2 -->
    <text x="0" y="100" font-family="Noto Serif SC, serif" font-size="14" 
          fill="{COLORS['gold']}" letter-spacing="2">02</text>
    <text x="60" y="100" font-family="Noto Sans SC, sans-serif" font-size="22" 
          fill="{COLORS['text_dark']}" font-weight="300">产品矩阵整体规划</text>
    <text x="60" y="128" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['text_gray']}">全链路护理逻辑</text>
    
    <!-- 章节3 -->
    <text x="0" y="200" font-family="Noto Serif SC, serif" font-size="14" 
          fill="{COLORS['gold']}" letter-spacing="2">03</text>
    <text x="60" y="200" font-family="Noto Sans SC, sans-serif" font-size="22" 
          fill="{COLORS['text_dark']}" font-weight="300">五款产品详细解析</text>
    <text x="60" y="228" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['text_gray']}">痛点 + 解决方案 + 核心卖点</text>
  </g>
  
  <!-- 装饰线 -->
  <line x1="120" y1="580" x2="300" y2="580" stroke="{COLORS['gold']}" stroke-width="0.5" opacity="0.5"/>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">02</text>
</svg>'''
    return svg

def create_slide_3_concept():
    """品牌核心理念页"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['bg_cream']}"/>
  
  <!-- 章节标题 -->
  <text x="120" y="100" font-family="Noto Serif SC, serif" font-size="14" 
        fill="{COLORS['gold']}" letter-spacing="3">CHAPTER 01</text>
  
  <!-- 主标题 -->
  <text x="{WIDTH/2}" y="200" font-family="Noto Serif SC, serif" font-size="48" 
        fill="{COLORS['forest']}" text-anchor="middle" font-weight="300" letter-spacing="6">
    植愈身心，原生奢养
  </text>
  
  <!-- 副标题 -->
  <text x="{WIDTH/2}" y="250" font-family="Noto Sans SC, sans-serif" font-size="16" 
        fill="{COLORS['text_gray']}" text-anchor="middle" letter-spacing="2">
    品牌核心理念
  </text>
  
  <!-- 分隔线 -->
  <line x1="{WIDTH/2-100}" y1="290" x2="{WIDTH/2+100}" y2="290" stroke="{COLORS['gold']}" stroke-width="0.5"/>
  
  <!-- 内容区域 -->
  <g transform="translate(150, 340)">
    <text x="0" y="0" font-family="Noto Sans SC, sans-serif" font-size="16" 
          fill="{COLORS['text_dark']}" line-height="1.8">
      我们的初心，是跨越山海，探寻全球每一寸黄金植萃产地
    </text>
    <text x="0" y="40" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['text_gray']}">
      只为将自然本真的修护力量，注入每一瓶身体护理产品中
    </text>
  </g>
  
  <!-- 四大洲标签 -->
  <g transform="translate(150, 460)">
    <rect x="0" y="0" width="140" height="80" fill="none" stroke="{COLORS['gold']}" stroke-width="0.5" opacity="0.5"/>
    <text x="70" y="35" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['forest']}" text-anchor="middle">法国普罗旺斯</text>
    <text x="70" y="55" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_gray']}" text-anchor="middle">鸢尾花</text>
    
    <rect x="180" y="0" width="140" height="80" fill="none" stroke="{COLORS['gold']}" stroke-width="0.5" opacity="0.5"/>
    <text x="250" y="35" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['forest']}" text-anchor="middle">澳洲南澳</text>
    <text x="250" y="55" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_gray']}" text-anchor="middle">药蜀葵根</text>
    
    <rect x="360" y="0" width="140" height="80" fill="none" stroke="{COLORS['gold']}" stroke-width="0.5" opacity="0.5"/>
    <text x="430" y="35" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['forest']}" text-anchor="middle">中国长白山</text>
    <text x="430" y="55" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_gray']}" text-anchor="middle">赤芝 · 人参</text>
    
    <rect x="540" y="0" width="140" height="80" fill="none" stroke="{COLORS['gold']}" stroke-width="0.5" opacity="0.5"/>
    <text x="610" y="35" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['forest']}" text-anchor="middle">比利时</text>
    <text x="610" y="55" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_gray']}" text-anchor="middle">顶级兰花</text>
  </g>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">03</text>
</svg>'''
    return svg

def create_slide_4_advantages():
    """核心优势页"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['bg_cream']}"/>
  
  <!-- 标题 -->
  <text x="120" y="100" font-family="Noto Serif SC, serif" font-size="36" 
        fill="{COLORS['forest']}" font-weight="300">核心优势</text>
  <text x="120" y="125" font-family="Noto Sans SC, sans-serif" font-size="14" 
        fill="{COLORS['gold']}" letter-spacing="3">CORE ADVANTAGES</text>
  
  <!-- 五大优势 -->
  <g transform="translate(120, 180)">
    <!-- 优势1 -->
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">原料来源</text>
    <text x="0" y="30" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['text_gray']}">全球黄金产区直采，四大洲有机认证</text>
    
    <!-- 优势2 -->
    <text x="380" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">植萃技术</text>
    <text x="380" y="30" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['text_gray']}">超临界CO₂低温萃取，100%保留活性</text>
    
    <!-- 优势3 -->
    <text x="760" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">品牌调性</text>
    <text x="760" y="30" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['text_gray']}">全球植萃、天然奢护、身心疗愈</text>
    
    <!-- 优势4 -->
    <text x="0" y="100" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">产品适配</text>
    <text x="0" y="130" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['text_gray']}">覆盖20-45岁女性全维度肌肤问题</text>
    
    <!-- 优势5 -->
    <text x="380" y="100" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">安全标准</text>
    <text x="380" y="130" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['text_gray']}">98%+天然来源，0添加，孕妇敏肌友好</text>
  </g>
  
  <!-- 0添加清单 -->
  <g transform="translate(120, 400)">
    <text x="0" y="0" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['forest']}" font-weight="500">安全承诺</text>
    <text x="0" y="35" font-family="Noto Sans SC, sans-serif" font-size="24" 
          fill="{COLORS['gold']}" letter-spacing="8">0酒精 · 0香精 · 0色素 · 0矿物油</text>
  </g>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">04</text>
</svg>'''
    return svg

def create_slide_5_matrix():
    """产品矩阵页"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['bg_cream']}"/>
  
  <!-- 章节标题 -->
  <text x="120" y="80" font-family="Noto Serif SC, serif" font-size="14" 
        fill="{COLORS['gold']}" letter-spacing="3">CHAPTER 02</text>
  <text x="120" y="110" font-family="Noto Sans SC, sans-serif" font-size="32" 
        fill="{COLORS['forest']}" font-weight="300">产品矩阵</text>
  
  <!-- 表格 -->
  <g transform="translate(80, 150)">
    <!-- 表头 -->
    <rect x="0" y="0" width="140" height="50" fill="{COLORS['forest']}" opacity="0.1"/>
    <rect x="140" y="0" width="260" height="50" fill="{COLORS['forest']}" opacity="0.1"/>
    <rect x="400" y="0" width="240" height="50" fill="{COLORS['forest']}" opacity="0.1"/>
    <rect x="640" y="0" width="180" height="50" fill="{COLORS['forest']}" opacity="0.1"/>
    <rect x="820" y="0" width="200" height="50" fill="{COLORS['forest']}" opacity="0.1"/>
    
    <text x="70" y="32" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['forest']}" text-anchor="middle" font-weight="500">核心痛点</text>
    <text x="270" y="32" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['forest']}" text-anchor="middle" font-weight="500">对应产品</text>
    <text x="520" y="32" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['forest']}" text-anchor="middle" font-weight="500">核心植萃成分</text>
    <text x="730" y="32" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['forest']}" text-anchor="middle" font-weight="500">核心功效</text>
    <text x="920" y="32" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['forest']}" text-anchor="middle" font-weight="500">适配人群</text>
    
    <!-- 行1 -->
    <rect x="0" y="50" width="140" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="140" y="50" width="260" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="400" y="50" width="240" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="640" y="50" width="180" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="820" y="50" width="200" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    
    <text x="70" y="80" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">痘痘、毛周角化</text>
    <text x="270" y="80" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">灵芝清透祛痘身体喷雾</text>
    <text x="520" y="80" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">长白山有机赤芝</text>
    <text x="730" y="80" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">祛痘淡印、改善鸡皮</text>
    <text x="920" y="80" font-family="Noto Sans SC, sans-serif" font-size="11" 
          fill="{COLORS['text_gray']}" text-anchor="middle">油痘肌、敏肌友好</text>
    
    <!-- 行2 -->
    <rect x="0" y="120" width="140" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="140" y="120" width="260" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="400" y="120" width="240" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="640" y="120" width="180" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="820" y="120" width="200" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    
    <text x="70" y="150" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">干、痒、皮屑</text>
    <text x="270" y="150" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">药蜀葵根深层保湿身体乳</text>
    <text x="520" y="150" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">南澳有机药蜀葵根</text>
    <text x="730" y="150" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">深层补水、长效锁水</text>
    <text x="920" y="150" font-family="Noto Sans SC, sans-serif" font-size="11" 
          fill="{COLORS['text_gray']}" text-anchor="middle">干皮、敏肌、40+熟龄肌</text>
    
    <!-- 行3 -->
    <rect x="0" y="190" width="140" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="140" y="190" width="260" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="400" y="190" width="240" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="640" y="190" width="180" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="820" y="190" width="200" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    
    <text x="70" y="220" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">松弛、颈纹</text>
    <text x="270" y="220" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">人参焕活紧致身体精华油</text>
    <text x="520" y="220" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">长白山有机人参</text>
    <text x="730" y="220" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">紧致抗老、淡化颈纹</text>
    <text x="920" y="220" font-family="Noto Sans SC, sans-serif" font-size="11" 
          fill="{COLORS['text_gray']}" text-anchor="middle">35+熟龄肌用户</text>
    
    <!-- 行4 -->
    <rect x="0" y="260" width="140" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="140" y="260" width="260" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="400" y="260" width="240" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="640" y="260" width="180" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="820" y="260" width="200" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    
    <text x="70" y="290" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">黑、黄、暗沉</text>
    <text x="270" y="290" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">鸢尾花焕亮美白身体乳</text>
    <text x="520" y="290" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">法国普罗旺斯鸢尾花</text>
    <text x="730" y="290" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">美白淡斑、改善色沉</text>
    <text x="920" y="290" font-family="Noto Sans SC, sans-serif" font-size="11" 
          fill="{COLORS['text_gray']}" text-anchor="middle">美白需求、敏肌、干皮</text>
    
    <!-- 行5 -->
    <rect x="0" y="330" width="140" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="140" y="330" width="260" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="400" y="330" width="240" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="640" y="330" width="180" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    <rect x="820" y="330" width="200" height="70" fill="none" stroke="{COLORS['gold']}" stroke-width="0.3" opacity="0.3"/>
    
    <text x="70" y="360" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">妊娠纹、肥胖纹</text>
    <text x="270" y="360" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">兰花修护淡纹身体油</text>
    <text x="520" y="360" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">比利时顶级兰花</text>
    <text x="730" y="360" font-family="Noto Sans SC, sans-serif" font-size="12" 
          fill="{COLORS['text_dark']}" text-anchor="middle">修护淡纹、预防纹路</text>
    <text x="920" y="360" font-family="Noto Sans SC, sans-serif" font-size="11" 
          fill="{COLORS['text_gray']}" text-anchor="middle">孕期/产后女性、敏肌友好</text>
  </g>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">05</text>
</svg>'''
    return svg

def create_slide_6_product1():
    """产品1：灵芝"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['bg_cream']}"/>
  
  <!-- 章节标题 -->
  <text x="120" y="80" font-family="Noto Serif SC, serif" font-size="14" 
        fill="{COLORS['gold']}" letter-spacing="3">CHAPTER 03 · 产品 01</text>
  
  <!-- 产品名称 -->
  <text x="120" y="130" font-family="Noto Sans SC, sans-serif" font-size="32" 
        fill="{COLORS['forest']}" font-weight="300">灵芝清透祛痘身体喷雾</text>
  
  <!-- 核心成分 -->
  <g transform="translate(120, 180)">
    <rect x="0" y="0" width="200" height="40" fill="{COLORS['forest']}" opacity="0.1"/>
    <text x="100" y="26" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['forest']}" text-anchor="middle">长白山有机赤芝</text>
  </g>
  
  <!-- 功效 -->
  <g transform="translate(120, 260)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">核心功效</text>
    <text x="0" y="40" font-family="Noto Sans SC, sans-serif" font-size="20" 
          fill="{COLORS['text_dark']}" letter-spacing="4">祛痘淡印 · 改善鸡皮 · 屏障修护</text>
  </g>
  
  <!-- 卖点 -->
  <g transform="translate(120, 360)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">核心优势</text>
    <text x="0" y="35" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['text_gray']}">喷雾设计，背部轻松护理，清爽不黏腻</text>
    <text x="0" y="60" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['text_gray']}">天然植萃温和祛痘，敏肌友好</text>
  </g>
  
  <!-- 适配人群 -->
  <g transform="translate(120, 480)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="14" 
          fill="{COLORS['text_light']}">适配人群</text>
    <text x="0" y="28" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['text_gray']}">油痘肌 · 后背/前胸痘痘 · 毛周角化</text>
  </g>
  
  <!-- 装饰 -->
  <rect x="900" y="150" width="200" height="400" fill="{COLORS['forest']}" opacity="0.05"/>
  <text x="1000" y="350" font-family="Noto Serif SC, serif" font-size="120" 
        fill="{COLORS['gold']}" opacity="0.1" text-anchor="middle">灵</text>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">06</text>
</svg>'''
    return svg

def create_slide_7_product2():
    """产品2：药蜀葵根"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['bg_cream']}"/>
  
  <!-- 章节标题 -->
  <text x="120" y="80" font-family="Noto Serif SC, serif" font-size="14" 
        fill="{COLORS['gold']}" letter-spacing="3">CHAPTER 03 · 产品 02</text>
  
  <!-- 产品名称 -->
  <text x="120" y="130" font-family="Noto Sans SC, sans-serif" font-size="32" 
        fill="{COLORS['forest']}" font-weight="300">药蜀葵根深层保湿身体乳</text>
  
  <!-- 核心成分 -->
  <g transform="translate(120, 180)">
    <rect x="0" y="0" width="220" height="40" fill="{COLORS['forest']}" opacity="0.1"/>
    <text x="110" y="26" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['forest']}" text-anchor="middle">南澳有机药蜀葵根</text>
  </g>
  
  <!-- 功效 -->
  <g transform="translate(120, 260)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">核心功效</text>
    <text x="0" y="40" font-family="Noto Sans SC, sans-serif" font-size="20" 
          fill="{COLORS['text_dark']}" letter-spacing="4">深层补水 · 长效锁水 · 舒缓干痒</text>
  </g>
  
  <!-- 卖点 -->
  <g transform="translate(120, 360)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">核心优势</text>
    <text x="0" y="35" font-family="Noto Sans SC, sans-serif" font-size="18" 
          fill="{COLORS['text_dark']}">800倍巨量锁水</text>
    <text x="0" y="65" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['text_gray']}">48小时长效保湿，敏肌、孕妇友好</text>
  </g>
  
  <!-- 适配人群 -->
  <g transform="translate(120, 480)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="14" 
          fill="{COLORS['text_light']}">适配人群</text>
    <text x="0" y="28" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['text_gray']}">干皮 · 敏肌 · 换季干燥 · 40+熟龄肌</text>
  </g>
  
  <!-- 装饰 -->
  <rect x="900" y="150" width="200" height="400" fill="{COLORS['forest']}" opacity="0.05"/>
  <text x="1000" y="350" font-family="Noto Serif SC, serif" font-size="120" 
        fill="{COLORS['gold']}" opacity="0.1" text-anchor="middle">润</text>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">07</text>
</svg>'''
    return svg

def create_slide_8_product3():
    """产品3：人参"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['bg_cream']}"/>
  
  <!-- 章节标题 -->
  <text x="120" y="80" font-family="Noto Serif SC, serif" font-size="14" 
        fill="{COLORS['gold']}" letter-spacing="3">CHAPTER 03 · 产品 03</text>
  
  <!-- 产品名称 -->
  <text x="120" y="130" font-family="Noto Sans SC, sans-serif" font-size="32" 
        fill="{COLORS['forest']}" font-weight="300">人参焕活紧致身体精华油</text>
  
  <!-- 核心成分 -->
  <g transform="translate(120, 180)">
    <rect x="0" y="0" width="200" height="40" fill="{COLORS['forest']}" opacity="0.1"/>
    <text x="100" y="26" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['forest']}" text-anchor="middle">长白山有机人参</text>
  </g>
  
  <!-- 功效 -->
  <g transform="translate(120, 260)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">核心功效</text>
    <text x="0" y="40" font-family="Noto Sans SC, sans-serif" font-size="20" 
          fill="{COLORS['text_dark']}" letter-spacing="4">紧致抗老 · 淡化颈纹 · 提亮焕活</text>
  </g>
  
  <!-- 卖点 -->
  <g transform="translate(120, 360)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">核心优势</text>
    <text x="0" y="35" font-family="Noto Sans SC, sans-serif" font-size="18" 
          fill="{COLORS['text_dark']}">天然抗老标杆</text>
    <text x="0" y="65" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['text_gray']}">促进胶原新生，改善松弛、颈纹，40+熟龄肌专属</text>
  </g>
  
  <!-- 适配人群 -->
  <g transform="translate(120, 480)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="14" 
          fill="{COLORS['text_light']}">适配人群</text>
    <text x="0" y="28" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['text_gray']}">35+熟龄肌 · 身体松弛 · 颈纹 · 暗沉</text>
  </g>
  
  <!-- 装饰 -->
  <rect x="900" y="150" width="200" height="400" fill="{COLORS['forest']}" opacity="0.05"/>
  <text x="1000" y="350" font-family="Noto Serif SC, serif" font-size="120" 
        fill="{COLORS['gold']}" opacity="0.1" text-anchor="middle">参</text>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">08</text>
</svg>'''
    return svg

def create_slide_9_product4():
    """产品4：鸢尾花"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['bg_cream']}"/>
  
  <!-- 章节标题 -->
  <text x="120" y="80" font-family="Noto Serif SC, serif" font-size="14" 
        fill="{COLORS['gold']}" letter-spacing="3">CHAPTER 03 · 产品 04</text>
  
  <!-- 产品名称 -->
  <text x="120" y="130" font-family="Noto Sans SC, sans-serif" font-size="32" 
        fill="{COLORS['forest']}" font-weight="300">鸢尾花焕亮美白身体乳</text>
  
  <!-- 核心成分 -->
  <g transform="translate(120, 180)">
    <rect x="0" y="0" width="240" height="40" fill="{COLORS['forest']}" opacity="0.1"/>
    <text x="120" y="26" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['forest']}" text-anchor="middle">法国普罗旺斯有机鸢尾花</text>
  </g>
  
  <!-- 功效 -->
  <g transform="translate(120, 260)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">核心功效</text>
    <text x="0" y="40" font-family="Noto Sans SC, sans-serif" font-size="20" 
          fill="{COLORS['text_dark']}" letter-spacing="4">美白淡斑 · 改善色沉 · 水润保湿</text>
  </g>
  
  <!-- 卖点 -->
  <g transform="translate(120, 360)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">核心优势</text>
    <text x="0" y="35" font-family="Noto Sans SC, sans-serif" font-size="18" 
          fill="{COLORS['text_dark']}">「白+润」双重焕亮</text>
    <text x="0" y="65" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['text_gray']}">温和美白不拔干，改善色差，敏肌友好</text>
  </g>
  
  <!-- 适配人群 -->
  <g transform="translate(120, 480)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="14" 
          fill="{COLORS['text_light']}">适配人群</text>
    <text x="0" y="28" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['text_gray']}">美白需求 · 肤色不均 · 敏肌 · 干皮</text>
  </g>
  
  <!-- 装饰 -->
  <rect x="900" y="150" width="200" height="400" fill="{COLORS['forest']}" opacity="0.05"/>
  <text x="1000" y="350" font-family="Noto Serif SC, serif" font-size="120" 
        fill="{COLORS['gold']}" opacity="0.1" text-anchor="middle">白</text>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">09</text>
</svg>'''
    return svg

def create_slide_10_product5():
    """产品5：兰花"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{COLORS['bg_cream']}"/>
  
  <!-- 章节标题 -->
  <text x="120" y="80" font-family="Noto Serif SC, serif" font-size="14" 
        fill="{COLORS['gold']}" letter-spacing="3">CHAPTER 03 · 产品 05</text>
  
  <!-- 产品名称 -->
  <text x="120" y="130" font-family="Noto Sans SC, sans-serif" font-size="32" 
        fill="{COLORS['forest']}" font-weight="300">兰花修护淡纹身体油</text>
  
  <!-- 核心成分 -->
  <g transform="translate(120, 180)">
    <rect x="0" y="0" width="320" height="40" fill="{COLORS['forest']}" opacity="0.1"/>
    <text x="160" y="26" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['forest']}" text-anchor="middle">比利时进口有机兰花（娇兰同款产地）</text>
  </g>
  
  <!-- 功效 -->
  <g transform="translate(120, 260)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">核心功效</text>
    <text x="0" y="40" font-family="Noto Sans SC, sans-serif" font-size="20" 
          fill="{COLORS['text_dark']}" letter-spacing="4">修护淡纹 · 预防纹路 · 舒缓干痒</text>
  </g>
  
  <!-- 卖点 -->
  <g transform="translate(120, 360)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="16" 
          fill="{COLORS['gold']}">核心优势</text>
    <text x="0" y="35" font-family="Noto Sans SC, sans-serif" font-size="18" 
          fill="{COLORS['text_dark']}">预防 + 淡化双重作用</text>
    <text x="0" y="65" font-family="Noto Sans SC, sans-serif" font-size="14" 
          fill="{COLORS['text_gray']}">温和安全，孕妇可用，敏肌友好</text>
  </g>
  
  <!-- 适配人群 -->
  <g transform="translate(120, 480)">
    <text x="0" y="0" font-family="Noto Serif SC, serif" font-size="14" 
          fill="{COLORS['text_light']}">适配人群</text>
    <text x="0" y="28" font-family="Noto Sans SC, sans-serif" font-size="13" 
          fill="{COLORS['text_gray']}">孕期/产后女性 · 肥胖纹 · 敏肌、孕妇友好</text>
  </g>
  
  <!-- 装饰 -->
  <rect x="900" y="150" width="200" height="400" fill="{COLORS['forest']}" opacity="0.05"/>
  <text x="1000" y="350" font-family="Noto Serif SC, serif" font-size="120" 
        fill="{COLORS['gold']}" opacity="0.1" text-anchor="middle">兰</text>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">10</text>
</svg>'''
    return svg

def create_slide_11_end():
    """结尾页"""
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGradEnd" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{COLORS['bg_ivory']}"/>
      <stop offset="100%" style="stop-color:{COLORS['bg_cream']}"/>
    </linearGradient>
  </defs>
  
  <rect width="{WIDTH}" height="{HEIGHT}" fill="url(#bgGradEnd)"/>
  
  <!-- 装饰线 -->
  <line x1="300" y1="250" x2="500" y2="250" stroke="{COLORS['gold']}" stroke-width="0.5" opacity="0.5"/>
  <line x1="780" y1="250" x2="980" y2="250" stroke="{COLORS['gold']}" stroke-width="0.5" opacity="0.5"/>
  
  <!-- 主标题 -->
  <text x="{WIDTH/2}" y="320" font-family="Noto Serif SC, serif" font-size="32" 
        fill="{COLORS['forest']}" text-anchor="middle" font-weight="300" letter-spacing="4">
    从田间到瓶身
  </text>
  <text x="{WIDTH/2}" y="370" font-family="Noto Serif SC, serif" font-size="24" 
        fill="{COLORS['text_gray']}" text-anchor="middle" font-weight="300" letter-spacing="3">
    每一滴都是自然的馈赠
  </text>
  
  <!-- 分隔装饰 -->
  <circle cx="{WIDTH/2}" cy="430" r="3" fill="{COLORS['gold']}"/>
  <line x1="{WIDTH/2-60}" y1="430" x2="{WIDTH/2-10}" y2="430" stroke="{COLORS['gold']}" stroke-width="0.5"/>
  <line x1="{WIDTH/2+10}" y1="430" x2="{WIDTH/2+60}" y2="430" stroke="{COLORS['gold']}" stroke-width="0.5"/>
  
  <!-- 品牌标语 -->
  <text x="{WIDTH/2}" y="520" font-family="Noto Sans SC, sans-serif" font-size="20" 
        fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="8">
    植愈身心 · 原生奢养
  </text>
  
  <!-- 页码 -->
  <text x="{WIDTH-60}" y="{HEIGHT-40}" font-family="Noto Sans SC, sans-serif" font-size="12" 
        fill="{COLORS['text_light']}" text-anchor="end">11</text>
</svg>'''
    return svg

# 生成所有幻灯片
slides = [
    ("slide_01_cover.svg", create_slide_1_cover),
    ("slide_02_toc.svg", create_slide_2_toc),
    ("slide_03_concept.svg", create_slide_3_concept),
    ("slide_04_advantages.svg", create_slide_4_advantages),
    ("slide_05_matrix.svg", create_slide_5_matrix),
    ("slide_06_product1.svg", create_slide_6_product1),
    ("slide_07_product2.svg", create_slide_7_product2),
    ("slide_08_product3.svg", create_slide_8_product3),
    ("slide_09_product4.svg", create_slide_9_product4),
    ("slide_10_product5.svg", create_slide_10_product5),
    ("slide_11_end.svg", create_slide_11_end),
]

for filename, func in slides:
    filepath = os.path.join(PROJECT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(func())
    print(f"✓ 生成: {filename}")

print(f"\n✅ 共生成 {len(slides)} 页 PPT")
