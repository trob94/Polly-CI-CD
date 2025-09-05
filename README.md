# Polly-CI-CD
Using Polly to automate text to speech and pushing that through a pipeline
# Text-to-Speech CI/CD Pipeline



## Setup

### 1. AWS Setup
1. **Create S3 bucket**: Go to S3 console, create a bucket with any name
2. **Create IAM user**: Go to IAM → Users → Create user
3. **Add policy** to the user:
   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "polly:SynthesizeSpeech",
               "Resource": "*"
           },
           {
               "Effect": "Allow", 
               "Action": "s3:PutObject",
               "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"
           }
       ]
   }
   ```
4. **Create access keys**: IAM → Users → Your user → Security credentials → Create access key

### 2. GitHub Setup
1. **Add secrets**: Settings → Secrets and variables → Actions
   - `AWS_ACCESS_KEY_ID` = your access key
   - `AWS_SECRET_ACCESS_KEY` = your secret key
   - `AWS_REGION` = us-east-1
2. **Edit synthesize.py**: Change `polly-bucket-8` to your bucket name

### 3. Files Needed
```
your-repo/
├── .github/workflows/
│   ├── on_pull_request.yml
│   └── on_merge.yml
├── speech.txt
└── synthesize.py
```

## How to Use

### Modify Text
Edit `speech.txt` with your content

### Test (Beta)
1. Create new branch
2. Edit `speech.txt`
3. Create pull request to main branch
4. Creates `polly-audio/beta.mp3`

### Deploy (Production)  
1. Merge pull request
2. Creates `polly-audio/prod.mp3`

## Verify Audio Files

**In AWS S3 Console:**
1. Go to your bucket
2. Look in `polly-audio/` folder
3. Download `beta.mp3` or `prod.mp3`
4. Play the file

**Direct URLs:**
- Beta: `https://YOUR-BUCKET.s3.us-east-1.amazonaws.com/polly-audio/beta.mp3`
- Prod: `https://YOUR-BUCKET.s3.us-east-1.amazonaws.com/polly-audio/prod.mp3`

## Troubleshooting

**Workflow fails?**
- Check GitHub secrets are set correctly
- Verify bucket name in synthesize.py matches your actual bucket
- Make sure IAM user has the policy attached

**No audio file?**
- Check Actions tab for error messages
- Verify bucket exists and you have write permissions
