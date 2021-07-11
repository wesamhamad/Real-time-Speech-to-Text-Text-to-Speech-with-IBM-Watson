# Real-time Speech to Text & Text to Speech with IBM Watson 
![tts](https://user-images.githubusercontent.com/74800962/125203252-55e9a980-e280-11eb-8fe5-7f62ef2a89a1.png)

## Synopsis
This project consists of a python client that interacts with the IBM Watson Speech To Text  & Text To Speech service through its WebSockets interface. The client streams audio to the STT,  text to the TTS service and receives recognition hypotheses in real time. It can run N simultaneous recognition sessions.
## Prerequisites
1. Install [python](https://www.python.org/downloads/).
2. Sign up for an [IBM Cloud account](https://cloud.ibm.com/registration).
3.Click on [catalog](https://cloud.ibm.com/catalog/services/speech-to-text) and search for Speech to Text.
4. Create an instance of the Speech to Text service and get your credentials:
    * Go to the [Speech to Text page](https://cloud.ibm.com/catalog/services/speech-to-text) in the IBM Cloud Catalog.
    * Log in to your IBM Cloud account.
    * Click Create.
    * Click Show to view the service credentials.
    * Copy the apikey value.
    * Copy the url value.
    
## Installation
There are some dependencies that need to be installed for this script to work. It is advisable to install the required packages in a separate virtual environment. Certain packages have been observed to conflict with the package requirements for this script; in particular the package nose conflicts with these required packages. In order to interact with the STT & TTS service via WebSockets, it is necessary to install [pip](https://pip.pypa.io/en/stable/installing/), then write the following commands:
```
pip install -r requirements.txt
```
You also may need to write these commands f error occurs 
```
pip install pipwin
```
Then install pyaudio 
```
pipwin install pyaudio
```
Also, You need to install ibm_watson 
```
pip install ibm_watson
```

## Speech to Text 
* ### You need to change **apikey** and **region** base on yours in [speech.cfg] file
```
apikey = AHtCuEgG6MpKIcMa3b56RBwBIVcxGUCEtpiF_OPJvJyG
# Modify region based on where you provisioned your stt instance
region = us-south
```
* ### Define and initialize a global variable to store the fragment you record. 
```python
 global Notes
 Notes = data['results'][0]['alternatives'][0]['transcript']
```

* ### Then use the variable in your [transcribe.py] file.

``
NOTE:You need to create file.text to save the text comes.
``

 ```python
 # To save text comes from Notes variable into note.txt . 
    with open("note.txt", "w") as out :
     out.write(Notes)
     out.close()
```

* ### Finally, now you can run it with this command  
```
python TextToSpeech.py -t 
```
## Text TO Speech
### 1. Authenticate
* ### You need to change **apikey** and **region** base on yours in [TextToSpeech.py] file
```python
apikey = 'yLlsRPdRzYZn5_NCieIzVR198v92K4f6HDPRxZIAFzml'
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/23939e8f-468c-4f3d-8eb5-8760b7d7033e'
```
* ### import some dependencies from ibm_watson 
```python
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
```
* ### Setup Service 
```python
authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)
```
* ### Convert a text from file 
* ``
NOTE:You need to create file.mp3 to save the converted audio .
``

```python
with open('note.txt', 'r') as f:
    text = f.readlines()
    text = [line.replace('\n', '') for line in text]
    text = ''.join(str(line) for line in text)


with open('./sound.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
```

* ### Finally, now you can run it with this command  
``
NOTE: After -t you can specify the number of seconds to record here I choose 5 second .
``
```
 python transcribe.py -t 5
```

# Output 
### Expected Output
Once you run transcribe.py with a timeout value (-t) you'll get both incremental output as data comes back, as well as a final stitching of things together. The output will look something like this.
```python
PS C:\Users\wesam\Desktop\folder\T4.1\S-M_Task4.1> python transcribe.py -t 5
* recording
hope 
hope you 
hope you 
hope you 
hope you 
hope you 
hope you have
hope you have
hope you have a
hope you have an
hope you have an eye
hope you have a nice
hope you have a nice
hope you have a ninety
hope you have a ninety
hope you have a nice day
hope you have a nice day
hope you have a nice day
hope you have a nice day
hope you have a nice day
hope you have a nice day
hope you have a nice day
* done recording
```
### Output Sample
https://user-images.githubusercontent.com/74800962/125205547-779c5e00-e28b-11eb-8087-7bbf79a03c6b.mp4

## Learning references:
1. [Click here](https://www.youtube.com/watch?v=YCyuZM454_I)
2. [Click here](https://www.youtube.com/watch?v=YCyuZM454_I&t=14s)
3. [Click here](https://www.youtube.com/watch?v=8k8S5ruFAUs&t=528s)
4. [Click here](https://github.com/watson-developer-cloud)
