from onvif import ONVIFCamera

def get_rtsp_url(host, port, username, password):
    mycam = ONVIFCamera(host, port, username, password)
    media_service = mycam.create_media_service()
    profiles = media_service.GetProfiles()
    token = profiles[0].token
    req = media_service.create_type('GetStreamUri')
    req.ProfileToken = token
    req.StreamSetup = {'Stream': 'RTP-Unicast', 'Transport': {'Protocol': 'RTSP'}}
    stream_uri = media_service.GetStreamUri(req)
    return stream_uri.Uri

# Пример использования
rtsp_url = get_rtsp_url('192.168.202.61', 80, 'nepretimov_i', '625RjrDgeDhe')
print(f"RTSP URL: {rtsp_url}")