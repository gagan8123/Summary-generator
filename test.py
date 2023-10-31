import numpy as np
# from transformers import pipeline
# #from youtube_transcript_api import YouTubeTranscriptApi
# import urllib

# link = "https://en.wikipedia.org/wiki/Algorithm"
# text = urllib.request.urlopen(link)
# print(text.read().decode("utf-8"))



# def trym(l,c,zindx):
#     if c >= 6:
#         return -1
#     if 


l =[]
for i in range(2):
    l.append(list(int(x) for x in input().split(' ')))
    
arr = np.array(l)
print(arr.item())
# c = 0
# z = 0
# while True:
#     if '0' in l[0]:
#         z = [l[0].index('0'),0]
#     else:
#         z = [l[1].index('1'),1]
#     if l[0] ==['1','2','3'] and l[0] == ['4','5','0']:
#         print(c)
#         break
#     else:
#         print(l)
#         trym(l,c,z)
#     break
        
