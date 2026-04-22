from flask import Flask, redirect
import boto3

app = Flask(__name__)

s3 = boto3.client('s3')

@app.route("/")
def home():
    return "Flask app is Running Successfully"

@app.route("/get-url")
def get_presigned_url():
    url = s3.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': 'kishore-upload-project-01',
            'Key': 'kishore resume.pdf'
        },
        ExpiresIn=3600
    )
    return redirect(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
