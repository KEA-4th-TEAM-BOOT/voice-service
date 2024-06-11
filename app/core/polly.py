import boto3
from app.schemas.post import Post

def polly_voice(post: Post):
    text = f'{post.title}\n{post.content}'

    client = boto3.client('polly')

    response = client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Seoyeon'
    )

    mp3 = f'app/voices/mp3/{post.post_id}.mp3'

    if "AudioStream" in response:
        with open(mp3, "wb") as file:
            file.write(response['AudioStream'].read())
        print("Audio file saved")
    else:
        print("Could not stream audio")

    return mp3