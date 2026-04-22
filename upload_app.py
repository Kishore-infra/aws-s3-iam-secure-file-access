from flask import Flask, request, redirect
import boto3

app = Flask(__name__)

s3 = boto3.client('s3')

@app.route("/download")
def download():
    filename = request.args.get("file")

    url = s3.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': 'kishore-upload-project-01',
            'Key': filename
        },
        ExpiresIn=3600
    )

    return redirect(url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
