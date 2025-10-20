import streamlit as st
import os
from onc import ONC
import pandas as pd

st.title("Oceans 3.0 Open API Playground")
st.metric("Web Services", 2, 1)

token = st.secrets["ONC_TOKEN"] #Pulls info from /.streamlit/secrets.toml
#token = os.getenv("ONC_TOKEN")
onc = ONC(token)

st.markdown(":blue-badge[GET] `/locations`")

location_code = st.text_input("locationCode", placeholder="FGPD")


if st.button("Run", key="location_button"):
    st.write(f"you input {location_code}")
    param = {"locationCode": location_code}
    location_info = onc.getLocations(param)
    st.json(location_info)
    #Location code does not show up here if just FGPD, because is just a place holder

st.divider()

st.header(":blue[Real-time Services]")

st.subheader(":green[Return archivefiles]")

st.markdown(":blue-badge[GET] `/archivefile`")

device_code = st.text_input("deviceCode", value="BPR_BC")
last_days = st.number_input("last days", value=4)

if st.button("Run", key="archivefile_button"):
    st.write(f"you input {device_code}")
    st.write(f"you input {last_days}")
    param = {
        "deviceCode": device_code,
        "dateFrom": f"-P{last_days}D",
        "returnOptions": "all",
    }
    archivefile = onc.getArchivefile(param)
    st.dataframe(pd.DataFrame(archivefile["files"]))


st.write(st.secrets)  #Pulls info from /.streamlit/secrets.toml