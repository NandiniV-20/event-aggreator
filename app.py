import streamlit as st
import pandas as pd
from db import SessionLocal, Event
from pipeline import run_pipeline

st.set_page_config(page_title="Event Aggregator",layout="wide")

st.title("🌍Event Aggregator Dashboard")
st.write("Internships | Hackathons | Challenges")

if st.button("🔄 Refresh Events"):
    run_pipeline()
    st.success("Events refreshed!")
    
db=SessionLocal()
events = db.query(Event).all()
db.close()

if events:
    df=pd.DataFrame([{
        "Title":e.title,
        "Source":e.source,
        "Category":e.category,
        "Location":e.location,
        "Date":e.date,
        "Link":e.link  
    }for e in events])
    
    category= st.sidebar.multiselect("Filter by Category", df["Category"].unique())
    if category:
        df= df[df["Category"].isin(category)]
        
    st.dataframe(df,use_container_width=True)
    
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇ Download CSV",csv,"events.csv","text/csv")
else:
    st.warning("No events yet. Try refreshing!")
    