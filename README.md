## Sentinel AI Multi-Surface-Threat-Detection Security Dashboard

## Objective:

SentinelAI is an AI-powered multi-surface threat detection and security dashboard that monitors emails for phishing attacks, analyses banking activity for fraud and anomalies, scans devices and websites for security risks, and correlates threats across all digital surfaces. Through a Plotly powered unified dashboard, users can track key cybersecurity KPIs and metrics including a 98.5% Threat Detection Rate, 95% Phishing Detection Accuracy, 12,500+ Emails analyzed, 320 Phishing Attempts Blocked, 92/100 Security Posture Score, 87/100 Financial Risk Score, 45 Vulnerabilities Identified, 99.2% Asset Monitoring Coverage, 2.3-minute Mean Time to Detect (MTTD), 8.7-minute Mean Time to Respond (MTTR), and an overall 18/100 Cyber Risk Rating. Agentic AI workflows automatically investigate alerts, prioritise incidents, and generate remediation recommendations, while a browser-based JavaScript and HTML 3D visualization engine provides an interactive view of relationships between emails, financial accounts, devices, websites, and cyber threats. SentinelAI functions as a personal Security Operations Centre (SOC), delivering real-time visibility, automated threat analysis, and proactive cyber defence from a single intelligent dashboard.

## Key Features:

SentinelAI combines AI-powered phishing detection, financial anomaly monitoring, device and web security scanning, and agentic AI workflows into a unified security platform. The system correlates threats across emails, financial accounts, devices, and websites, providing real-time insights through an interactive Plotly dashboard with cybersecurity KPIs and risk metrics. Users can visualise threat relationships, monitor security posture, investigate incidents, and receive AI-driven recommendations through an intuitive browser-based dashboard and 3D threat visualisation experience.

## Dashboard:

The SentinelAI dashboard provides a unified, real-time view of cybersecurity and financial risk across emails, devices, websites, and financial accounts. Built with Plotly and JavaScript, the dashboard displays interactive KPIs and analytics including Threat Detection Rate, Phishing Attempts Blocked, Financial Risk Score, Security Posture Score, Vulnerabilities Detected, Active Incidents, MTTD, and MTTR. Users can explore threat trends, monitor system health, visualise attack correlations, and investigate security events through dynamic charts, risk heatmaps, and an interactive 3D threat map, enabling faster and more informed security decisions.

## JavaScript/HTML User Interface:

The application features a responsive browser-based interface built with JavaScript, HTML, and modern web technologies to deliver real-time security monitoring and threat visualization. The platform includes interactive dashboards, dynamic security analytics, and a 3D threat visualisation engine that enables users to explore relationships between emails, financial accounts, devices, websites, and detected threats. Through an intuitive user experience, users can monitor KPIs, investigate security incidents, analyse attack trends, and receive AI-generated recommendations from a single web-based security operations dashboard.

## Plotly Dashboard:

The application will use Plotly to provide  a real-time view of cybersecurity and financial risk by monitoring phishing emails, suspicious transactions, device vulnerabilities, website security issues, and active security incidents. Through interactive charts, KPI cards, risk scores, and threat analytics, users can track key metrics such as Threat Detection Rate, Phishing Attempts Blocked, Financial Risk Score, Security Posture Score, Vulnerabilities Detected, MTTD, and MTTR. The dashboard enables users to visualize trends, investigate threats, and gain actionable insights from a single unified security platform.

## Chain, LangGraph & LangSmith:

SentinelAI leverages LangChain, LangGraph, and LangSmith to power its agentic AI workflows and autonomous threat investigation capabilities. LangChain orchestrates interactions between large language models, security tools, and external data sources, while LangGraph manages multi-step security workflows such as phishing analysis, fraud investigation, threat correlation, and incident response. LangSmith provides observability, debugging, evaluation, and performance monitoring for AI agents, enabling continuous improvement of threat detection accuracy and workflow reliability. Together, these technologies allow SentinelAI to automate security investigations, correlate threats across emails, financial accounts, devices, and websites, and generate intelligent, context-aware security recommendations through a scalable AI-driven architecture.

## Key Installation:

- Python

- JavaScript

- HTML

- Plotly

- JSON

- LangChain

- LangGraph

- LangSmith

- Gemini 3.6 flash

- MCP Server

- Render

## Deployment of Render:

The application is to deploy on Render using a lightweight cloud-native architecture that hosts a browser-based JavaScript and HTML security dashboard alongside and FastAPI. The platform delivers real-time threat monitoring, security analytics, and AI-powered threat investigations through interactive Plotly visualizations and 3D threat mapping. Render provides automated deployment, secure API hosting, scalability, and continuous delivery, enabling users to monitor email security events, financial anomalies, device vulnerabilities, and web security risks through a unified Security Operations Centre dashboard.

## Installation & Deployment Steps (Render):

- Log in to Render

- Click New → Web Service

- Select your project repo

## Configure the Web Service:

- Runtime: Python

## Build Command: 

- `pip install -r requirements.txt`

## Start Command:

- `uvicorn app:app --host 0.0.0.0 --port 10000`

## Environment Variables:

- Gemini API Key
  
- LangSmith API Key
  
## Add a Background Worker (Agentic AI Workflows):

- Service Type: Background Worker

## Start Command:

- `python agent_loop.py`

## Frontend:

- Browser-based HTML, JavaScript, and Plotly dashboards for security monitoring, KPI visualization, and threat analytics.

## Deploy:

- Render automatically builds and deploys the application on every GitHub push.

-   A public URL is generated for the SentinelAI dashboard and FastAPI endpoints.
  
- The platform provides real-time threat monitoring, AI-powered investigations, and interactive cybersecurity visualisations through a unified Security Operations Centre      (SOC) interface.

## LangChain, LangGraph & LangSmith Integration:

SentinelAI integrates LangChain, LangGraph, and LangSmith to enable intelligent, agentic cybersecurity workflows. LangChain connects the Gemini model with security data sources, analysis tools, and threat intelligence pipelines, while LangGraph orchestrates multi-step workflows for phishing detection, financial anomaly analysis, risk assessment, incident investigation, and threat correlation. LangSmith provides monitoring, debugging, evaluation, and tracing capabilities for AI agents, allowing security workflows to be tested, optimized, and monitored for reliability. Together, these technologies enable SentinelAI to automate threat analysis, generate security insights, and deliver context-aware recommendations through an AI-powered Security Operations Centre (SOC) dashboard

## Each Node:

- Email Threat Analysis Node: Analyses incoming emails from my gmail for phishing attempts, malicious links, suspicious attachments, and social engineering indicators,        generating a threat score and recommended actions.

- Financial Anomaly Detection Node: Monitors financial transaction data to identify unusual spending patterns, high\-risk transactions, and potential fraud activities.
  
- Device Security Monitoring Node: Evaluates device health, security configurations, vulnerabilities, and suspicious activity to determine overall device risk.
  
- Web Security Scanning Node: Assesses website security posture, detects vulnerabilities, reviews SSL/TLS status, and identifies potential web based threats.
  
- Threat Correlation Node: Aggregates findings from email, financial, device, and web security nodes to identify attack patterns and calculate an overall cyber risk score.
  
- Risk Assessment Node: Prioritizes incidents based on severity, impact, confidence scores, and business rules to support effective decision making.
  
- AI Recommendation Node: Uses Gemini to generate incident summaries, mitigation strategies, and actionable security recommendations.
  
- Dashboard Reporting Node: Sends KPIs, alerts, risk scores, and threat intelligence to the Plotly dashboard for real\-time visualisation and monitoring.

## Fallback Logic: 

SentinelAI implements fallback logic to ensure reliable threat analysis and incident processing. If an AI model, data source, or security service is unavailable, the system automatically switches to alternative analysis workflows, cached security data, or rule-based detection methods to maintain continuous monitoring. This resilience ensures that phishing detection, financial anomaly analysis, threat correlation, and security recommendations remain operational even during API failures, service interruptions, or unexpected processing errors.

## LangSmith - Observability, Tracing, and Evaluation:

SentinelAI uses LangSmith to provide comprehensive observability, tracing, and evaluation for its AI-powered security workflows. LangSmith tracks every agent decision, tool invocation, and workflow execution across phishing detection, financial anomaly analysis, threat correlation, and incident investigations, enabling complete visibility into the system's behaviour. Detailed traces help identify performance bottlenecks, debugging issues, and workflow failures, while evaluation metrics measure response quality, threat detection accuracy, and overall agent effectiveness. This observability layer ensures that SentinelAI's AI agents remain reliable, transparent, and continuously optimised for cybersecurity operations.

## Function of the Agent:

- The word is analyze to function the AI agent (Gemini 3.6 flash) for the website.

## How This Fits the Project:

The application uses Gemini 3.6 Flash serves as the core intelligence engine of SentinelAI, integrating with LangChain, LangGraph, and LangSmith to automate cybersecurity analysis and investigation workflows. The agent analyses email threats, financial anomalies, device vulnerabilities, and web security risks, correlates findings across multiple security surfaces, calculates risk scores, and generates actionable recommendations. These insights are then visualized through the Plotly dashboard, enabling users to monitor KPIs, investigate incidents, and gain a unified view of their overall cybersecurity posture from a single Security Operations Centre (SOC) platform.
  








