from pydub import AudioSegment

def mp3_to_wav(src_file: str, post_id: int):
    dest_file = f'app/voices/wav/{post_id}.wav'
    sound = AudioSegment.from_mp3(src_file)
    sound.export(dest_file, format="wav")
    return dest_file