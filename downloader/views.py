from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import yt_dlp

@csrf_exempt
def download_audio(request):

    if request.method == 'POST':
        url = request.POST.get('url')
        video_name = request.POST.get('video_name')
        format_choice = request.POST.get('format_choice')

        ydl_opts = {
            'format': 'bestaudio/best',
            "ignoreerrors": True,
            "outtmpl": {
                "default": f"media/{video_name}.%(ext)s",
            },
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": format_choice,
                }, ],
            "prefer_ffmpeg": True,
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


# def download_yt(self):
#     # sample chapter video https://youtu.be/2F0G8LKvtnE
#
#     self.label_complete.configure(self, text="")
#     url = self.input_link.get()
#     ytpath = self.path.get()
#     # videotitle = None
#
#     # Parametres de youtube dl
#     ydl_opts = {
#         "format": 'bestaudio/best',
#         "ignoreerrors": True,
#         "outtmpl": {
#             "default": f"{ytpath}/%(uploader)s/%(title)s.%(ext)s",
#             "chapter": f"{ytpath}/%(title)s/%(section_title)s.%(ext)s"
#         },
#         "postprocessors": [
#             {
#                 "key": "FFmpegSplitChapters",
#                 "force_keyframes": False,
#             },
#             {
#                 "key": "FFmpegExtractAudio",
#                 "preferredcodec": self.format_option.get(),
#             }, ],
#         "prefer_ffmpeg": True,
#         "progress_hooks": [],
#         "chapter": True,
#         # "verbose": True, # Parametre pour avoir plus de details
#     }
#
#     # Verification si lien Youtube
#     if "youtube" in url or "youtu.be" in url:
#
#         # Si playlist change le template d'output
#         if "playlist" in url:
#             ydl_opts.update({"outtmpl": "%(playlist)s/%(uploader)s/%(title)s.%(ext)s"})
#
#         # Ajoute la fonction percent au progress hook
#         ydl_opts.update({"progress_hooks": [self.percent]})
#
#     # Verification si lien SoundCloud
#     if "soundcloud" in url:
#         pass
#
#     # Progress bar
#     self.pourcent = customtkinter.CTkLabel(self, text='0%')
#     self.pourcent.grid(row=2, column=2, padx=20, pady=10, sticky="ew")
#     self.progress_bar = customtkinter.CTkProgressBar(self)
#     self.progress_bar.set(0)
#     self.progress_bar.grid(row=2, column=0, padx=20, pady=10, columnspan=2, sticky="ew")
#
#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(url, download=False)
#             videotitle = info['title']
#             print(info)
#
#             ydl.download([url])
#
#             if info.get('chapters') is not None:
#                 self.convert_chapters(url, self.format_option.get(), ytpath, videotitle)
#
#             self.label_complete.configure(text="Téléchargement terminé", text_color="green")
#             print('Process finished !')
#
#     except Exception as e:
#         self.label_complete.configure(text=f"Erreur : {str(e)}", text_color="red")
#         print(f"Erreur : {str(e)}")
