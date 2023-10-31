
from  transformers import pipeline

from gtts import gTTS
import os
#D:\GaganFiles\django project\myproject\audio
#model="bert-base-uncased"
#model="facebook/bart-large-cnn"
#model = "t5-large" # t5-base, t5-large
class Summary:
    def __init__(self,text):
        self.text = text
        self.output = self.sumry()
    
    def sumry(self):
        pipesummary = pipeline("summarization",model="facebook/bart-large-cnn",use_fast=True)
        
        out =""
        le = len(self.text)
        l =0
        if le < 500:
            end = le
            b = 1 
        else:
            end = 500
            b = int(le/500)
        
        for i in range(0,b):
            st = self.text[l:end]
            if not(len(st) > 450):
                try:
                    out += st[st.index(" "):]
                except: 
                    out += st[st.index("."):]
                break
            print(out,"1")
            summary = pipesummary(st)[0]["summary_text"]
            out += summary
            l = end 
            end = end + 500
            if le >= end:
                continue
            else:
                end = le
        
        let =int(len(os.listdir("static")))+1
        speech = gTTS(text=out,lang_check=False)
        speech.save(f"static/text{let}.mp3")
        
        
        return [out,f"static/text{let}.mp3"]
        
        
