from pytube import YouTube


with open('IO/songs.txt') as f:
    lines = f.readlines()

for line in lines:
    try:
        yt = YouTube(line)
        yt.streams.get_audio_only().download(filename=f'{yt.title}.mp3', output_path='songs/')
    except:
        with open('IO/errors.txt', 'w') as e:
            e.write(f'ERROR ON: {line}')