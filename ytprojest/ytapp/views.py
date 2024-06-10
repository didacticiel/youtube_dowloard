from django.shortcuts import render
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

def youtube(request):
    if request.method == 'POST':
        link = request.POST['link']
        try:
            video = YouTube(link)
            stream = video.streams.get_lowest_resolution()
            stream.download()
            message = "Video successfully downloaded."
        except AgeRestrictedError:
            message = "The video is age restricted and cannot be downloaded without logging in."
        except Exception as e:
            message = f"An error occurred: {str(e)}"
        
        return render(request, 'youtube.html', {'message': message})
    return render(request, 'youtube.html')
