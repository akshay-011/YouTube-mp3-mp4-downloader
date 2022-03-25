class download(object):
    def __init__(self):
        pass
    @staticmethod   
    def download_mp3(link):
        import os
        from pytube import YouTube

        path = os.path.join(os.getcwd(), "medias")
        mp3 = YouTube(link)
        name = mp3.title + ".mp3"
        file = mp3.streams.get_audio_only()
        file.download(filename=name, output_path=path)
        return os.path.join(path, name)
    @staticmethod
    def download_mp4(link, resulution):
        import os
        from pytube import YouTube
        
        mp4 = YouTube(link)
        path = os.path.join(os.getcwd(), "medias")
        name = mp4.title + ".mp4"
        if resulution == "high":
            file = mp4.streams.get_highest_resolution()
        elif resulution == "low":
            file = mp4.streams.get_lowest_resolution()
        else:
            file = mp4.streams.filter(file_extension='mp4')
        file.download(filename=name, output_path=path)
        return os.path.join(path, name)