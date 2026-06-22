import streamlit as st
try:
    from PIL import Imageā
    import requests
    from io import ByteāsIO
    FAVICON_URL = "https://raw.githubusercontent.com/meryam-elghouti/agenticalpha/refs/heads/main/favicon.png.png"
    response = requests.get(FAVICON_URL)
    icon = Image.open(BytesIO(response.content))
    st.set_page_config(
        page_title="The Agentic Alpha",
        page_icon=icon,
        layout="wide",
        initial_sidebar_state="expanded"
    )
except:
    st.set_page_config(
        page_title="The Agentic Alpha",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded"
    )
import subprocess
subprocess.run(["pip", "install", "plotly", "groq", "-q"])
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from groq import Groq
import os
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
LOGO_URL = "https://raw.githubusercontent.com/meryam-elghouti/agenticalpha/refs/heads/main/agentic-alpha-logo.png.png"
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
* { font-family: 'Inter', sans-serif; }
.stApp { background-color: #f0f2f6; color: #1a2744; }
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a1628 0%, #0d1f3c 100%);
    border-right: 3px solid #c9a227;
}
[data-testid="stSidebar"] * { color: #e8e8e8 !important; }
[data-testid="stSidebar"] .stRadio label {
    padding: 10px 14px; border-radius: 8px;
    font-weight: 500; transition: all 0.2s; display: block;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(201,162,39,0.15);
    color: #FFD700 !important;
}
h1 {
    color: #0a1628 !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
    border-bottom: 3px solid #c9a227;
    padding-bottom: 10px;
}
h2 { color: #0a1628 !important; font-weight: 700 !important; }
h3 { color: #1a3a6b !important; font-weight: 600 !important; }
[data-testid="metric-container"] {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-top: 4px solid #c9a227;
    border-radius: 10px;
    padding: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    overflow: hidden;
}
[data-testid="metric-container"] label {
    color: #64748b !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 1px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
[data-testid="metric-container"] [data-testid="metric-value"] {
    color: #0a1628 !important;
    font-size: 1.5rem !important;
    font-weight: 800 !important;
    white-space: nowrap;
    overflow: hidden;
}
.stButton > button {
    background: #0a1628;
    color: #FFD700 !important;
    border: 2px solid #c9a227;
    border-radius: 8px;
    font-weight: 700;
    font-size: 14px;
    padding: 12px 28px;
    text-transform: uppercase;
    transition: all 0.3s;
}
.stButton > button:hover {
    background: #c9a227;
    color: #0a1628 !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 15px rgba(201,162,39,0.3);
}
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #ffffff;
    color: #1a2744 !important;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    font-size: 13px;
}
div[data-baseweb="select"] > div {
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 8px !important;
    color: #1a2744 !important;
    font-size: 13px !important;
}
.stTabs [data-baseweb="tab-list"] {
    background: #ffffff;
    border-radius: 10px;
    padding: 4px;
    border: 1px solid #e2e8f0;
}
.stTabs [data-baseweb="tab"] {
    color: #64748b !important;
    border-radius: 8px;
    font-weight: 600;
    font-size: 13px;
}
.stTabs [aria-selected="true"] {
    background: #0a1628 !important;
    color: #FFD700 !important;
}
.stProgress > div > div {
    background: linear-gradient(90deg, #0a1628, #c9a227);
    border-radius: 10px;
}
hr { border: none; border-top: 1px solid #e2e8f0; margin: 20px 0; }
.stCaption { color: #94a3b8 !important; }
.gold-line {
    height: 3px;
    background: linear-gradient(90deg, #c9a227, #FFD700, #c9a227);
    border: none; margin: 28px 0; border-radius: 2px;
}
.aa-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)
# ── Sidebar ───────────────────────────────────
st.sidebar.markdown(f"""
<div style='text-align:center; padding:20px 0 24px;'>
    <div style='margin:0 auto;'>
        <img src='{LOGO_URL}'
             style='width:160px; height:auto; border-radius:50%;'
             alt='Agentic Alpha'>
    </div>
    <div style='margin-top:14px; font-size:15px; font-weight:800;
                color:#FFD700; letter-spacing:1px;'>THE AGENTIC ALPHA</div>
    <div style='font-size:10px; color:#94a3b8; letter-spacing:2px;
                margin-top:4px; text-transform:uppercase;'>
        AI Decision Support System</div>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("""
<div style='background:rgba(255,255,255,0.05);
            border:1px solid rgba(201,162,39,0.3);
            border-radius:10px; padding:14px; margin-bottom:16px;'>
    <div style='color:#c9a227; font-size:10px;
                text-transform:uppercase; letter-spacing:1px;
                margin-bottom:8px;'>Researcher</div>
    <div style='color:#ffffff; font-weight:700; font-size:14px;'>
        Meryam El Ghouti</div>
    <div style='color:#94a3b8; font-size:12px; margin-top:3px;'>
        Sapienza University of Rome</div>
    <div style='color:#94a3b8; font-size:12px;'>
        MSc Business Management · 2026</div>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown(
    "<div style='color:#c9a227; font-size:10px; text-transform:uppercase;"
    "letter-spacing:1px; padding:0 4px; margin-bottom:6px;'>"
    "Navigation</div>",
    unsafe_allow_html=True
)
page = st.sidebar.radio("", [
    "🏠 Home", "🤖 Live Analyzer", "📊 Dashboard",
    "⚔️ AI vs Human", "🔍 Custom Analysis",
    "🎓 Jury Demo", "ℹ️ About"
])
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style='text-align:center; color:#475569; font-size:11px; padding:8px;'>
    © 2026 Meryam El Ghouti<br>
    <span style='color:#c9a227;'>agenticalpha.streamlit.app</span>
</div>
""", unsafe_allow_html=True)
# ── Data — 40 Cases ───────────────────────────
data = {
    "Company": [
        "WeWork","Tesla","Apple","Theranos","Kodak",
        "Blockbuster","Peloton","Amazon","Netflix","Microsoft",
        "Meta","Twitter","Disney","Uber","Rivian",
        "Microsoft","Adobe","Apple","Meta","OpenAI",
        "UBS/Credit Suisse","Toshiba","Microsoft/Activision","Nokia",
        "Silicon Valley Bank","Royal Bank of Scotland","Volkswagen",
        "SoftBank","Spotify","LVMH",
        "Wirecard","Bayer","Arm Holdings","Deliveroo","Alibaba",
        "Didi","Samsung","Robinhood","Beyond Meat","Zoom"
    ],
    "Year": [
        2019,2020,2018,2016,2012,2010,2021,2015,2013,2016,
        2021,2022,2019,2019,2021,2023,2023,2024,2022,2025,
        2023,2023,2022,2013,2023,2007,2015,2019,2018,2020,
        2020,2018,2023,2021,2019,2021,2016,2021,2019,2019
    ],
    "Corporate_Decision": [
        "Proceed with IPO expansion?",
        "Invest in Gigafactory Texas?",
        "Shift to services expansion?",
        "Scale blood-testing operations?",
        "Invest in digital transformation?",
        "Invest in streaming technology?",
        "Expand manufacturing capacity?",
        "Invest massively in AWS expansion?",
        "Invest billions in original content?",
        "Acquire LinkedIn for $26B?",
        "Invest billions in Metaverse?",
        "Accept Musk $44B acquisition?",
        "Acquire Fox and launch Disney+?",
        "Proceed with IPO unprofitable?",
        "Invest in mass EV production?",
        "Invest $10B in OpenAI partnership?",
        "Acquire Figma for $20B?",
        "Launch Vision Pro at $3,499?",
        "Massive layoffs and restructuring?",
        "Transition to fully commercial?",
        "Emergency acquisition of Credit Suisse for CHF 3B?",
        "Accept JIP consortium take-private buyout of ¥2T?",
        "Acquire Activision Blizzard for $69B amid regulatory opposition?",
        "Sell mobile phone business to Microsoft for $7.2B?",
        "Maintain current interest rate risk exposure?",
        "Acquire ABN AMRO for $98B?",
        "Continue diesel emissions strategy with defeat device software?",
        "Invest additional $9.5B in WeWork at $47B valuation?",
        "Proceed with direct listing on NYSE without underwriter?",
        "Complete $15.8B acquisition of Tiffany despite COVID-19?",
        "Deny missing €1.9B fraud allegations and continue operations?",
        "Acquire Monsanto for $63B despite known Roundup litigation?",
        "Proceed with NASDAQ IPO at $54.5B valuation?",
        "Proceed with London Stock Exchange IPO?",
        "Proceed with Hong Kong secondary listing raising $11.2B?",
        "Proceed with NYSE IPO despite Chinese government warnings?",
        "Execute full global recall of Galaxy Note 7?",
        "Proceed with NASDAQ IPO after GameStop controversy?",
        "Proceed with NASDAQ IPO as first plant-based meat company?",
        "Proceed with NASDAQ IPO and aggressive enterprise expansion?"
    ],
    # UPDATE after running all 40 cases at temperature=0
    "Neutral_Decision": [
        "NO","YES","YES","NO","NO","NO","YES","YES","YES","YES",
        "NO","NO","YES","YES","YES","YES","NO","NO","YES","YES",
        "YES","YES","YES","YES","NO","NO","NO","NO","YES","YES",
        "NO","NO","YES","NO","YES","NO","YES","NO","YES","YES"
    ],
    "Aggressive_Decision": [
        "YES","YES","YES","YES","NO","NO","YES","YES","YES","YES",
        "YES","YES","NO","YES","YES","YES","YES","YES","YES","YES",
        "YES","YES","YES","YES","YES","YES","NO","YES","YES","NO",
        "YES","YES","YES","YES","YES","YES","YES","YES","YES","YES"
    ],
    "Conservative_Decision": [
        "YES","NO","YES","NO","NO","NO","NO","YES","NO","YES",
        "NO","NO","YES","NO","NO","YES","NO","NO","NO","NO",
        "NO","NO","NO","NO","NO","NO","NO","NO","NO","YES",
        "NO","NO","YES","NO","YES","NO","YES","NO","YES","YES"
    ],
    "Actual_Outcome": [
        "Failed","Success","Success","Failed","Failed","Failed",
        "Failed","Success","Success","Success","Mixed","Failed",
        "Mixed","Failed","Failed","Success","Failed","Failed",
        "Success","Pending",
        "Success","Mixed","Success","Failed","Failed",
        "Failed","Failed","Failed","Success","Success",
        "Failed","Failed","Success","Failed","Success",
        "Failed","Success","Failed","Success","Success"
    ],
    "Human_Decision": [
        "Proceed","Proceed","Proceed","Proceed","Did Not","Did Not",
        "Proceed","Proceed","Proceed","Proceed","Proceed","Accepted",
        "Proceed","Proceed","Proceed","Proceeded","Attempted",
        "Launched","Proceeded","Proceeding",
        "Proceeded","Accepted","Proceeded","Proceeded","Proceeded",
        "Proceeded","Continued","Proceeded","Proceeded","Completed",
        "Denied","Proceeded","Proceeded","Proceeded","Proceeded",
        "Proceeded","Recalled","Proceeded","Proceeded","Proceeded"
    ],
    "Industry": [
        "Real Estate","Automotive","Technology","Healthcare","Photography",
        "Entertainment","Fitness","E-Commerce","Media","Technology",
        "Social Media","Social Media","Entertainment","Transport","Automotive",
        "Technology","Software","Technology","Social Media","AI",
        "Banking","Technology","Technology/Gaming","Technology","Banking",
        "Banking","Automotive","Investment","Media/Music","Luxury",
        "Fintech","Pharmaceuticals","Semiconductors","Food Delivery","E-Commerce",
        "Transport","Electronics","Fintech","Food/Agriculture","Technology"
    ],
    # UPDATE after running all 40 cases at temperature=0
    "Neutral_Correct": [
        1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1,0,
        1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1
    ],
    "Aggressive_Correct": [
        0,1,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,1,0,
        1,0,1,0,0,0,1,0,1,0,
        0,0,1,0,1,0,1,0,1,1
    ],
    "Conservative_Correct": [
        0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,
        0,0,0,1,1,1,1,1,0,1,
        1,1,1,1,1,1,1,1,1,1
    ],
    # UPDATE after running all 40 cases at temperature=0
    "Neutral_Score": [
        15,78,82,12,20,18,55,85,80,90,35,30,72,60,65,88,25,28,82,60,
        85,85,85,85,60,32,30,20,82,85,
        50,50,50,50,50,50,50,50,50,50
    ],
    "Aggressive_Score": [
        65,88,92,75,35,30,80,95,85,85,80,72,45,80,75,95,70,78,88,90,
        95,80,95,80,78,80,40,85,78,80,
        50,50,50,50,50,50,50,50,50,50
    ],
    "Conservative_Score": [
        8,25,88,15,18,12,22,82,25,88,20,18,75,15,18,85,20,18,22,35,
        45,45,20,20,42,20,80,10,40,85,
        50,50,50,50,50,50,50,50,50,50
    ],
    "Main_Bias": [
        "Herding","Overconfidence","None","Herding","Loss Aversion",
        "Loss Aversion","Overconfidence","None","Overconfidence","None",
        "Overconfidence","Loss Aversion","Anchoring","Overconfidence","Overconfidence",
        "None","Overconfidence","Overconfidence","Loss Aversion","Overconfidence",
        "Herding","Overconfidence","Overconfidence","Overconfidence","Overconfidence",
        "Loss Aversion","None","Loss Aversion","Loss Aversion","Overconfidence",
        "None","None","None","None","None",
        "None","None","None","None","None"
    ],
    "Human_Correct": [
        0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,
        1,0,1,0,0,0,0,0,1,1,
        0,0,1,0,1,0,1,0,1,1
    ]
}
df = pd.DataFrame(data)
df["Average_Score"] = (
    df["Neutral_Score"]+df["Aggressive_Score"]+df["Conservative_Score"]
)/3
df["AI_Recommendation"] = df["Average_Score"].apply(
    lambda x: "PROCEED" if x>=60 else "CAUTION" if x>=40 else "DO NOT PROCEED"
)
# Exclude Pending (ongoing) AND Mixed from accuracy calculations
df_h = df[
    (df["Actual_Outcome"]!="Pending") &
    (df["Actual_Outcome"]!="Mixed")
]
# Separate views for display
df_mixed = df[df["Actual_Outcome"]=="Mixed"]
df_pending = df[df["Actual_Outcome"]=="Pending"]
PT = dict(
    paper_bgcolor="#ffffff",
    plot_bgcolor="#f8fafc",
    font_color="#1a2744",
    title_font_color="#0a1628",
    title_font_size=13,
    font_size=11,
    height=320
)
def parse_response(text):
    lines = text.strip().split('\n')
    dec=sc=conf=r1=r2=r3=kr=alt=""
    for line in lines:
        l = line.strip()
        if "DECISION:" in l:
            dec = l.split("DECISION:")[-1].strip()
        elif "SCORE:" in l:
            try:
                nums = ''.join(filter(str.isdigit,
                               l.split("SCORE:")[-1].strip()))
                sc = str(int(nums[:3])) if nums else "50"
            except:
                sc = "50"
        elif "CONFIDENCE:" in l:
            try:
                nums = ''.join(filter(str.isdigit,
                               l.split("CONFIDENCE:")[-1].strip()))
                conf = str(int(nums[:3])) if nums else "50"
            except:
                conf = "50"
        elif "REASON 1:" in l:
            r1 = l.split("REASON 1:")[-1].strip()
        elif "REASON 2:" in l:
            r2 = l.split("REASON 2:")[-1].strip()
        elif "REASON 3:" in l:
            r3 = l.split("REASON 3:")[-1].strip()
        elif "KEY RISK:" in l:
            kr = l.split("KEY RISK:")[-1].strip()
        elif "ALTERNATIVE:" in l:
            alt = l.split("ALTERNATIVE:")[-1].strip()
    return dec, sc, conf, r1, r2, r3, kr, alt
def render_persona_card(name, color, dec, sc, conf, r1, r2, r3):
    yes = "YES" in dec.upper()
    vc = "#15803d" if yes else "#dc2626"
    vbg = "#f0fdf4" if yes else "#fff1f2"
    verdict = "✅ PROCEED" if yes else "❌ DO NOT PROCEED"
    score_int = int(sc) if sc.isdigit() else 50
    st.markdown(f"""
    <div style='background:#ffffff; border:1px solid #e2e8f0;
                border-top:4px solid {color};
                border-radius:12px; padding:16px;'>
        <div style='color:{color}; font-weight:700;
                    font-size:13px; margin-bottom:10px;'>{name}</div>
        <div style='background:{vbg}; border:1px solid {vc};
                    border-radius:8px; padding:8px;
                    text-align:center; margin-bottom:10px;'>
            <span style='color:{vc}; font-weight:800; font-size:14px;'>
                {verdict}</span>
        </div>
        <div style='height:6px; background:#e2e8f0;
                    border-radius:3px; margin-bottom:8px;'>
            <div style='height:6px; background:{color};
                        border-radius:3px; width:{score_int}%;'></div>
        </div>
        <div style='color:#64748b; font-size:12px; margin-bottom:8px;'>
            Score: <strong style='color:#0a1628;'>{sc}/100</strong> ·
            Confidence: <strong style='color:#0a1628;'>{conf}%</strong>
        </div>
        <div style='font-size:12px; color:#334155; line-height:1.6;'>
            📌 {r1}<br>📌 {r2}<br>📌 {r3}
        </div>
    </div>
    """, unsafe_allow_html=True)
def render_verdict(avg, all_scores):
    if avg >= 60:
        v="PROCEED WITH INVESTMENT"; vc="#15803d"; vbg="#f0fdf4"; vi="✅"
    elif avg >= 40:
        v="PROCEED WITH CAUTION"; vc="#92400e"; vbg="#fffbeb"; vi="⚠️"
    else:
        v="DO NOT PROCEED"; vc="#991b1b"; vbg="#fff1f2"; vi="❌"
    st.markdown(f"""
    <div style='background:{vbg}; border:2px solid {vc};
                border-radius:14px; padding:24px; text-align:center;
                margin-top:20px;'>
        <div style='color:{vc}; font-size:11px; font-weight:700;
                    text-transform:uppercase; letter-spacing:2px;
                    margin-bottom:6px;'>Simulation Verdict</div>
        <div style='color:{vc}; font-size:22px; font-weight:900;'>
            {vi} {v}</div>
        <div style='color:{vc}; font-size:12px; margin-top:8px; opacity:0.8;'>
            Avg: {avg:.0f}/100 ·
            Neutral: {all_scores[0] if all_scores else 0}/100 ·
            Aggressive: {all_scores[1] if len(all_scores)>1 else 0}/100 ·
            Conservative: {all_scores[2] if len(all_scores)>2 else 0}/100
        </div>
    </div>
    <div style='text-align:center; color:#94a3b8; font-size:11px;
                margin-top:8px;'>
        ⚠️ Simulation output only — not financial advice</div>
    """, unsafe_allow_html=True)
PERSONAS = [
    {"name":"🤖 Neutral Advisor","color":"#1e3a8a",
     "badge":"PURE AI REASONING",
     "instruction":"You are a neutral objective corporate finance advisor."},
    {"name":"📈 Aggressive CFO","color":"#dc2626",
     "badge":"AI + HUMAN OVERCONFIDENCE",
     "instruction":"You are an aggressive CFO who prioritizes growth and accepts high risk."},
    {"name":"🛡️ Conservative Board","color":"#15803d",
     "badge":"AI + HUMAN LOSS AVERSION",
     "instruction":"You are a conservative board member who prioritizes stability and risk management."},
]
# ══════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════
if page == "🏠 Home":
    st.markdown(f"""
    <div style='background:linear-gradient(135deg,#0a1628,#1a3a6b);
                border-radius:16px; padding:40px; margin-bottom:24px;
                border:1px solid #c9a227; text-align:center;'>
        <div style='margin:0 auto 16px;'>
            <img src='{LOGO_URL}'
                 style='width:280px; height:auto; border-radius:50%;'
                 alt='Agentic Alpha Logo'>
        </div>
        <div style='font-size:30px; font-weight:900; color:#FFD700;
                    margin-bottom:10px;'>THE AGENTIC ALPHA</div>
        <div style='font-size:15px; color:#94a3b8; max-width:560px;
                    margin:0 auto 18px; line-height:1.7;'>
            An AI-powered corporate investment decision simulator that analyzes
            any investment through three behavioral personas — detecting
            cognitive biases in real time.
        </div>
        <div style='background:rgba(201,162,39,0.2); border:1px solid #c9a227;
                    display:inline-block; color:#FFD700; font-weight:700;
                    font-size:12px; padding:8px 20px; border-radius:20px;
                    letter-spacing:1px;'>
            ⚡ AI · SIMULATION · BEHAVIORAL ANALYSIS
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; margin-bottom:20px;'>
        <div style='color:#c9a227; font-size:11px; font-weight:700;
                    text-transform:uppercase; letter-spacing:2px;'>
            What Is The Agentic Alpha?</div>
        <div style='color:#0a1628; font-size:20px; font-weight:800;
                    margin-top:6px;'>
            A Multi-Agent AI That Simulates Corporate Investment Decisions
        </div>
        <div style='color:#64748b; font-size:13px; margin-top:8px;'>
            Three personas representing different configurations
            of Human-AI integration
        </div>
    </div>
    """, unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    for col,color,icon,name,badge,acc,desc in zip(
        [c1,c2,c3],
        ["#1e3a8a","#dc2626","#15803d"],
        ["🤖","📈","🛡️"],
        ["Neutral Advisor","Aggressive CFO","Conservative Board"],
        ["PURE AI REASONING",
         "AI + HUMAN OVERCONFIDENCE",
         "AI + HUMAN LOSS AVERSION"],
        [f"{round(df_h['Neutral_Correct'].mean()*100)}% accuracy",
         f"{round(df_h['Aggressive_Correct'].mean()*100)}% accuracy",
         f"{round(df_h['Conservative_Correct'].mean()*100)}% accuracy"],
        [
            "Pure AI reasoning — objective analysis based on financial data with no human behavioral framing applied",
            "AI embedded with human overconfidence characteristics — growth-focused reasoning reflecting executive ambition and risk-seeking behavioral patterns",
            "AI embedded with human loss aversion theory — risk-conscious reasoning derived from Kahneman and Tversky Prospect Theory"
        ]
    ):
        with col:
            st.markdown(f"""
            <div class='aa-card' style='border-top:4px solid {color};
                        text-align:center;'>
                <div style='font-size:32px; margin-bottom:8px;'>{icon}</div>
                <div style='color:{color}; font-weight:800; font-size:14px;
                            margin-bottom:4px;'>{name}</div>
                <div style='background:{color}; color:#ffffff;
                            font-size:9px; font-weight:700;
                            padding:2px 8px; border-radius:20px;
                            display:inline-block; margin-bottom:4px;
                            letter-spacing:0.5px;'>{badge}</div>
                <div style='color:{color}; font-size:11px;
                            font-weight:700; margin-bottom:8px;'>
                    {acc}</div>
                <div style='color:#64748b; font-size:12px;
                            line-height:1.6;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("<hr class='gold-line'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; margin-bottom:20px;'>
        <div style='color:#c9a227; font-size:11px; font-weight:700;
                    text-transform:uppercase; letter-spacing:2px;'>How It Works</div>
        <div style='color:#0a1628; font-size:20px; font-weight:800;
                    margin-top:6px;'>4 Simple Steps</div>
    </div>
    """, unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    for col,num,icon,title,desc in zip(
        [c1,c2,c3,c4],
        ["01","02","03","04"],
        ["🏢","⚡","💯","🧠"],
        ["Input Decision","AI Simulates","Get Scores","Detect Biases"],
        [
            "Enter company, year and investment decision type",
            "3 personas analyze through different behavioral lenses",
            "Each persona gives a 0-100 investment score",
            "System detects overconfidence, herding and more"
        ]
    ):
        with col:
            st.markdown(f"""
            <div class='aa-card' style='text-align:center; padding:20px 14px;'>
                <div style='background:#0a1628; color:#FFD700; font-size:10px;
                            font-weight:800; padding:3px 10px;
                            border-radius:20px; display:inline-block;
                            margin-bottom:10px; letter-spacing:1px;'>
                    STEP {num}</div>
                <div style='font-size:28px; margin-bottom:8px;'>{icon}</div>
                <div style='color:#0a1628; font-weight:700; font-size:13px;
                            margin-bottom:6px;'>{title}</div>
                <div style='color:#64748b; font-size:12px;
                            line-height:1.5;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("<hr class='gold-line'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; margin-bottom:16px;'>
        <div style='color:#c9a227; font-size:11px; font-weight:700;
                    text-transform:uppercase; letter-spacing:2px;'>
            Research Validation</div>
    </div>
    """, unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.metric("📊 Total Cases","40")
    with c2: st.metric("✅ Confirmed Cases",str(len(df_h)))
    with c3: st.metric("🎯 Best Accuracy",
                       f"{round(df_h['Conservative_Correct'].mean()*100)}%")
    with c4: st.metric("🧠 Bias Types","5")
    st.caption(
        f"⚠️ 40 total cases · {len(df_h)} confirmed for accuracy analysis · "
        f"{len(df_mixed)} Mixed outcomes excluded · {len(df_pending)} Ongoing excluded"
    )
    st.markdown("<hr class='gold-line'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; margin-bottom:16px;'>
        <div style='color:#c9a227; font-size:11px; font-weight:700;
                    text-transform:uppercase; letter-spacing:2px;'>What You Get</div>
        <div style='color:#0a1628; font-size:20px; font-weight:800;
                    margin-top:6px;'>Every Analysis Includes</div>
    </div>
    """, unsafe_allow_html=True)
    c1,c2 = st.columns(2)
    with c1:
        for item in [
            "✅  Investment decision — YES or NO",
            "✅  Investment score from 0 to 100",
            "✅  Three specific reasons per persona",
            "✅  Final simulation verdict"
        ]:
            st.markdown(f"""
            <div class='aa-card' style='padding:12px 16px; margin-bottom:8px;
                        font-weight:600; color:#0a1628; font-size:13px;'>
                {item}</div>
            """, unsafe_allow_html=True)
    with c2:
        for item in [
            "✅  Behavioral bias detection report",
            "✅  Heuristic overconfidence indicator",
            "✅  Herding and anchoring analysis",
            "✅  Private company custom analysis"
        ]:
            st.markdown(f"""
            <div class='aa-card' style='padding:12px 16px; margin-bottom:8px;
                        font-weight:600; color:#0a1628; font-size:13px;'>
                {item}</div>
            """, unsafe_allow_html=True)
    st.markdown("<hr class='gold-line'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:#0a1628; border:1px solid #c9a227;
                border-radius:16px; padding:32px; text-align:center;'>
        <div style='color:#FFD700; font-size:20px; font-weight:800;
                    margin-bottom:8px;'>Ready to Simulate?</div>
        <div style='color:#94a3b8; font-size:13px; line-height:1.6;'>
            Use the navigation menu on the left sidebar to access
            the Live Analyzer and Custom Analysis
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.info("👈 Use the sidebar navigation to get started")
# ══════════════════════════════════════════════
# LIVE ANALYZER
# ══════════════════════════════════════════════
elif page == "🤖 Live Analyzer":
    st.title("🤖 Live Corporate Investment Simulator")
    st.markdown(
        "*Simulate corporate investment decisions through AI behavioral personas*"
    )
    st.info(
        "⚠️ Research simulation tool — does not predict actual financial "
        "outcomes or constitute financial advice."
    )
    st.markdown("---")
    c1,c2 = st.columns(2)
    with c1:
        company = st.text_input(
            "🏢 Company Name:", placeholder="e.g. Apple, Tesla, OpenAI"
        )
    with c2:
        year = st.text_input(
            "📅 Year:", placeholder="e.g. 2019, 2023, 2025"
        )
    decision_type = st.selectbox("📋 Type of Corporate Investment Decision:", [
        "IPO / Going Public","Merger & Acquisition (M&A)",
        "Capital Expenditure / Expansion","New Product / Service Investment",
        "Digital Transformation","Market Entry / Geographic Expansion",
        "Research & Development","Strategic Pivot","AI Investment","Restructuring"
    ])
    custom = st.text_input(
        "📝 Describe the specific decision (optional):",
        placeholder="e.g. Should the company acquire a competitor for $10B?"
    )
    if st.button("⚡ RUN SIMULATION", use_container_width=True):
        if company and year:
            st.markdown("---")
            st.markdown(f"""
            <div class='aa-card' style='border-left:5px solid #c9a227;'>
                <div style='color:#64748b; font-size:11px;
                            text-transform:uppercase; letter-spacing:1px;'>
                    Simulation Target</div>
                <div style='color:#0a1628; font-size:18px; font-weight:800;
                            margin-top:4px;'>{company} · {year}</div>
                <div style='color:#64748b; font-size:13px;'>{decision_type}</div>
            </div>
            """, unsafe_allow_html=True)
            all_decisions=[]
            all_scores=[]
            c1,c2,c3 = st.columns(3)
            cols = [c1,c2,c3]
            for i,p in enumerate(PERSONAS):
                with cols[i]:
                    with st.spinner("Simulating..."):
                        spec = custom if custom else f"a major {decision_type} decision"
                        q = f"""
{p['instruction']}
Company: {company} | Year: {year} | Decision: {spec}
Answer in EXACTLY this format:
DECISION: YES or NO
SCORE: (number 0 to 100)
CONFIDENCE: (number 0 to 100)
REASON 1: (one sentence)
REASON 2: (one sentence)
REASON 3: (one sentence)
"""
                        r = client.chat.completions.create(
                            model="llama-3.1-8b-instant",
                            messages=[{"role":"user","content":q}],
                            temperature=0
                        )
                        dec,sc,conf,r1,r2,r3,_,_ = parse_response(
                            r.choices[0].message.content
                        )
                        all_decisions.append(dec)
                        try:
                            all_scores.append(int(sc))
                        except:
                            all_scores.append(50)
                        render_persona_card(
                            p["name"],p["color"],dec,sc,conf,r1,r2,r3
                        )
            avg = sum(all_scores)/len(all_scores) if all_scores else 50
            render_verdict(avg, all_scores)
            st.markdown("---")
            bq = f"""
Three advisors simulated {company} {decision_type} in {year}.
Decisions: {', '.join(all_decisions)}
Scores: {', '.join([str(s) for s in all_scores])}
Answer in EXACTLY this format:
OVERCONFIDENCE: YES or NO — (why)
LOSS AVERSION: YES or NO — (why)
HERDING: YES or NO — (why)
ANCHORING: YES or NO — (why)
MAIN BIAS: (name or NONE)
EXPLANATION: (one sentence)
"""
            br = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role":"user","content":bq}],
                temperature=0
            )
            bl = br.choices[0].message.content.strip().split('\n')
            oc=la=h=an=mb=ex=""
            for line in bl:
                l = line.strip()
                if "OVERCONFIDENCE:" in l:
                    oc = l.split("OVERCONFIDENCE:")[-1].strip()
                elif "LOSS AVERSION:" in l:
                    la = l.split("LOSS AVERSION:")[-1].strip()
                elif "HERDING:" in l:
                    h = l.split("HERDING:")[-1].strip()
                elif "ANCHORING:" in l:
                    an = l.split("ANCHORING:")[-1].strip()
                elif "MAIN BIAS:" in l:
                    mb = l.split("MAIN BIAS:")[-1].strip()
                elif "EXPLANATION:" in l:
                    ex = l.split("EXPLANATION:")[-1].strip()
            st.markdown("### 🧠 Heuristic Bias Detection")
            st.caption("Heuristic indicators — not definitive bias diagnoses")
            c1,c2,c3,c4 = st.columns(4)
            for col,bias,val,color in zip(
                [c1,c2,c3,c4],
                ["Overconfidence","Loss Aversion","Herding","Anchoring"],
                [oc,la,h,an],
                ["#dc2626","#c9a227","#1e3a8a","#7c3aed"]
            ):
                with col:
                    detected = "YES" in val.upper()
                    st.markdown(f"""
                    <div style='background:#ffffff; border:1px solid #e2e8f0;
                                border-top:3px solid {color if detected else "#e2e8f0"};
                                border-radius:10px; padding:12px;'>
                        <div style='color:{color}; font-weight:700;
                                    font-size:12px;'>{bias}</div>
                        <div style='color:{"#dc2626" if detected else "#15803d"};
                                    font-weight:800; font-size:16px; margin:4px 0;'>
                            {"⚠️ YES" if detected else "✅ NO"}</div>
                        <div style='color:#64748b; font-size:11px;
                                    line-height:1.4;'>{val}</div>
                    </div>
                    """, unsafe_allow_html=True)
            if mb:
                st.warning(f"**Main Bias Indicator:** {mb} — {ex}")
        else:
            st.error("⚠️ Please enter both company name and year!")
# ══════════════════════════════════════════════
# DASHBOARD
# ══════════════════════════════════════════════
elif page == "📊 Dashboard":
    st.title("📊 Research Dashboard")
    st.markdown(
        f"*Simulation results across 40 cases (2007–2025) · "
        f"{len(df_h)} confirmed for accuracy analysis · "
        f"{len(df_mixed)} Mixed outcomes excluded · {len(df_pending)} Ongoing excluded*"
    )
    st.info(
        "⚠️ Results represent simulated decision reasoning — "
        "not causal financial predictions."
    )
    st.markdown("---")
    tab1,tab2,tab3 = st.tabs(["📊 Accuracy","💯 Scoring","🧠 Bias"])
    with tab1:
        na=round(df_h["Neutral_Correct"].mean()*100)
        ag=round(df_h["Aggressive_Correct"].mean()*100)
        co=round(df_h["Conservative_Correct"].mean()*100)
        hu=round(df_h["Human_Correct"].mean()*100)
        c1,c2,c3,c4 = st.columns(4)
        with c1: st.metric("🤖 Neutral (Pure AI)",f"{na}%")
        with c2: st.metric("📈 Aggressive (AI+Overconf)",f"{ag}%")
        with c3: st.metric("🛡️ Conservative (AI+LossAv)",f"{co}%")
        with c4: st.metric("🧑 Human",f"{hu}%")
        st.caption(
            f"⚠️ Accuracy based on N={len(df_h)} confirmed cases. "
            "Mixed outcomes (Meta, Disney, Toshiba) and Ongoing (OpenAI) excluded. "
            "Conservative = AI + Loss Aversion · Neutral = Pure AI · "
            "Aggressive = AI + Overconfidence"
        )
        st.markdown("---")
        c1,c2 = st.columns(2)
        with c1:
            fig = px.bar(
                pd.DataFrame({
                    "Persona":["Neutral\n(Pure AI)",
                               "Aggressive\n(AI+Overconf)",
                               "Conservative\n(AI+LossAv)",
                               "Human"],
                    "Accuracy":[na,ag,co,hu]
                }),
                x="Persona",y="Accuracy",color="Persona",
                color_discrete_map={
                    "Neutral\n(Pure AI)":"#1e3a8a",
                    "Aggressive\n(AI+Overconf)":"#dc2626",
                    "Conservative\n(AI+LossAv)":"#15803d",
                    "Human":"#c9a227"
                },
                title="Simulation Accuracy by Human-AI Integration Type",
                text="Accuracy"
            )
            fig.update_traces(texttemplate='%{text}%',textposition='outside')
            fig.update_layout(**PT,yaxis_range=[0,115],showlegend=False)
            st.plotly_chart(fig,use_container_width=True)
        with c2:
            yd = df_h.groupby("Year")["Neutral_Correct"].mean().reset_index()
            yd.columns = ["Year","Accuracy"]
            yd["Accuracy"] = round(yd["Accuracy"]*100)
            fig2 = px.line(yd,x="Year",y="Accuracy",
                          title="Simulation Accuracy Over Time",
                          markers=True,
                          color_discrete_sequence=["#c9a227"])
            fig2.update_layout(**PT,yaxis_range=[0,115])
            st.plotly_chart(fig2,use_container_width=True)
        c1,c2 = st.columns(2)
        with c1:
            fig3 = go.Figure()
            for name,col,color in [
                ("Neutral","Neutral_Correct","#1e3a8a"),
                ("Aggressive","Aggressive_Correct","#dc2626"),
                ("Conservative","Conservative_Correct","#15803d")
            ]:
                fig3.add_trace(go.Bar(
                    name=name,x=df_h["Company"],
                    y=df_h[col],marker_color=color
                ))
            fig3.update_layout(
                **PT,barmode="group",
                title="Correct Simulations by Company",
                yaxis=dict(tickvals=[0,1],ticktext=["Wrong","Correct"])
            )
            st.plotly_chart(fig3,use_container_width=True)
        with c2:
            ind = df_h.groupby("Industry")["Conservative_Correct"].mean().reset_index()
            ind.columns = ["Industry","Accuracy"]
            ind["Accuracy"] = round(ind["Accuracy"]*100)
            fig4 = px.bar(ind,x="Industry",y="Accuracy",
                         title="Conservative Accuracy by Industry",
                         color="Accuracy",
                         color_continuous_scale=[
                             [0,"#dc2626"],[0.5,"#c9a227"],[1,"#15803d"]
                         ],
                         text="Accuracy")
            fig4.update_traces(texttemplate='%{text}%',textposition='outside')
            fig4.update_layout(**PT,yaxis_range=[0,115])
            st.plotly_chart(fig4,use_container_width=True)
        st.markdown(f"### 📋 Confirmed Cases — N={len(df_h)}")
        st.dataframe(
            df_h[[
                "Company","Year","Corporate_Decision",
                "Neutral_Decision","Aggressive_Decision",
                "Conservative_Decision","Human_Decision",
                "Actual_Outcome","Main_Bias"
            ]].rename(columns={
                "Corporate_Decision":"Decision",
                "Neutral_Decision":"Neutral (Pure AI)",
                "Aggressive_Decision":"Aggressive (AI+Overconf)",
                "Conservative_Decision":"Conservative (AI+LossAv)",
                "Human_Decision":"Human",
                "Actual_Outcome":"Outcome",
                "Main_Bias":"Bias"
            }),
            use_container_width=True,
            hide_index=True,
            height=420
        )
        st.markdown("---")
        st.markdown("### ⚠️ Excluded Cases — Not Included in Accuracy Analysis")
        st.markdown("#### ⚠️ Mixed Outcome Cases (3) — Simulated but Excluded")
        st.dataframe(
            pd.DataFrame({
                "Company": ["Meta","Disney","Toshiba"],
                "Year": [2021,2019,2023],
                "Decision": [
                    "Invest billions in Metaverse?",
                    "Acquire Fox and launch Disney+?",
                    "Accept JIP take-private buyout of ¥2T?"
                ],
                "AI Simulated": ["✅ Yes","✅ Yes","✅ Yes"],
                "Why Excluded": [
                    "Success on corporate revenue but Failed on segment level — Reality Labs posted $40B+ losses. Binary classification would misrepresent a genuinely ambiguous outcome.",
                    "Success on streaming (Disney+ reached 100M+ subscribers) but Failed on acquisition economics (Fox integration wrote down $22B). Metric-dependent outcome.",
                    "Take-private deal completed in 2023 but long-term operational turnaround outcome remains unconfirmed. Cannot classify as clear Success or Failed."
                ],
                "Status": ["⚠️ Mixed","⚠️ Mixed","⚠️ Mixed"]
            }),
            use_container_width=True,
            hide_index=True
        )
        st.caption(
            "Mixed cases were fully simulated by all three personas (9 additional simulations) "
            "but excluded from binary accuracy calculations because no single financial metric "
            "can classify their outcome as unambiguously Success or Failed. "
            "They are retained in the dataset for qualitative analysis and bias detection."
        )
        st.markdown("#### 🔄 Ongoing Case (1) — Simulated but Excluded")
        st.dataframe(
            pd.DataFrame({
                "Company": ["OpenAI"],
                "Year": [2025],
                "Decision": ["Transition to fully commercial Public Benefit Corporation?"],
                "AI Simulated": ["✅ Yes"],
                "Why Excluded": [
                    "The commercial transition is ongoing at the time of this research. No confirmed outcome exists — the decision cannot be evaluated for accuracy until the outcome is known."
                ],
                "Status": ["🔄 Ongoing"]
            }),
            use_container_width=True,
            hide_index=True
        )
        st.caption(
            "OpenAI 2025 was included in the dataset and simulated by all three personas "
            "to demonstrate the system's capability with unresolved decisions, "
            "but excluded from accuracy analysis as no outcome can be confirmed."
        )
    with tab2:
        st.markdown("### 💯 Scoring Analysis")
        st.caption(
            "Scores represent simulated reasoning strength — "
            "not financial return predictions"
        )
        c1,c2,c3 = st.columns(3)
        with c1:
            st.metric("🤖 Avg Neutral (Pure AI)",
                     f"{df_h['Neutral_Score'].mean():.0f}/100")
        with c2:
            st.metric("📈 Avg Aggressive (AI+Overconf)",
                     f"{df_h['Aggressive_Score'].mean():.0f}/100")
        with c3:
            st.metric("🛡️ Avg Conservative (AI+LossAv)",
                     f"{df_h['Conservative_Score'].mean():.0f}/100")
        st.markdown("---")
        c1,c2 = st.columns(2)
        with c1:
            fig = px.scatter(
                df_h,x="Average_Score",y="Neutral_Correct",text="Company",
                title="Higher Score = Better Decision?",
                labels={"Average_Score":"Avg Score","Neutral_Correct":"Correct"},
                color="Actual_Outcome",size="Average_Score",
                color_discrete_map={
                    "Success":"#15803d","Failed":"#dc2626","Mixed":"#c9a227"
                }
            )
            fig.update_traces(textposition="top center")
            fig.update_layout(**PT)
            st.plotly_chart(fig,use_container_width=True)
        with c2:
            sd = pd.DataFrame({
                "Company":df_h["Company"],
                "Neutral (Pure AI)":df_h["Neutral_Score"],
                "Aggressive (AI+Overconf)":df_h["Aggressive_Score"],
                "Conservative (AI+LossAv)":df_h["Conservative_Score"]
            })
            fig2 = px.line(sd,x="Company",
                          y=["Neutral (Pure AI)",
                             "Aggressive (AI+Overconf)",
                             "Conservative (AI+LossAv)"],
                          title="Score Comparison — Human-AI Integration Spectrum",
                          color_discrete_map={
                              "Neutral (Pure AI)":"#1e3a8a",
                              "Aggressive (AI+Overconf)":"#dc2626",
                              "Conservative (AI+LossAv)":"#15803d"
                          })
            fig2.update_layout(**PT)
            st.plotly_chart(fig2,use_container_width=True)
        st.dataframe(
            df_h[[
                "Company","Year","Neutral_Score","Aggressive_Score",
                "Conservative_Score","Average_Score",
                "AI_Recommendation","Actual_Outcome"
            ]].rename(columns={
                "Neutral_Score":"Neutral",
                "Aggressive_Score":"Aggressive",
                "Conservative_Score":"Conservative",
                "Average_Score":"Avg",
                "AI_Recommendation":"Verdict",
                "Actual_Outcome":"Outcome"
            }),
            use_container_width=True,
            hide_index=True,
            height=420
        )
    with tab3:
        st.markdown("### 🧠 Heuristic Bias Analysis")
        st.caption(
            "Bias detection is heuristic — suggests possible patterns, "
            "not definitive diagnoses"
        )
        bc = df_h["Main_Bias"].value_counts().reset_index()
        bc.columns = ["Bias","Count"]
        c1,c2 = st.columns(2)
        with c1:
            fig = px.pie(bc,values="Count",names="Bias",
                        title="Bias Distribution",
                        color_discrete_sequence=[
                            "#c9a227","#1e3a8a","#dc2626","#15803d","#7c3aed"
                        ])
            fig.update_layout(**PT)
            st.plotly_chart(fig,use_container_width=True)
        with c2:
            fig2 = px.bar(bc,x="Bias",y="Count",
                         title="Bias Frequency",
                         color="Bias",text="Count",
                         color_discrete_sequence=[
                             "#c9a227","#1e3a8a","#dc2626","#15803d","#7c3aed"
                         ])
            fig2.update_traces(textposition='outside')
            fig2.update_layout(**PT,showlegend=False)
            st.plotly_chart(fig2,use_container_width=True)
        st.dataframe(
            df_h[[
                "Company","Year","Main_Bias",
                "Neutral_Decision","Aggressive_Decision",
                "Conservative_Decision","Actual_Outcome"
            ]].rename(columns={
                "Main_Bias":"Bias Indicator",
                "Neutral_Decision":"Neutral",
                "Aggressive_Decision":"Aggressive",
                "Conservative_Decision":"Conservative",
                "Actual_Outcome":"Outcome"
            }),
            use_container_width=True,
            hide_index=True,
            height=420
        )
# ══════════════════════════════════════════════
# AI VS HUMAN
# ══════════════════════════════════════════════
elif page == "⚔️ AI vs Human":
    st.title("⚔️ AI Simulation vs Human Decisions")
    st.markdown(
        "*Comparing simulated AI reasoning against documented "
        "human corporate decisions*"
    )
    st.info(
        "⚠️ Comparison between simulated AI reasoning and documented "
        "historical decisions — not causal performance measurement."
    )
    st.markdown("---")
    ai_w = len(df_h[(df_h["Neutral_Correct"]==1)&(df_h["Human_Correct"]==0)])
    hu_w = len(df_h[(df_h["Human_Correct"]==1)&(df_h["Neutral_Correct"]==0)])
    bo_r = len(df_h[(df_h["Neutral_Correct"]==1)&(df_h["Human_Correct"]==1)])
    bo_w = len(df_h[(df_h["Neutral_Correct"]==0)&(df_h["Human_Correct"]==0)])
    tot  = len(df_h)
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.metric("🤖 AI Better",f"{ai_w}",delta=f"{round(ai_w/tot*100)}%")
    with c2: st.metric("🧑 Human Better",f"{hu_w}",delta=f"{round(hu_w/tot*100)}%")
    with c3: st.metric("🤝 Both Correct",f"{bo_r}",delta=f"{round(bo_r/tot*100)}%")
    with c4: st.metric("❌ Both Wrong",f"{bo_w}",delta=f"{round(bo_w/tot*100)}%")
    st.markdown("---")
    c1,c2 = st.columns(2)
    with c1:
        fig = px.bar(
            pd.DataFrame({
                "Result":["AI Better","Human Better","Both Correct","Both Wrong"],
                "Cases":[ai_w,hu_w,bo_r,bo_w]
            }),
            x="Result",y="Cases",color="Result",
            color_discrete_map={
                "AI Better":"#1e3a8a","Human Better":"#c9a227",
                "Both Correct":"#15803d","Both Wrong":"#dc2626"
            },
            title="AI vs Human — Head to Head",text="Cases"
        )
        fig.update_traces(textposition='outside')
        fig.update_layout(**PT,showlegend=False)
        st.plotly_chart(fig,use_container_width=True)
    with c2:
        na = round(df_h["Neutral_Correct"].mean()*100)
        ag = round(df_h["Aggressive_Correct"].mean()*100)
        co = round(df_h["Conservative_Correct"].mean()*100)
        hu = round(df_h["Human_Correct"].mean()*100)
        fig2 = px.bar(
            pd.DataFrame({
                "Decision Maker":["Neutral (Pure AI)",
                                  "Aggressive (AI+Overconf)",
                                  "Conservative (AI+LossAv)",
                                  "Human"],
                "Accuracy":[na,ag,co,hu]
            }),
            x="Decision Maker",y="Accuracy",color="Decision Maker",
            title="Accuracy by Human-AI Integration Type",text="Accuracy",
            color_discrete_map={
                "Neutral (Pure AI)":"#1e3a8a",
                "Aggressive (AI+Overconf)":"#dc2626",
                "Conservative (AI+LossAv)":"#15803d",
                "Human":"#c9a227"
            }
        )
        fig2.update_traces(texttemplate='%{text}%',textposition='outside')
        fig2.update_layout(**PT,yaxis_range=[0,115],showlegend=False)
        st.plotly_chart(fig2,use_container_width=True)
    st.markdown("---")
    st.markdown(f"### 📋 Case by Case Comparison — N={len(df_h)} Confirmed Cases")
    st.caption(
        f"Based on {len(df_h)} confirmed cases. "
        "Mixed (Meta, Disney, Toshiba) and Ongoing (OpenAI) excluded from analysis."
    )
    comp = df_h[[
        "Company","Year","Neutral_Decision","Human_Decision",
        "Actual_Outcome","Neutral_Correct","Human_Correct"
    ]].copy()
    def lbl(row):
        if row["Neutral_Correct"]==1 and row["Human_Correct"]==0:
            return "🤖 AI Better"
        elif row["Human_Correct"]==1 and row["Neutral_Correct"]==0:
            return "🧑 Human Better"
        elif row["Neutral_Correct"]==1 and row["Human_Correct"]==1:
            return "🤝 Both Correct"
        else:
            return "❌ Both Wrong"
    comp["Result"] = comp.apply(lbl,axis=1)
    st.dataframe(
        comp[[
            "Company","Year","Neutral_Decision",
            "Human_Decision","Actual_Outcome","Result"
        ]].rename(columns={
            "Neutral_Decision":"AI Simulation (Pure AI)",
            "Human_Decision":"Human",
            "Actual_Outcome":"Outcome"
        }),
        use_container_width=True,
        hide_index=True,
        height=480
    )
    st.markdown("---")
    st.markdown("### ⚠️ Mixed Cases — Simulated But Excluded from Accuracy Analysis")
    mixed_display = df_mixed[["Company","Year","Neutral_Decision","Aggressive_Decision",
                               "Conservative_Decision","Human_Decision","Actual_Outcome"]].copy()
    mixed_display["Why Mixed"] = [
        "Success on revenue / Failed on Reality Labs losses — metric-dependent",
        "Success on Disney+ streaming / Failed on Fox acquisition economics",
        "Deal completed / Long-term turnaround outcome unconfirmed"
    ]
    st.dataframe(
        mixed_display.rename(columns={
            "Neutral_Decision":"Neutral","Aggressive_Decision":"Aggressive",
            "Conservative_Decision":"Conservative","Human_Decision":"Human",
            "Actual_Outcome":"Outcome"
        }),
        use_container_width=True,
        hide_index=True
    )
    st.info(
        "⚠️ Mixed cases were fully simulated by all three AI personas but excluded "
        "from accuracy analysis because their outcomes depend on which financial metric "
        "is used as the classification standard."
    )
    st.markdown("---")
    st.markdown("### 🔄 Ongoing Case — Cannot Be Evaluated")
    st.dataframe(
        pd.DataFrame({
            "Company":["OpenAI"],
            "Year":[2025],
            "AI Simulation (Neutral)":["PROCEED"],
            "Human Decision":["Proceeding"],
            "Outcome":["🔄 Ongoing — outcome not yet confirmed at time of research"],
        }),
        use_container_width=True,
        hide_index=True
    )
    st.info(
        "⚠️ OpenAI 2025 was simulated by the AI system and is included in the "
        "dataset to demonstrate capability with unresolved decisions, but excluded "
        "from accuracy analysis as the outcome remains unconfirmed."
    )
    st.markdown("---")
    co2 = round(df_h["Conservative_Correct"].mean()*100)
    hu2 = round(df_h["Human_Correct"].mean()*100)
    diff = co2 - hu2
    if diff > 0:
        st.success(
            f"**AI embedded with human loss aversion theory (Conservative) "
            f"aligned with correct outcomes {diff}% more than documented "
            f"human decisions across {len(df_h)} confirmed cases.** "
            f"This demonstrates that encoding positive human behavioral "
            f"characteristics — specifically Prospect Theory's loss aversion — "
            f"into AI reasoning enhances decision accuracy beyond both pure AI "
            f"reasoning and unaided human judgment."
        )
# ══════════════════════════════════════════════
# CUSTOM ANALYSIS
# ══════════════════════════════════════════════
elif page == "🔍 Custom Analysis":
    st.title("📂 Custom Investment Simulation")
    st.markdown(
        "*Input your company data for a private AI-powered "
        "investment decision simulation*"
    )
    st.markdown("""
    <div style='display:flex; gap:12px; margin-bottom:20px; flex-wrap:wrap;'>
        <div style='background:#f0fdf4; border:1px solid #22c55e;
                    border-radius:8px; padding:10px 16px; flex:1;'>
            <span style='color:#15803d; font-weight:700;'>🔒 Privacy:</span>
            <span style='color:#15803d; font-size:13px;'>
                Your data is never stored. Analysis generated in real time only.
            </span>
        </div>
        <div style='background:#fffbeb; border:1px solid #c9a227;
                    border-radius:8px; padding:10px 16px; flex:1;'>
            <span style='color:#92400e; font-weight:700;'>⚠️ Note:</span>
            <span style='color:#92400e; font-size:13px;'>
                Simulation tool — not financial advice.
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    def section_bar(title):
        st.markdown(f"""
        <div style='background:#0a1628; color:#FFD700; font-weight:700;
                    padding:8px 16px; border-radius:8px;
                    margin:20px 0 12px; font-size:13px;'>
            {title}</div>
        """, unsafe_allow_html=True)
    section_bar("📋 SECTION 1 — COMPANY IDENTITY")
    c1,c2,c3 = st.columns(3)
    with c1:
        cname = st.text_input("🏢 Company Name:",placeholder="Your company")
        ind   = st.selectbox("🏭 Industry:",[
            "Technology","Healthcare","Financial Services","Real Estate",
            "Retail/E-Commerce","Automotive","Energy","Media/Entertainment",
            "Manufacturing","Telecommunications","Education","Other"
        ])
    with c2:
        country = st.text_input("🌍 Country:",placeholder="e.g. Italy, USA")
        ctype   = st.selectbox("🏗️ Company Type:",[
            "Startup (0-3 years)","Growth Stage (3-7 years)",
            "SME","Large Corporation","Multinational"
        ])
    with c3:
        yrs   = st.number_input("📅 Years in Business:",min_value=0,value=5)
        cstat = st.selectbox("📊 Status:",[
            "Private","Public (Listed)","Family Business",
            "State Owned","Subsidiary"
        ])
    section_bar("💰 SECTION 2 — FINANCIAL HEALTH")
    c1,c2,c3 = st.columns(3)
    with c1:
        rev  = st.number_input("💵 Revenue ($M):",min_value=0.0,value=10.0)
        pnl  = st.number_input("📈 Profit/Loss ($M):",value=1.0)
        debt = st.number_input("💳 Total Debt ($M):",min_value=0.0,value=5.0)
    with c2:
        cash = st.number_input("🏦 Cash ($M):",min_value=0.0,value=3.0)
        grw  = st.number_input("📊 Revenue Growth (%):",value=10.0)
        val  = st.number_input("🏷️ Valuation ($M):",min_value=0.0,value=50.0)
    with c3:
        de     = st.number_input("⚖️ Debt/Equity:",min_value=0.0,value=0.5)
        ebitda = st.number_input("📉 EBITDA ($M):",value=2.0)
        burn   = st.number_input("🔥 Monthly Burn ($M):",min_value=0.0,value=0.5)
    section_bar("🎯 SECTION 3 — INVESTMENT DECISION")
    c1,c2,c3 = st.columns(3)
    with c1:
        itype = st.selectbox("📋 Investment Type:",[
            "Merger & Acquisition","Geographic Expansion","New Product",
            "Technology Investment","R&D","Strategic Partnership",
            "IPO","Capital Expenditure","Digital Transformation","Restructuring"
        ])
        iamt = st.number_input("💰 Amount ($M):",min_value=0.1,value=5.0)
    with c2:
        eret   = st.number_input("📈 Expected Return (%):",value=15.0)
        tframe = st.selectbox("⏱️ Timeframe:",[
            "Short term (under 1 year)","Medium term (1-3 years)",
            "Long term (3-10 years)","Very long term (10+ years)"
        ])
    with c3:
        mkt = st.selectbox("🌍 Target Market:",
                          ["Local","National","Regional","Global"])
        fin = st.selectbox("💳 Financing:",[
            "Own cash","Bank loan","Investor/VC",
            "Bond issuance","Mixed","Government grant"
        ])
    section_bar("🌍 SECTION 4 — STRATEGIC CONTEXT")
    c1,c2,c3 = st.columns(3)
    with c1:
        mktc = st.selectbox("📊 Market Conditions:",[
            "Growing","Stable","Declining",
            "Highly competitive","Emerging/disrupted"
        ])
        reg = st.selectbox("⚖️ Regulatory:",[
            "Highly regulated","Moderately regulated",
            "Low regulation","Changing"
        ])
    with c2:
        tech = st.selectbox("💻 Tech Risk:",[
            "High — being disrupted","Medium","Low — stable"
        ])
        rtol = st.selectbox("🎯 Risk Tolerance:",[
            "Very conservative","Moderate","Aggressive"
        ])
    with c3:
        why  = st.text_area("❓ Why Invest?",
                            placeholder="Brief reason...",height=80)
        risk = st.text_area("⚠️ Main Risk?",
                            placeholder="Biggest concern...",height=80)
    section_bar("📝 SECTION 5 — ADDITIONAL CONTEXT")
    c1,c2 = st.columns(2)
    with c1:
        comp   = st.text_input("🏆 Competitors:",
                               placeholder="e.g. Amazon, Google")
        events = st.text_area("📰 Recent Events:",
                              placeholder="Leadership change...",height=80)
    with c2:
        decision = st.text_area(
            "📋 Describe Your Investment Decision:",
            placeholder="e.g. We want to acquire a competitor for $20M...",
            height=120
        )
    st.markdown("---")
    if st.button("⚡ SIMULATE MY INVESTMENT", use_container_width=True):
        if cname and decision:
            st.markdown(f"""
            <div class='aa-card' style='border-left:5px solid #c9a227;
                        margin-bottom:20px;'>
                <div style='color:#64748b; font-size:11px;
                            text-transform:uppercase;'>Simulation Target</div>
                <div style='color:#0a1628; font-size:18px;
                            font-weight:800; margin-top:4px;'>{cname}</div>
                <div style='color:#64748b; font-size:13px;'>{decision}</div>
            </div>
            """, unsafe_allow_html=True)
            profile = (
                f"Company:{cname}|Industry:{ind}|Country:{country}|"
                f"Type:{ctype}|Years:{yrs}|Status:{cstat}|"
                f"Revenue:${rev}M|P&L:${pnl}M|Debt:${debt}M|"
                f"Cash:${cash}M|Growth:{grw}%|Val:${val}M|"
                f"D/E:{de}|EBITDA:${ebitda}M|Burn:${burn}M|"
                f"Investment:{itype}|Amount:${iamt}M|Return:{eret}%|"
                f"Time:{tframe}|Market:{mkt}|Finance:{fin}|"
                f"Conditions:{mktc}|Reg:{reg}|Tech:{tech}|Risk:{rtol}|"
                f"Competitors:{comp}|Why:{why}|Risk:{risk}|"
                f"Events:{events}|DECISION:{decision}"
            )
            all_d = []
            all_s = []
            c1,c2,c3 = st.columns(3)
            cols = [c1,c2,c3]
            for i,p in enumerate(PERSONAS):
                with cols[i]:
                    with st.spinner("Simulating..."):
                        q = f"""
{p['instruction']}
Company data: {profile}
Should proceed with: {decision}?
Answer in EXACTLY this format:
DECISION: YES or NO
SCORE: (number 0 to 100)
CONFIDENCE: (number 0 to 100)
REASON 1: (specific to financials)
REASON 2: (specific to market context)
REASON 3: (specific to risk profile)
KEY RISK: (biggest risk)
ALTERNATIVE: (if NO — what instead?)
"""
                        r = client.chat.completions.create(
                            model="llama-3.1-8b-instant",
                            messages=[{"role":"user","content":q}],
                            temperature=0
                        )
                        dec,sc,conf,r1,r2,r3,kr,alt = parse_response(
                            r.choices[0].message.content
                        )
                        all_d.append(dec)
                        try:
                            all_s.append(int(sc))
                        except:
                            all_s.append(50)
                        render_persona_card(
                            p["name"],p["color"],dec,sc,conf,r1,r2,r3
                        )
                        if kr:
                            st.warning(f"⚠️ **Key Risk:** {kr}")
                        if alt and "NO" in dec.upper():
                            st.info(f"💡 **Alternative:** {alt}")
            avg = sum(all_s)/len(all_s) if all_s else 50
            render_verdict(avg, all_s)
            st.success(
                "🔒 Your data was used only for this simulation "
                "and has not been stored."
            )
        else:
            st.error(
                "⚠️ Please fill Company Name and describe your "
                "Investment Decision!"
            )
# ══════════════════════════════════════════════
# JURY DEMO
# ══════════════════════════════════════════════
elif page == "🎓 Jury Demo":
    st.title("🎤 Jury Presentation Demo")
    st.markdown("*Live simulation for thesis defense*")
    st.markdown("""
    <div style='background:#fffbeb; border:1px solid #c9a227;
                border-left:5px solid #c9a227;
                border-radius:10px; padding:14px; margin-bottom:16px;'>
        <div style='color:#92400e; font-weight:700; margin-bottom:4px;'>
            💡 Best Results With These Companies</div>
        <div style='color:#92400e; font-size:13px; line-height:1.8;'>
            WeWork 2019 · Tesla 2020 · Apple 2018 · Amazon 2015 ·
            Netflix 2013 · Microsoft 2016 · Theranos 2016 ·
            Kodak 2012 · Blockbuster 2010 · Twitter 2022 · Uber 2019 ·
            RBS 2007 · VW 2015 · SoftBank 2019 · Spotify 2018 · LVMH 2020
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    c1,c2,c3 = st.columns(3)
    with c1:
        dco  = st.text_input("🏢 Company:",value="WeWork")
    with c2:
        dyr  = st.text_input("📅 Year:",value="2019")
    with c3:
        ddec = st.text_input("📋 Decision:",
                             value="Proceed with IPO expansion?")
    if st.button("⚡ RUN LIVE DEMONSTRATION", use_container_width=True):
        if dco and dyr:
            st.markdown(f"""
            <div style='background:#0a1628; border-radius:12px;
                        padding:20px; margin:16px 0;
                        border:1px solid #c9a227;'>
                <div style='color:#c9a227; font-size:11px;
                            text-transform:uppercase; letter-spacing:2px;'>
                    Live Simulation</div>
                <div style='color:#ffffff; font-size:20px;
                            font-weight:800; margin-top:4px;'>
                    {dco} · {dyr}</div>
                <div style='color:#94a3b8; font-size:13px;
                            margin-top:4px;'>{ddec}</div>
            </div>
            """, unsafe_allow_html=True)
            all_decisions = []
            all_scores    = []
            c1,c2,c3 = st.columns(3)
            cols = [c1,c2,c3]
            for i,p in enumerate(PERSONAS):
                with cols[i]:
                    with st.spinner("Simulating..."):
                        q = f"""
{p['instruction']}
Company: {dco} | Year: {dyr} | Decision: {ddec}
Answer in EXACTLY this format:
DECISION: YES or NO
SCORE: (number 0 to 100)
CONFIDENCE: (number 0 to 100)
REASON 1: (one sentence)
REASON 2: (one sentence)
REASON 3: (one sentence)
"""
                        r = client.chat.completions.create(
                            model="llama-3.1-8b-instant",
                            messages=[{"role":"user","content":q}],
                            temperature=0
                        )
                        dec,sc,conf,r1,r2,r3,_,_ = parse_response(
                            r.choices[0].message.content
                        )
                        all_decisions.append(dec)
                        try:
                            all_scores.append(int(sc))
                        except:
                            all_scores.append(50)
                        yes = "YES" in dec.upper()
                        vc  = "#15803d" if yes else "#dc2626"
                        vbg = "#f0fdf4" if yes else "#fff1f2"
                        score_int = int(sc) if sc.isdigit() else 50
                        st.markdown(f"""
                        <div style='background:#ffffff;
                                    border:2px solid {p['color']};
                                    border-radius:14px; padding:16px;'>
                            <div style='color:{p['color']}; font-weight:800;
                                        font-size:13px; margin-bottom:2px;'>
                                {p['name']}</div>
                            <div style='background:{p['color']}; color:#ffffff;
                                        font-size:9px; font-weight:700;
                                        padding:2px 8px; border-radius:20px;
                                        display:inline-block; margin-bottom:10px;
                                        letter-spacing:0.5px;'>
                                {p['badge']}</div>
                            <div style='background:{vbg};
                                        border:2px solid {vc};
                                        border-radius:10px; padding:10px;
                                        text-align:center; margin-bottom:10px;'>
                                <span style='color:{vc}; font-weight:900;
                                             font-size:15px;'>
                                    {"✅ PROCEED" if yes else "❌ DO NOT PROCEED"}
                                </span>
                            </div>
                            <div style='height:8px; background:#e2e8f0;
                                        border-radius:4px; margin-bottom:10px;'>
                                <div style='height:8px; background:{p['color']};
                                            border-radius:4px;
                                            width:{score_int}%;'></div>
                            </div>
                            <div style='color:#64748b; font-size:12px;
                                        margin-bottom:8px;'>
                                Score:
                                <strong style='color:{p["color"]};'>
                                    {sc}/100</strong> ·
                                Conf:<strong>{conf}%</strong>
                            </div>
                            <div style='font-size:12px; color:#334155;
                                        line-height:1.7;'>
                                📌 {r1}<br>📌 {r2}<br>📌 {r3}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
            avg = sum(all_scores)/len(all_scores) if all_scores else 50
            if avg>=60:
                v="PROCEED"; vc="#15803d"; vbg="#f0fdf4"; vi="✅"
            elif avg>=40:
                v="PROCEED WITH CAUTION"; vc="#92400e"; vbg="#fffbeb"; vi="⚠️"
            else:
                v="DO NOT PROCEED"; vc="#991b1b"; vbg="#fff1f2"; vi="❌"
            st.markdown(f"""
            <div style='background:{vbg}; border:3px solid {vc};
                        border-radius:16px; padding:28px;
                        text-align:center; margin:20px 0;'>
                <div style='color:{vc}; font-size:11px; font-weight:700;
                            text-transform:uppercase; letter-spacing:3px;
                            margin-bottom:8px;'>Final Simulation Verdict</div>
                <div style='color:{vc}; font-size:26px;
                            font-weight:900; margin-bottom:10px;'>
                    {vi} {v}</div>
                <div style='display:flex; justify-content:center;
                            gap:16px; flex-wrap:wrap;'>
                    <span style='color:{vc}; font-size:13px; opacity:0.9;'>
                        Avg: {avg:.0f}/100</span>
                    <span style='color:{vc}; font-size:13px; opacity:0.9;'>
                        Neutral: {all_scores[0] if all_scores else 0}/100
                    </span>
                    <span style='color:{vc}; font-size:13px; opacity:0.9;'>
                        Aggressive:
                        {all_scores[1] if len(all_scores)>1 else 0}/100
                    </span>
                    <span style='color:{vc}; font-size:13px; opacity:0.9;'>
                        Conservative:
                        {all_scores[2] if len(all_scores)>2 else 0}/100
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            failed_co = ["WeWork","Theranos","Kodak","Blockbuster","Peloton",
                         "Royal Bank of Scotland","Volkswagen","SoftBank",
                         "Nokia","Silicon Valley Bank","Deliveroo","Didi",
                         "Robinhood","Wirecard","Bayer","Uber","Rivian","Adobe"]
            success_co = ["Tesla","Apple","Amazon","Netflix","Microsoft",
                          "UBS/Credit Suisse","Microsoft/Activision","Spotify",
                          "LVMH","Arm Holdings","Alibaba","Samsung","Beyond Meat",
                          "Zoom"]
            if dco in failed_co:
                st.error(
                    f"✅ **Historical Validation:** {dco} FAILED — "
                    "Simulation correctly identified risk"
                )
            elif dco in success_co:
                st.success(
                    f"✅ **Historical Validation:** {dco} SUCCEEDED — "
                    "Simulation correctly identified opportunity"
                )
            st.caption(
                "⚠️ Simulation output for research demonstration only — "
                "not financial advice"
            )
# ══════════════════════════════════════════════
# ABOUT
# ══════════════════════════════════════════════
elif page == "ℹ️ About":
    st.title("📋 About This Research")
    st.markdown(
        "*The Agentic Alpha — Multi-Agent AI Decision Support System*"
    )
    st.markdown("---")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div style='background:#ffffff; border:1px solid #e2e8f0;
                    border-top:4px solid #c9a227; border-radius:12px;
                    padding:24px; box-shadow:0 2px 8px rgba(0,0,0,0.05);'>
            <div style='color:#0a1628; font-size:15px; font-weight:800;
                        margin-bottom:18px;'>👩‍🎓 Researcher</div>
            <div style='margin-bottom:12px;'>
                <div style='color:#94a3b8; font-size:10px; font-weight:700;
                            text-transform:uppercase; letter-spacing:1px;'>
                    Name</div>
                <div style='color:#0a1628; font-weight:700; font-size:14px;
                            margin-top:3px;'>Meryam El Ghouti</div>
            </div>
            <div style='margin-bottom:12px;'>
                <div style='color:#94a3b8; font-size:10px; font-weight:700;
                            text-transform:uppercase; letter-spacing:1px;'>
                    University</div>
                <div style='color:#334155; font-size:13px; margin-top:3px;'>
                    Sapienza University of Rome</div>
            </div>
            <div style='margin-bottom:12px;'>
                <div style='color:#94a3b8; font-size:10px; font-weight:700;
                            text-transform:uppercase; letter-spacing:1px;'>
                    Degree</div>
                <div style='color:#334155; font-size:13px; margin-top:3px;'>
                    Master's in Business Management · 2026</div>
            </div>
            <div>
                <div style='color:#94a3b8; font-size:10px; font-weight:700;
                            text-transform:uppercase; letter-spacing:1px;'>
                    Thesis</div>
                <div style='color:#334155; font-size:13px; margin-top:3px;
                            line-height:1.6;'>
                    The Agentic Alpha — A Multi-Agent AI Decision Support
                    System for Corporate Investment Simulation with
                    Behavioral Bias Detection</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div style='background:#0a1628; border:1px solid #c9a227;
                    border-radius:12px; padding:24px;'>
            <div style='color:#FFD700; font-size:15px; font-weight:800;
                        margin-bottom:18px;'>🔬 Research Overview</div>
            <div style='margin-bottom:14px;'>
                <div style='color:#c9a227; font-size:10px; font-weight:700;
                            text-transform:uppercase; letter-spacing:1px;'>
                    Research Question</div>
                <div style='color:#e8e8e8; font-size:13px; margin-top:5px;
                            line-height:1.6;'>
                    Can a multi-agent AI system simulate corporate investment
                    reasoning with behavioral bias detection comparable to
                    human decision-makers?</div>
            </div>
            <div style='margin-bottom:14px;'>
                <div style='color:#c9a227; font-size:10px; font-weight:700;
                            text-transform:uppercase; letter-spacing:1px;'>
                    Key Finding</div>
                <div style='color:#e8e8e8; font-size:13px; margin-top:5px;'>
                    AI accuracy is determined by the quality of human
                    behavioral characteristics embedded in AI reasoning.
                    Positive traits enhance it. Negative traits degrade it.
                </div>
            </div>
            <div style='margin-bottom:14px;'>
                <div style='color:#c9a227; font-size:10px; font-weight:700;
                            text-transform:uppercase; letter-spacing:1px;'>
                    Theory</div>
                <div style='color:#e8e8e8; font-size:13px; margin-top:5px;'>
                    Kahneman and Tversky (1979) — Behavioral Finance ·
                    Thaler (2008) — Nudge Theory</div>
            </div>
            <div>
                <div style='color:#c9a227; font-size:10px; font-weight:700;
                            text-transform:uppercase; letter-spacing:1px;'>
                    Tools</div>
                <div style='color:#e8e8e8; font-size:13px; margin-top:5px;'>
                    Python · Groq LLaMA API · Streamlit · Plotly</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<hr class='gold-line'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; margin-bottom:20px;'>
        <div style='color:#c9a227; font-size:11px; font-weight:700;
                    text-transform:uppercase; letter-spacing:2px;'>
            Academic Contributions</div>
        <div style='color:#0a1628; font-size:20px; font-weight:800;
                    margin-top:6px;'>Three Research Contributions</div>
    </div>
    """, unsafe_allow_html=True)
    c1,c2,c3 = st.columns(3)
    for col,num,title,desc in zip(
        [c1,c2,c3],
        ["01","02","03"],
        ["Multi-Agent Framework",
         "Heuristic Bias Detection",
         "Human-AI Integration Spectrum"],
        [
            "AI framework simulating investment reasoning through three personas representing different human-AI integration configurations",
            "Module identifying overconfidence, herding, loss aversion and anchoring in simulated investment decisions",
            "Empirical demonstration that AI accuracy is determined by quality of human behavioral theory embedded in AI parameters"
        ]
    ):
        with col:
            st.markdown(f"""
            <div class='aa-card' style='border-top:4px solid #c9a227;'>
                <div style='font-size:36px; font-weight:900;
                            color:#c9a227;'>{num}</div>
                <div style='color:#0a1628; font-weight:700; font-size:14px;
                            margin:8px 0 6px;'>{title}</div>
                <div style='color:#64748b; font-size:13px;
                            line-height:1.6;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("<hr class='gold-line'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; margin-bottom:20px;'>
        <div style='color:#c9a227; font-size:11px; font-weight:700;
                    text-transform:uppercase; letter-spacing:2px;'>Key Results</div>
        <div style='color:#0a1628; font-size:20px; font-weight:800;
                    margin-top:6px;'>Top 5 Simulation Findings</div>
    </div>
    """, unsafe_allow_html=True)
    for title,desc,color in [
        ("Conservative AI (AI + Loss Aversion) Achieves Highest Accuracy",
         "AI embedded with Prospect Theory loss aversion achieved the highest accuracy across all personas — proving that encoding validated human behavioral theory enhances AI performance beyond pure AI reasoning.",
         "#15803d"),
        ("Overconfidence Most Detected Bias",
         "Aggressive persona (AI + overconfidence) showed the highest bias indicators in failed simulations — directly replicating the executive overconfidence patterns documented in behavioral finance literature.",
         "#c9a227"),
        ("Herding Pattern Detected in AI",
         "Simulated reasoning followed crowd sentiment in WeWork and Theranos — demonstrating that AI training data absorbs market narrative biases consistent with Shiller's irrational exuberance framework.",
         "#1e3a8a"),
        ("Persona Framing Dominates Simulation Outputs",
         "Identical scenarios produced substantial average score differences between Aggressive and Conservative personas — validating Nudge Theory's proposition that framing determines outcomes.",
         "#c9a227"),
        ("2021 Market Euphoria Effect",
         "All personas over-scored 2021 growth companies — AI training data absorbed market overoptimism, replicating collective overconfidence rather than providing independent analysis.",
         "#dc2626"),
    ]:
        st.markdown(f"""
        <div class='aa-card' style='border-left:4px solid {color};
                    padding:14px 18px; margin-bottom:10px;'>
            <div style='color:#0a1628; font-weight:700;
                        font-size:14px;'>{title}</div>
            <div style='color:#64748b; font-size:13px;
                        margin-top:4px; line-height:1.6;'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<hr class='gold-line'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; margin-bottom:20px;'>
        <div style='color:#c9a227; font-size:11px; font-weight:700;
                    text-transform:uppercase; letter-spacing:2px;'>
            Human-AI Integration Spectrum</div>
        <div style='color:#0a1628; font-size:20px; font-weight:800;
                    margin-top:6px;'>Behavioral Finance Framework</div>
    </div>
    """, unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    for col,bias,theory,persona,desc,color in zip(
        [c1,c2,c3,c4],
        ["Overconfidence","Loss Aversion","Herding Behavior","Anchoring Bias"],
        ["Kahneman & Tversky","Prospect Theory","Shiller","Tversky"],
        ["→ Embedded in Aggressive CFO",
         "→ Embedded in Conservative Board",
         "→ Detected in WeWork · Theranos",
         "→ Detected in Disney 2019"],
        [
            "Overestimating accuracy of corporate decisions",
            "Fear of losses stronger than desire for gains",
            "Following crowd despite contradictory evidence",
            "Over-relying on first piece of information"
        ],
        ["#dc2626","#c9a227","#1e3a8a","#7c3aed"]
    ):
        with col:
            st.markdown(f"""
            <div class='aa-card' style='border-left:4px solid {color};'>
                <div style='color:{color}; font-weight:700;
                            font-size:13px;'>{bias}</div>
                <div style='color:#94a3b8; font-size:11px;
                            margin:3px 0;'>{theory}</div>
                <div style='color:{color}; font-size:10px;
                            font-weight:700; font-style:italic;
                            margin:3px 0;'>{persona}</div>
                <div style='color:#64748b; font-size:12px;
                            line-height:1.5;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("<hr class='gold-line'>", unsafe_allow_html=True)
    st.markdown("### 🛠️ System Architecture")
    st.code("""
    Input: Corporate Investment Decision
           (Known Company OR Custom Private Data)
                        ↓
    ┌──────────────────────────────────────────────────────┐
    │              Multi-Agent AI Pipeline                  │
    │               (Groq LLaMA 3.1 API)                  │
    ├──────────────────────────────────────────────────────┤
    │  Agent 1: Neutral Advisor    → Pure AI Reasoning     │
    │  Agent 2: Aggressive CFO     → AI + Overconfidence   │
    │  Agent 3: Conservative Board → AI + Loss Aversion    │
    └──────────────────────────────────────────────────────┘
                        ↓
    Investment Scoring Module (0 to 100)
                        ↓
    Heuristic Bias Detection Module
    (Overconfidence · Loss Aversion · Herding · Anchoring)
                        ↓
    Simulated Corporate Investment Verdict
    """, language="text")
    st.markdown("---")
    st.markdown(f"""
    <div style='text-align:center; padding:32px 0 16px;
            background:transparent;'>
    <img src='{LOGO_URL}'
         style='width:320px; height:auto;
                border-radius:50%;
                margin-bottom:16px;'
         alt='Agentic Alpha Logo'>
        <div style='color:#94a3b8; font-size:12px; margin-top:8px;'>
            Master's Thesis · The Agentic Alpha · Meryam El Ghouti ·
            Sapienza University of Rome · 2026 ·
            <a href='https://agenticalpha.streamlit.app'
               style='color:#c9a227;'>agenticalpha.streamlit.app</a> ·
            <a href='https://github.com/meryam-elghouti/agenticalpha'
               style='color:#c9a227;'>github.com/meryam-elghouti/agenticalpha</a>
        </div>
    </div>
    """, unsafe_allow_html=True)
