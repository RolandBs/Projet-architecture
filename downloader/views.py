from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import yt_dlp

@csrf_exempt
def download_audio(request):

    if request.method == 'POST':
        url = request.POST.get('url')
        format_choice = request.POST.get('format_choice')
        install_path = request.POST.get('install_path')

        ydl_opts = {
            'format': format_choice+'/bestaudio/best',
            "ignoreerrors": True,
            "outtmpl": {
                "default": f"{install_path}/%(title)s.%(ext)s",
            },
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": format_choice,
                }, ],
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