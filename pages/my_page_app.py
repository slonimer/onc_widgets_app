import streamlit as st

st.title('Hello, Streamlit! 👋')
st.write('Welcome to my :red[first] web app!')

st.divider()

st.header("Hey")

st.write("more")

st.badge('Highlighted')
st.badge('Highlighted',color = 'yellow')


with st.echo():
    st.write('echo')

# Can also use custom css within a streamlit app

st.divider()

st.header(":blue[Real-time Services]")

st.subheader(":green[Return archivefiles]")

st.markdown(":blue-badge[GET] `/archivefile`")

device_code = st.text_input("deviceCode", value="BPR_BC")
last_days = st.number_input("last days", value=4)

if st.button("Run", key="archivefile_button"):
    st.write(f"you input {device_code}")
    st.write(f"you input {last_days}")