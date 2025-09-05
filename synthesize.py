import boto3
import sys

# Read text file
text = open('speech.txt').read()

# Create audio
polly = boto3.client('polly')
audio = polly.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId='Joanna')

# Upload to S3
s3 = boto3.client('s3')
s3.put_object(
    Bucket='polly-bucket-8',
    Key=f'polly-audio/{sys.argv[1]}',
    Body=audio['AudioStream'].read()
)

print('Done!')
