import tempfile
import gradio as gr
import openai
from neon_tts_plugin_coqui import CoquiTTS

def Question(Ask_Question):
  # pass the generated text to audio
  openai.api_key = "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"
  # Set up the model and prompt
  model_engine = "text-davinci-003"
  #prompt = "who is alon musk?"
  # Generate a response
  completion = openai.Completion.create(
  engine=model_engine,
  prompt=Ask_Question,
  max_tokens=1024,
  n=1,
  stop=None,
  temperature=0.5,)
  response = completion.choices[0].text
  #out_result=resp['message']
  return  response

LANGUAGES = list(CoquiTTS.langs.keys())
default_lang = "en"
import telnetlib
#import whisper
#whisper_model = whisper.load_model("small")
whisper = gr.Interface.load(name="spaces/sanchit-gandhi/whisper-large-v2")
#chatgpt = gr.Blocks.load(name="spaces/fffiloni/whisper-to-chatGPT")
import os
import json
session_token = os.environ.get('SessionToken')
#api_endpoint = os.environ.get('API_EndPoint')
# ChatGPT
#from revChatGPT.ChatGPT import Chatbot
#chatbot = Chatbot({"session_token": session_token}) # You can start a custom conversation
import asyncio
from pygpt import PyGPT

title = "Speech to ChatGPT to Speech"
#info = "more info at [Neon Coqui TTS Plugin](https://github.com/NeonGeckoCom/neon-tts-plugin-coqui), [Coqui TTS](https://github.com/coqui-ai/TTS)"
#badge = "https://visitor-badge-reloaded.herokuapp.com/badge?page_id=neongeckocom.neon-tts-plugin-coqui"
coquiTTS = CoquiTTS()
chat_id = {'conversation_id': None, 'parent_id': None}
headers = {'Authorization': 'yusin'}

async def chat_gpt_ask(prompt):
    chat_gpt = PyGPT(session_token)
    await chat_gpt.connect()
    await chat_gpt.wait_for_ready()
    answer = await chat_gpt.ask(prompt)
    print(answer)
    await chat_gpt.disconnect()

# ChatGPT
def chat_hf(audio, custom_token, language):
    #output = chatgpt(audio, "transcribe", fn_index=0)
    #whisper_text, gpt_response = output[0], output[1]
    try:
        whisper_text = translate(audio)
        if whisper_text == "ERROR: You have to either use the microphone or upload an audio file":
            gpt_response = "MISSING AUDIO: Record your voice by clicking the microphone button, do not forget to stop recording before sending your message ;)"
        else:
            #gpt_response = chatbot.ask(whisper_text, conversation_id=conversation_id, parent_id=None)
            gpt_response = asyncio.run(chat_gpt_ask(whisper_text, id='yusin'))
            #if chat_id['conversation_id'] != None:
            #    data = {"content": whisper_text, "conversation_id": chat_id['conversation_id'], "parent_id": chat_id['parent_id']}
            #else: 
            #    data = {"content": whisper_text}
            #print(data)
            #res = requests.get('http://myip.ipip.net', timeout=5).text
            #print(res)
            #response = requests.post('api_endpoint', headers=headers, json=data, verify=False, timeout=5)
            #print('this is my answear', response.text)
            #chat_id['parent_id'] = response.json()["response_id"]
            #chat_id['conversation_id'] = response.json()["conversation_id"]
            #gpt_response = response.json()["content"]
            #response = requests.get('https://api.pawan.krd/chat/gpt?text=' + whisper_text + '&cache=false', verify=False, timeout=5)
            #print(response.text)
        
        #whisper_text = translate(audio)
        #api = ChatGPT(session_token) 
        #resp = api.send_message(whisper_text)
        
        #api.refresh_auth()  # refresh the authorization token
        #api.reset_conversation()  # reset the conversation
        #gpt_response = resp['message']

    except:
        whisper_text = translate(audio)
        gpt_response = """Sorry, I'm quite busy right now, but please try again later :)"""
        #whisper_text = translate(audio)
        #api = ChatGPT(custom_token) 
        #resp = api.send_message(whisper_text)
        
        #api.refresh_auth()  # refresh the authorization token
        #api.reset_conversation()  # reset the conversation
        #gpt_response = resp['message']

    ## call openai
        gpt_response = Question(whisper_text)
    
    # to voice
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
        coquiTTS.get_tts(gpt_response, fp, speaker = {"language" : language})
    
    return whisper_text, gpt_response, fp.name

# whisper
#def translate(audio):
#    print("""
#    —
#    Sending audio to Whisper ...
#    —
#    """)
#    
#    audio = whisper.load_audio(audio)
#    audio = whisper.pad_or_trim(audio)
#    
#    mel = whisper.log_mel_spectrogram(audio).to(whisper_model.device)
#    
#    _, probs = whisper_model.detect_language(mel)
#    
#    transcript_options = whisper.DecodingOptions(task="transcribe", fp16 = False)
#    
#    transcription = whisper.decode(whisper_model, mel, transcript_options)
#    
#    print("language spoken: " + transcription.language)
#    print("transcript: " + transcription.text)
#    print("———————————————————————————————————————————")  
#      
#    return transcription.text

def translate(audio):
    print("""
    —
    Sending audio to Whisper ...
    —
    """)
   
    text_result = whisper(audio, None, "transcribe", fn_index=0)
    #print(text_result)
    return text_result


with gr.Blocks() as blocks:
    gr.Markdown("<h1 style='text-align: center; margin-bottom: 1rem'>"
                + title
                + "</h1>")
    #gr.Markdown(description)
    radio = gr.Radio(label="Language",choices=LANGUAGES,value=default_lang)
    with gr.Row(equal_height=True):# equal_height=False
        with gr.Column():# variant="panel"
            audio_file = gr.Audio(source="microphone",type="filepath")
            custom_token = gr.Textbox(label='If it fails, use your own session token', placeholder="your own session token")
            with gr.Row():# mobile_collapse=False
                submit = gr.Button("Submit", variant="primary")
        with gr.Column():
            text1 = gr.Textbox(label="Speech to Text")
            text2 = gr.Textbox(label="ChatGPT Response")
            audio = gr.Audio(label="Output", interactive=False)
    #gr.Markdown(info)
    #gr.Markdown("<center>"
    #            +f'<img src={badge} alt="visitors badge"/>'
    #            +"</center>")

    # actions
    submit.click(
        chat_hf,
        [audio_file, custom_token, radio],
        [text1, text2, audio],
    )
    radio.change(lambda lang: CoquiTTS.langs[lang]["sentence"], radio, text2)


blocks.launch(debug=True)


Apollo
