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
apikey:
region: 
```
* ### Define and initialize a global variable to store the fragment you record. 
```

```
* ### Then use the variable in your [transcribe.py] file.

``
NOTE:You need to create file.text to save the text comes.
``
 ```

```
* ### Finally, now you can run it with this command  
```
```
## Text TO Speech
### 1. Authenticate
* ### You need to change **apikey** and **region** base on yours in [TextToSpeech.py] file
```
```
* ### import some dependencies from ibm_watson 
```

```
* ### Setup Service 
```
```
* ### Convert a text from file 

``
NOTE:You need to create file.mp3 to save the converted audio .
``

* ### Finally, now you can run it with this command  
```
```

# Output 

### Expected Output
Once you run transcribe.py with a timeout value (-t) you'll get both incremental output as data comes back, as well as a final stitching of things together. The output will look something like this.
```
```
### Output Sample


## Learning references:
1. [Click here](https://www.youtube.com/watch?v=YCyuZM454_I)
2. [Click here](https://www.youtube.com/watch?v=YCyuZM454_I&t=14s)
3. [Click here](https://www.youtube.com/watch?v=8k8S5ruFAUs&t=528s)
4. [Click here](https://github.com/watson-developer-cloud)
