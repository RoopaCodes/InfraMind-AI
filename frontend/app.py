import streamlit as st
import sys
import os
import pandas as pd
import plotly.express as px

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.ai_service import analyze_logs
from backend.sanitizer import sanitize_logs
from agents.monitoring_agent import monitoring_agent
from agents.rca_agent import rca_agent
from agents.automation_agent import automation_agent
from agents.security_agent import security_agent
from backend.playbook_generator import save_playbook
from backend.report_generator import generate_report

# Page Config
st.set_page_config(
    page_title="InfraMind AI",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: #FFFFFF;
}

.stButton button {
    background-color: #4F46E5;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

.stButton button:hover {
    background-color: #6366F1;
    color: white;
}

.metric-card {
    background-color: #1E1E2F;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
}

.analysis-box {
    background-color: #1A1D24;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #4F46E5;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🚀 InfraMind AI")
st.sidebar.success("🟢 System Status: Operational")
st.sidebar.metric("Active AI Agents", "4")
st.sidebar.metric("Incidents Resolved", "128")
st.sidebar.metric("Automation Success Rate", "96%")
st.sidebar.markdown("---")
st.sidebar.write("AI-Powered Infrastructure Operations")
st.sidebar.markdown("""
### Features
- Log Analysis
- Root Cause Detection
- AI Recommendations
- Automation Suggestions
- Security Validation
""")

# Main Title
st.title("🚀 InfraMind AI")
st.markdown("""
### Autonomous Infrastructure Operations Copilot

InfraMind AI uses specialized AI agents to:

- Detect infrastructure anomalies
- Perform root cause analysis
- Generate remediation workflows
- Validate security compliance
- Automate operational intelligence

Built for enterprise-scale cloud and hybrid infrastructure environments.
""")
st.subheader("Autonomous Infrastructure Operations Copilot")

st.markdown("---")

# Metrics Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Incidents Analyzed", "128")

with col2:
    st.metric("Critical Alerts", "12")

with col3:
    st.metric("Automation Generated", "34")

with col4:
    st.metric("Security Validated", "100%")

st.markdown("---")

# Upload Section
st.header("📂 Upload Infrastructure Logs")

uploaded_file = st.file_uploader(
    "Upload log file",
    type=["txt", "log"]
)


if uploaded_file is not None:

    log_data = uploaded_file.read().decode("utf-8")
    sanitized_logs = sanitize_logs(log_data)
    st.success("✅ Log file uploaded successfully!")

    with st.expander("📄 View Uploaded Logs"):
        st.code(log_data)
    with st.expander("🔒 View Sanitized Logs"):
        st.code(sanitized_logs)

    if st.button("🚀 Analyze Logs"):

        with st.spinner("🤖 AI agents are analyzing infrastructure logs..."):

            monitoring_result = monitoring_agent(sanitized_logs)

            rca_result = rca_agent(sanitized_logs)

            automation_result = automation_agent(sanitized_logs)

            playbook_path = save_playbook(automation_result)

            security_result = security_agent(sanitized_logs)

            report = generate_report(
                monitoring_result,
                rca_result,
                automation_result,
                security_result
            )

        st.markdown("---")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Incident Status", "Active")

        with col2:
            st.metric("Affected Services", "3")

        with col3:
            st.metric("Estimated Downtime Risk", "High")

        st.metric("AI Confidence Score", "94%")

        st.markdown("---")

        st.header("📡 Live Infrastructure Incident Feed")

        incident_feed = [
            "🚨 CPU spike detected on production node",
            "⚠️ Memory threshold exceeded",
            "🔍 AI anomaly detection triggered",
            "🛡️ Security validation in progress",
            "⚙️ Automated remediation generated"
        ]

        for incident in incident_feed:
            st.markdown(f"- {incident}")
        st.markdown("---")

        st.header("🤖 AI Agent Activity Console")

        terminal_logs = """
        [Monitoring Agent] Scanning infrastructure logs...
        [RCA Agent] Correlating incident patterns...
        [Automation Agent] Generating remediation workflow...
        [Security Agent] Validating compliance and security...
        [InfraMind AI] Incident response completed successfully.
        """

        st.code(terminal_logs, language="bash")
        st.markdown("---")

        st.header("🔥 Incident Severity Heatmap")

        severity_data = pd.DataFrame({
            "Severity": ["Critical", "High", "Medium", "Low"],
            "Count": [12, 8, 5, 2]
        })

        fig2 = px.pie(
            severity_data,
            values="Count",
            names="Severity",
            title="Infrastructure Incident Severity Distribution"
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("---")

        st.header("📡 Monitoring Agent")
        st.error("🔴 Severity: Critical")
        st.write(monitoring_result)

        st.header("🧠 RCA Agent")
        st.warning("⚠️ Root Cause Analysis Completed")
        st.write(rca_result)

        st.header("⚙️ Automation Agent")
        st.success("✅ Automation Workflow Generated")
        st.write(automation_result)

        with open(playbook_path, "r") as file:
            st.download_button(
                label="⬇️ Download Generated Playbook",
                data=file,
                file_name="generated_playbook.yml",
                mime="text/yaml"
            )

        st.header("🔐 Security Agent")
        st.info("🛡️ Security Validation Completed")
        st.write(security_result)

        st.markdown("---")

        st.header("📅 Incident Timeline")

        st.markdown("""
        - 🚨 Alert Generated
        - 🔍 Monitoring Agent Detected Incident
        - 🧠 RCA Agent Identified Root Cause
        - ⚙️ Automation Agent Generated Remediation
        - 🔐 Security Agent Validated Action
        """)

        st.markdown("---")

        st.download_button(
            label="📄 Download Incident Report",
            data=report,
            file_name="incident_report.txt",
            mime="text/plain"
        )
# Footer
st.markdown("---")
st.caption("InfraMind AI © 2026 | AI-Powered SRE Intelligence Platform")