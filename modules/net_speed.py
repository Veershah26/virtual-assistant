import speedtest      #pip install speedtest-cli

st = speedtest.Speedtest()

def download_speed():
    down = round(st.download() / 10 ** 6, 2)
    return down

def upload_speed():
    up= round(st.upload() / 10 ** 6, 2)
    return up

def ping():
    servernames =[]
    st.get_servers(servernames)
    results=st.results.ping
    return results

#print(f"Download Speed is {download_speed()} MB/s")
#print(f"Uplaod Speed is {upload_speed()} MB/s")
#print(f"Ping is {ping()} ")