# ============================================================
# SENTINEL AI: Autonomous Cybersecurity Intelligence Platform
# ============================================================

import os
import io
import json
import base64
import random
import numpy as np
import pandas as pd
from fastapi import FastAPI, Request, Body
from fastapi.responses import HTMLResponse, JSONResponse
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from langsmith import Client
from typing import TypedDict

try:
    from mcp.server import MCPServer
    MCP_ENABLED = True
except Exception:
    MCP_ENABLED = False

# ============================================================
# GEMINI
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    api_key=os.environ["GOOGLE_API_KEY"]
)
# =============================================================
# MCP SERVER
# =============================================================

if MCP_ENABLED:
    try:
        mcp_server = MCPServer(
            name="SentinelAI-MCP"
        )
    except Exception:
        mcp_server = None
else:
    mcp_server = None

# ============================================================
# LANGSMITH
# ============================================================

ls_client = Client()

def trace_run(user_input, output):

    try:

        ls_client.create_run(
            name="sentinel-ai-run",
            inputs={"input": user_input},
            outputs=output
        )

    except:
        pass

# ============================================================
# BASE64 REPORT EXPORT
# ============================================================

def encode_report(data):

    return base64.b64encode(
        json.dumps(
            data,
            indent=2,
            default=str
        ).encode()
    ).decode()

# ============================================================
# CYBER DATASET
# ============================================================

np.random.seed(42)

dates = pd.date_range(
    start="2026-01-01",
    periods=90,
    freq="D"
)

df = pd.DataFrame({

    "Date": dates,

    "Phishing_Attempts":
        np.random.randint(50,300,90),

    "Blocked_Phishing":
        np.random.randint(40,280,90),

    "Suspicious_Transactions":
        np.random.randint(5,50,90),

    "Financial_Risk_Score":
        np.random.randint(30,100,90),

    "Critical_Vulnerabilities":
        np.random.randint(0,15,90),

    "High_Vulnerabilities":
        np.random.randint(5,25,90),

    "Active_Incidents":
        np.random.randint(1,20,90),

    "MTTD":
        np.random.randint(5,25,90),

    "MTTR":
        np.random.randint(15,120,90),

    "SSL_Issues":
        np.random.randint(0,10,90),

    "API_Exposures":
        np.random.randint(0,8,90),

    "Open_Ports":
        np.random.randint(5,30,90),

    "Device_Risk_Score":
        np.random.randint(40,100,90),

    "Security_Posture_Score":
        np.random.randint(60,100,90)
})

# ============================================================
# DERIVED METRICS
# ============================================================

df["Threat_Detection_Rate"] = (

    df["Blocked_Phishing"]
    /
    df["Phishing_Attempts"]

) * 100


df["Overall_Cyber_Risk"] = (

    (100 - df["Security_Posture_Score"]) * 0.25
    +
    df["Financial_Risk_Score"] * 0.30
    +
    df["Active_Incidents"] * 1.5
    +
    df["Critical_Vulnerabilities"] * 2
    +
    df["API_Exposures"] * 1.2

)

# ============================================================
# DASHBOARD CREATION
# ============================================================

def create_dashboard():

    fig = make_subplots(
        rows=3,
        cols=2
    )

    fig.add_trace(

        go.Scatter(
            x=df["Date"],
            y=df["Overall_Cyber_Risk"],
            name="Cyber Risk"
        ),

        row=1,
        col=1
    )

    fig.add_trace(

        go.Bar(
            x=df["Date"],
            y=df["Phishing_Attempts"],
            name="Phishing"
        ),

        row=1,
        col=2
    )

    fig.add_trace(

        go.Bar(
            x=df["Date"],
            y=df["Blocked_Phishing"],
            name="Blocked"
        ),

        row=1,
        col=2
    )

    fig.add_trace(

        go.Scatter(
            x=df["Date"],
            y=df["Critical_Vulnerabilities"],
            name="Critical"
        ),

        row=2,
        col=1
    )

    fig.add_trace(

        go.Scatter(
            x=df["Date"],
            y=df["Financial_Risk_Score"],
            name="Financial"
        ),

        row=2,
        col=2
    )

    fig.add_trace(

        go.Scatter(
            x=df["Date"],
            y=df["Active_Incidents"],
            name="Incidents"
        ),

        row=3,
        col=1
    )

    fig.add_trace(

        go.Scatter(
            x=df["Date"],
            y=df["Security_Posture_Score"],
            name="Posture"
        ),

        row=3,
        col=2
    )

    fig.update_layout(

        height=950,
        width=1150,

        title=
        "SentinelAI Cybersecurity Intelligence Dashboard",

        template="plotly_white"

    )

    return fig

# ============================================================
# AGENT STATE
# ============================================================

class SentinelState(TypedDict):

    input: str

    metrics: dict

    anomalies: dict

    risk: dict

    dashboard_html: str

    analysis: str

    decision: str

    action_report: str

# ============================================================
# AGENT 1
# KPI AGENT
# ============================================================

def metrics_step(state):

    metrics = {

        "Average Risk":
            round(df["Overall_Cyber_Risk"].mean(),2),

        "Average Posture":
            round(df["Security_Posture_Score"].mean(),2),

        "Average Phishing":
            round(df["Phishing_Attempts"].mean(),2),

        "Average MTTR":
            round(df["MTTR"].mean(),2)
    }

    return {
        "metrics": metrics
    }

# ============================================================
# AGENT 2
# ANOMALY
# ============================================================

def anomaly_step(state):

    anomalies = df[
        df["Overall_Cyber_Risk"]
        >
        df["Overall_Cyber_Risk"].mean() * 1.5
    ]

    return {

        "anomalies": {

            "count":
                len(anomalies),

            "records":

                anomalies.head(
                    10
                ).to_dict(
                    orient="records"
                )
        }

    }

# ============================================================
# AGENT 3
# RISK
# ============================================================

def risk_step(state):

    top_risk = (

        df.sort_values(
            "Overall_Cyber_Risk",
            ascending=False
        )

        .head(10)
    )

    return {

        "risk": {

            "top_risk":
                top_risk.to_dict()
        }
    }

# ============================================================
# AGENT 4
# DASHBOARD
# ============================================================

def dashboard_step(state):

    dashboard_html = (

        create_dashboard()

        .to_html(

            full_html=False,

            include_plotlyjs="cdn"
        )

    )

    return {

        "dashboard_html":
            dashboard_html
    }

# ============================================================
# AGENT 5
# GEMINI ANALYSIS
# ============================================================

def analysis_step(state):

    prompt = f"""

You are SentinelAI.

Metrics:
{json.dumps(state['metrics'],indent=2)}

Risk:
{json.dumps(state['risk'],indent=2)}

Anomalies:
{json.dumps(state['anomalies'],indent=2)}

Provide:

1 Threat Assessment

2 Root Cause

3 Risk Severity

4 Recommended Actions

5 Executive Summary

"""

  try:

    result = llm.invoke(
        prompt
    )

    analysis = (
        result.content
    )

except Exception as e:

    analysis = (
        f"Analysis Failed: {e}"
    )

return {

    "analysis":
        analysis

}

# ============================================================
# AGENT 6
# DECISION
# ============================================================

def decision_step(state):

    text = (
        state["analysis"]
        .lower()
    )

    if (

        "critical" in text
        or
        "breach" in text
        or
        "high" in text

    ):

        decision = (
            "Escalate to SOC Team"
        )

    else:

        decision = (
            "Continue Monitoring"
        )

    return {

        "decision": decision
    }

# ============================================================
# AGENT 7
# RESPONSE
# ============================================================

def action_step(state):

    report = f"""

Decision:
{state['decision']}

Recommended Actions

• Investigate phishing surges

• Review API exposures

• Patch critical vulnerabilities

• Reduce MTTR

• Improve posture score

• Validate suspicious transactions

"""

    return {

        "action_report":
            report
    }

# ============================================================
# LANGGRAPH
# ============================================================

builder = StateGraph(SentinelState)

builder.add_node(
    "metrics",
    metrics_step
)

builder.add_node(
    "anomaly",
    anomaly_step
)

builder.add_node(
    "risk",
    risk_step
)

builder.add_node(
    "dashboard",
    dashboard_step
)

builder.add_node(
    "analysis",
    analysis_step
)

builder.add_node(
    "decision",
    decision_step
)

builder.add_node(
    "action",
    action_step
)

builder.set_entry_point("metrics")

builder.add_edge(
    "metrics",
    "anomaly"
)

builder.add_edge(
    "anomaly",
    "risk"
)

builder.add_edge(
    "risk",
    "dashboard"
)

builder.add_edge(
    "dashboard",
    "analysis"
)

builder.add_edge(
    "analysis",
    "decision"
)

builder.add_edge(
    "decision",
    "action"
)

builder.add_edge(
    "action",
    END
)

agent_app = builder.compile()

# ============================================================
# FASTAPI
# ============================================================

app = FastAPI()

# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "platform": "SentinelAI"
    }

@app.get("/health")
...
@app.get("/mcp/status")
....
@app.get("/export/report")
...
@app.get("/")
def home():

    return HTMLResponse("""

    <h1>
# ==================================================
# MCP Server Endpoint.
# ==================================================

@app.get("/mcp/status")
def mcp_status():

    return {

        "mcp_enabled":
            MCP_ENABLED,

        "server":

            "connected"

            if mcp_server

            else

            "disabled"

    }

# ============================================================
# Report Status.
# ============================================================

@app.get("/export/report")
def export_report():

    report = {
        "platform":
            "SentinelAI",

        "system":
            "Cybersecurity Intelligence",

        "status":
            "Operational"
    }

    return {

        "base64_report":

            encode_report(
                report
            )

    }

# ============================================================
# DASHBOARD
# ============================================================

@app.get("/dashboard")
def dashboard():

    html = (

        create_dashboard()

        .to_html(
            full_html=True,
            include_plotlyjs="cdn"
        )
    )

    return HTMLResponse(html)

# ============================================================
# AGENT API
# ============================================================

# ============================================================
# AGENT API
# ============================================================

@app.post("/agent")
def run_agent(
    prompt: str = Body(...)
):

    result = agent_app.invoke({

        "input": prompt,

        "metrics": {},

        "anomalies": {},

        "risk": {},

        "dashboard_html": "",

        "analysis": "",

        "decision": "",

        "action_report": ""

    })

    result[
        "base64_report"
    ] = encode_report(
        result
    )

    trace_run(
        prompt,
        result
    )

    return result

# ============================================================
# AGENT UI
# ============================================================

@app.get("/agent-ui")

def agent_ui():

    return HTMLResponse("""

<html>

<body>

<h2>
SentinelAI Investigation Console
</h2>

<form method="post"
      action="/agent-ui">

<textarea
name="prompt"
rows="4"
style="width:100%;">
</textarea>

<br><br>

<button>
Run Full Investigation
</button>

</form>

</body>

</html>

""")

@app.get("/agent-ui")
def agent_ui():

    return HTMLResponse("""
    <html>
    <body>

    <h2>
    SentinelAI Investigation Console
    </h2>

    </body>
    </html>
    """)

# ============================================================
# LOCAL STARTUP
# ============================================================

if __name__ == "__main__":

 import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=int(
            os.getenv(
                "PORT",
                8000
            )
        )
    )
