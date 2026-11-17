import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# SYNTHETIC CYBERSECURITY & FINANCIAL RISK DATA

np.random.seed(42)

dates = pd.date_range(
    start="2026-01-01",
    periods=90,
    freq="D"
)

df = pd.DataFrame({
    "Date": dates,

    # Email Security
    "Phishing_Attempts": np.random.randint(50, 300, 90),
    "Blocked_Phishing": np.random.randint(40, 280, 90),

    # Financial Monitoring
    "Suspicious_Transactions": np.random.randint(5, 50, 90),
    "Financial_Risk_Score": np.random.randint(30, 100, 90),

    # Endpoint Security
    "Critical_Vulnerabilities": np.random.randint(0, 15, 90),
    "High_Vulnerabilities": np.random.randint(5, 25, 90),

    # Security Operations
    "Active_Incidents": np.random.randint(1, 20, 90),
    "MTTD": np.random.randint(5, 25, 90),
    "MTTR": np.random.randint(15, 120, 90),

    # Website Security
    "SSL_Issues": np.random.randint(0, 10, 90),
    "API_Exposures": np.random.randint(0, 8, 90),
    "Open_Ports": np.random.randint(5, 30, 90),

    # Device Security
    "Device_Risk_Score": np.random.randint(40, 100, 90),
    "Security_Posture_Score": np.random.randint(60, 100, 90)
})

# ======================================================
# DERIVED METRICS
# ======================================================

df["Threat_Detection_Rate"] = (
    df["Blocked_Phishing"] /
    df["Phishing_Attempts"] * 100
).clip(0, 100)

df["Overall_Cyber_Risk"] = (
    (100 - df["Security_Posture_Score"]) * 0.25 +
    df["Financial_Risk_Score"] * 0.30 +
    df["Active_Incidents"] * 1.5 +
    df["Critical_Vulnerabilities"] * 2 +
    df["API_Exposures"] * 1.2
).round(2)

# ================================================

# Optimized Dashboard layout using Plotly Subplots, Pandas, and NumPy data structures
fig = make_subplots(
    rows=3, cols=2,
    subplot_titles=(
        "<b>Overall Cyber Risk Trend</b>",
        "<b>Phishing Efficacy (Attempts vs. Blocked)</b>",
        "<b>Vulnerability Distribution (Critical & High)</b>",
        "<b>Financial Risk vs. Suspicious Incidents</b>",
        "<b>Ops Load & Efficiency (Incidents & MTTR)</b>",
        "<b>Posture and Device Integrity Scores</b>"
    ),
    vertical_spacing=0.12,
    horizontal_spacing=0.10
)

# 1. Overall Cyber Risk Trend
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Overall_Cyber_Risk'],
        name='Overall Cyber Risk',
        line=dict(color='firebrick', width=2.5),
        hovertemplate='Date: %{x}<br>Risk: %{y}'
    ),
    row=1, col=1
)

# 2. Phishing Attempts vs Blocked (Using barmode grouped look via overlapping offset)
fig.add_trace(
    go.Bar(
        x=df['Date'],
        y=df['Phishing_Attempts'],
        name='Phishing Attempts',
        marker_color='#1f77b4',
        hovertemplate='Date: %{x}<br>Attempts: %{y}'
    ),
    row=1, col=2
)
fig.add_trace(
    go.Bar(
        x=df['Date'],
        y=df['Blocked_Phishing'],
        name='Blocked Phishing',
        marker_color='#2ca02c',
        hovertemplate='Date: %{x}<br>Blocked: %{y}'
    ),
    row=1, col=2
)

# 3. Endpoint Vulnerabilities
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Critical_Vulnerabilities'],
        name='Critical Vulns',
        stackgroup='one',
        fillcolor='rgba(214, 39, 40, 0.65)',
        line=dict(width=0.5, color='red'),
        hovertemplate='Date: %{x}<br>Critical: %{y}'
    ),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['High_Vulnerabilities'],
        name='High Vulns',
        stackgroup='one',
        fillcolor='rgba(255, 127, 14, 0.55)',
        line=dict(width=0.5, color='orange'),
        hovertemplate='Date: %{x}<br>High: %{y}'
    ),
    row=2, col=1
)

# 4. Financial Risk vs Suspicious Transactions
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Financial_Risk_Score'],
        name='Financial Risk Score',
        line=dict(color='purple', width=2, dash='dash'),
        hovertemplate='Date: %{x}<br>Risk Score: %{y}'
    ),
    row=2, col=2
)
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Suspicious_Transactions'],
        name='Suspicious Transactions',
        line=dict(color='indigo', width=2),
        hovertemplate='Date: %{x}<br>Transactions: %{y}'
    ),
    row=2, col=2
)

# 5. Security Operations
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Active_Incidents'],
        name='Active Incidents',
        mode='lines+markers',
        marker=dict(size=4),
        line=dict(color='teal', width=1.5),
        hovertemplate='Date: %{x}<br>Active Incidents: %{y}'
    ),
    row=3, col=1
)
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['MTTR'],
        name='MTTR (min)',
        line=dict(color='grey', width=1.5, dash='dot'),
        hovertemplate='Date: %{x}<br>MTTR: %{y} min'
    ),
    row=3, col=1
)

# 6. Posture and Device Risk
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Security_Posture_Score'],
        name='Security Posture',
        line=dict(color='forestgreen', width=2),
        hovertemplate='Date: %{x}<br>Posture: %{y}'
    ),
    row=3, col=2
)
fig.add_trace(
    go.Scatter(
        x=df['Date'],
        y=df['Device_Risk_Score'],
        name='Device Risk',
        line=dict(color='goldenrod', width=1.5),
        hovertemplate='Date: %{x}<br>Device Risk: %{y}'
    ),
    row=3, col=2
)

# Layout Configurations
fig.update_layout(
    title_text="<b>Enterprise Cybersecurity & Financial Risk Dashboard</b>",
    title_font_size=22,
    height=950,
    width=1150,
    barmode='group',
    showlegend=True,
    template="plotly_white",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)

# Update axis properties for clean design
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')

fig.show()

!pip install --upgrade langchain-google-genai google-generativeai langgraph==1.1.1 langsmith

import os
os.environ["LANGSMITH_API_KEY"] = "LangSmith"

!pip install --upgrade "mcp[cli]"
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("GeminiTools")

@mcp.tool()
def search(query: str) -> list:
    # Your search logic here
    return ["Result 1", "Result 2"]

!cd mcp-server-demo

!cd mcp-server-demo && uv add langchain-google-genai langgraph langsmith

import os
import json
import random
import pandas as pd
from google.colab import userdata
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END
from typing import TypedDict
from mcp.server.mcpserver import MCPServer
from langsmith.run_helpers import traceable

# SentinelAI Agent State Definition
class SentinelAIState(TypedDict):
    input: str
    logs: str
    symptom: str
    diagnostic_report: str
    context: dict
    kpi_metrics: dict
    trace_id: str
    threat_model: dict
    resilience_model: dict
    immune_response: dict

# SentinelAI Prompt Template (Incorporating Plotly Dashboard Data Analysis)
prompt = ChatPromptTemplate.from_template("""
You are the Agentic Reasoning Layer of SentinelAI, an Autonomous Threat Investigation System.

Core Principles:
- Multi-Step Threat Investigation & Correlation: Evaluate indicators across phishing, endpoint, financial, and device integrity.
- Data-Driven Posture Analytics: Provide continuous assessment using live telemetry metrics.
- Transparent Diagnostic Reasoning: Deliver precise root-cause analysis and mitigation strategies.

Signal/Symptom: {symptom}
Incident Logs: {logs}

[DASHBOARD METRICS & TRENDS FOR ANALYSIS]
{graph_metrics_summary}

[OPERATIONAL TELEMETRY]
{kpi_data}

Your tasks:
1. Correlate the dashboard trend statistics with the active incident symptoms.
2. Diagnose anomalies, security posture drift, and systemic vulnerabilities.
3. Propose defensive actions and digital antibodies to mitigate the discovered risks.
""")

# Gemini Model Binding
api_key = userdata.get("Ben856")
os.environ["GOOGLE_API_KEY"] = api_key

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=api_key
)

try:
    tools = [search]
    llm_with_tools = llm.bind_tools(tools)
except NameError:
    llm_with_tools = llm

# Entry Node — SentinelAI Data Synthesis
@traceable(name="sentinel_entry_node")
def entry_node(state: SentinelAIState) -> SentinelAIState:
    # Synthesizing and summarizing the Plotly dataset 'df'
    graph_summary = {}
    try:
        global df
        if 'df' in globals() and not df.empty:
            graph_summary = {
                "Days Covered": len(df),
                "Mean Cyber Risk Index": round(df["Overall_Cyber_Risk"].mean(), 2),
                "Peak Cyber Risk": round(df["Overall_Cyber_Risk"].max(), 2),
                "Mean Phishing Attempts/Day": round(df["Phishing_Attempts"].mean(), 2),
                "Mean Blocked Phishing": round(df["Blocked_Phishing"].mean(), 2),
                "Phishing Block Efficacy (%)": round((df["Blocked_Phishing"].sum() / df["Phishing_Attempts"].sum()) * 100, 2),
                "Average Active Incidents": round(df["Active_Incidents"].mean(), 2),
                "Mean Mean-Time-To-Resolve (MTTR - mins)": round(df["MTTR"].mean(), 2),
                "Mean Security Posture Score": round(df["Security_Posture_Score"].mean(), 2)
            }
    except Exception as e:
        graph_summary = {"error": f"DataFrame metrics unavailable: {str(e)}"}

    kpi_summary = {
        "Threat Velocity": {"current": 0.42, "baseline": 0.30},
        "Anomaly Density": {"current": 0.18, "baseline": 0.25},
        "Incident Response Time (sec)": {"current": 1.4, "baseline": 2.1},
        "System Stability": {"current": 0.92, "baseline": 0.80}
    }

    threat_model = {
        "detected": True,
        "type": "Behavioral Drift",
        "confidence": 0.87,
        "antibody_synthesized": True,
        "deployment_time_ms": 420
    }

    resilience_model = {
        "resilience_score": 0.91,
        "bottlenecks": ["Network Latency", "Resource Allocation"],
        "risk_projection": "Low",
        "timeline_projection_min": 12
    }

    immune_response = {
        "digital_antibody": "ACIS-ABX-2026",
        "response_vector": "behavioral-correction",
        "effectiveness": 0.93
    }

    return {
        **state,
        "symptom": state["input"],
        "kpi_metrics": kpi_summary,
        "threat_model": threat_model,
        "resilience_model": resilience_model,
        "immune_response": immune_response,
        "context": {**state.get("context", {}), "graph_summary": graph_summary},
        "trace_id": f"sentinel-trace-{random.randint(1000, 9999)}"
    }

# LLM Node — SentinelAI Reasoning Layer
@traceable(name="sentinel_llm_node")
def llm_node(state: SentinelAIState) -> SentinelAIState:
    kpi_str = json.dumps(state["kpi_metrics"], indent=2)
    graph_metrics_str = json.dumps(state["context"].get("graph_summary", {}), indent=2)

    messages = prompt.format_messages(
        symptom=state["symptom"],
        logs=state.get("logs", "Normal operational telemetry"),
        kpi_data=kpi_str,
        graph_metrics_summary=graph_metrics_str
    )

    response = llm_with_tools.invoke(messages)

    return {
        **state,
        "diagnostic_report": response.content
    }

# Display Node — SentinelAI Analysis Output
@traceable(name="sentinel_display_node")
def display_node(state: SentinelAIState) -> SentinelAIState:
    print("\n=== SentinelAI Autonomous Threat Investigation Report ===")
    print(f"Trace ID: {state['trace_id']}")
    print(f"Context Source: {state['context'].get('source', 'SentinelAI Hub')}")

    print("\n--- Threat Model ---")
    print(json.dumps(state["threat_model"], indent=2))

    print("\n--- Resilience Simulation ---")
    print(json.dumps(state["resilience_model"], indent=2))

    print("\n--- Cyber Response & Immunization ---")
    print(json.dumps(state["immune_response"], indent=2))

    print("\n--- SentinelAI Threat Trend Analysis (Gemini Evaluated) ---")
    print(state["diagnostic_report"])

    return state

# SentinelAI Workflow Graph
workflow = StateGraph(SentinelAIState)
workflow.add_node("entry", entry_node)
workflow.add_node("llm", llm_node)
workflow.add_node("display", display_node)

workflow.set_entry_point("entry")
workflow.add_edge("entry", "llm")
workflow.add_edge("llm", "display")
workflow.add_edge("display", END)

agent_executor = workflow.compile()

# Execute SentinelAI
agent_executor.invoke({
    "input": "Analyze the overall cyber risk trends and security metrics from our dashboard.",
    "logs": "Telemetry logs indicate anomalous phishing surges and unstable MTTR spikes.",
    "context": {"source": "Enterprise Security Dashboard"}
})
