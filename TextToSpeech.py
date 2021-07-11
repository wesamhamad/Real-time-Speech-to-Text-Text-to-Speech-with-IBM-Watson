
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


apikey = 'yLlsRPdRzYZn5_NCieIzVR198v92K4f6HDPRxZIAFzml'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/23939e8f-468c-4f3d-8eb5-8760b7d7033e'

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)


with open('note.txt', 'r') as f:
    text = f.readlines()
    text = [line.replace('\n', '') for line in text]
    text = ''.join(str(line) for line in text)


with open('./sound.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)


    