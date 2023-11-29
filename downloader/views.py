from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import yt_dlp

@csrf_exempt
def download_audio(request):

    if request.method == 'POST':
        url = request.POST.get('url')
        video_name = request.POST.get('video_name')
        format_choice = request.POST.get('format_choice')

        print(f"url: {url}, video_name: {video_name}, format_choice: {format_choice}")

        ydl_opts = {
            'format': format_choice + '/bestaudio/best',
            "ignoreerrors": True,
            "outtmpl": {
                "default": f"media/%(title)s.%(ext)s",
            },
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": format_choice,
             }, ],
           #     "prefer_ffmpeg": True,
        }
        if "youtube" in url or "youtu.be" in url:
            # Si playlist change le template d'output
            if "playlist" in url:
                ydl_opts.update({"outtmpl": "%(playlist)s/%(uploader)s/%(title)s.%(ext)s"})

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})