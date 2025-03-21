import streamlit as st
import openai
import pandas as pd

# Set OpenAI API Key (Use Free Tier API)
openai.api_key = "your-openai-api-key"

# Sidebar for Navigation
st.sidebar.title("GenAI Integrated Platform")
page = st.sidebar.radio("Navigation", ["Dashboard", "AI Chatbot", "Incident Automation", "Telemetry Insights"])

# Sample Incident Data (Simulated)
incident_data = pd.DataFrame({
    "Incident ID": ["INC1001", "INC1002", "INC1003"],
    "Status": ["Open", "Resolved", "In Progress"],
    "Priority": ["High", "Medium", "Critical"],
    "Summary": ["Database latency issue", "API failure in production", "Memory leak detected"]
})

# **1. Dashboard Page**
if page == "Dashboard":
    st.title("📊 Incident Dashboard")
    st.write("This dashboard shows live incidents from the integrated platform.")
    st.dataframe(incident_data)

# **2. AI Chatbot**
elif page == "AI Chatbot":
    st.title("🤖 AI Chatbot for Incident Support")
    
    # Chatbot Interaction
    user_input = st.text_input("Ask about an incident:")
    if st.button("Get AI Response"):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write("💡 AI Response:", response["choices"][0]["message"]["content"])

# **3. Incident Automation**
elif page == "Incident Automation":
    st.title("⚙️ Incident Automation & Health Checks")
    
    # Simulated Automated Actions
    action = st.selectbox("Select Automation Task", ["Run Health Check", "Restart Service", "Fetch Logs"])
    
    if st.button("Execute"):
        st.success(f"✅ {action} executed successfully!")

# **4. Telemetry Insights**
elif page == "Telemetry Insights":
    st.title("📡 Telemetry & Observability Insights")
    st.write("Real-time system health metrics (simulated).")

    # Simulated Telemetry Data
    telemetry_data = pd.DataFrame({
        "Metric": ["CPU Usage", "Memory Usage", "Response Time"],
        "Value": ["75%", "3.2 GB", "200ms"]
    })
    st.table(telemetry_data)

