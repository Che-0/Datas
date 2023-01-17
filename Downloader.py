from pytube import YouTube

def Download(link):
  youtubObject = YouTube(link)
  #youtubObject = youtubObject.streams.get_highest_resolution()  <--video
  youtubObject = youtubObject.streams.get_audio_only()   # <--Audio
  try:  
    youtubObject.download()
  except:
    print("No se pudo k rnal")
  print("Descarga completa")

link = input("Link: ")
Download(link)