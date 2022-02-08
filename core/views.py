from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateResponseMixin, View
import youtube_dl

from core.constants import itag_to_format

def convert_bytes(size):
    if not size:
        return 0
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size

class HomeView(View, TemplateResponseMixin):
    template_name = 'home.html'

    def get_video_context(self, url):
        ydl_opts = {}
        result = None
        audio_formats = []
        video_formats = []
        audio_video_formats = []
        not_valid_format = []

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)
            for frmt in result['formats']:
                frmt['h_size'] = convert_bytes(frmt['filesize'])
                # format_id = frmt['format_id']
                # format = itag_to_format.get(format_id, None)
                # if not format:
                #     not_valid_format.append(frmt)
                if frmt['vcodec'] != 'none' and frmt['acodec'] != 'none':
                    audio_video_formats.append(frmt)
                elif frmt['acodec'] != 'none':
                    audio_formats.append(frmt)
                elif frmt['vcodec'] != 'none':
                    video_formats.append(frmt)

        context = {
            "result": result,
            "url": url,
            "audio_formats": audio_formats,
            "video_formats": video_formats,
            "audio_video_formats": audio_video_formats
        }
        return context

    def get(self, request):
        context = {}
        url = request.GET.get('youtube_url', None)
        if url:
            context = self.get_video_context(url)
        return self.render_to_response(context)
