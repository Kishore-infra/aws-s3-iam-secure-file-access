  Secure Private File Access using AWS S3, IAM and Presigned URLs 

«A Flask-based backend system that enables secure, temporary, and dynamic access to files stored in a private AWS S3 bucket.»

---

 Overview 

This project demonstrates how to securely access private files stored in AWS S3 without making the bucket public.

The system uses:

- IAM policies for access control
- Boto3 to generate presigned URLs
- Flask API to handle requests

The S3 bucket is configured with Block Public Access enabled, ensuring that files are never publicly exposed.

---

 Features

- Private S3 bucket (no public access)
- Temporary access using presigned URLs
- IAM-based permission control (least privilege)
- Dynamic file access using query parameters
- Direct browser access via redirect
- Simple REST API design

---

 Project Evolution

This project was built step-by-step through multiple testing stages:

Stage 1 — Static File Access

- Generated presigned URL for a hardcoded file
- Verified S3 connectivity and IAM permissions

Stage 2 — JSON Response

- Returned presigned URL as JSON
- Used for debugging and API validation

Stage 3 — Direct File Access

- Implemented redirect to open file directly in browser
- Improved user experience

Stage 4 — Dynamic File Access (Final)

- File name passed as query parameter
- Backend generates presigned URL dynamically
- Single API supports multiple files

---

 Security Architecture

- S3 Bucket: Private (Block Public Access enabled)
- Access Control: IAM policies (least privilege)
- File Access: Presigned URLs (time-limited)
- Backend: Flask API

---

 API Endpoint

GET /download?file=<filename>

Example:
http://<EC2-IP>:5000/download?file=kishore%20resume.pdf

---

 Tech Stack

- Python (Flask)
- AWS S3
- AWS IAM
- Boto3

---

 Setup & Installation

Prerequisites

- Python 3.x
- AWS account
- S3 bucket (private)
- IAM user with S3 read permissions

Install dependencies

pip install -r requirements.txt

Configure AWS

aws configure

Run application

python upload_app.py

---

 How It Works

1. User sends request to backend API
2. Flask receives the request
3. Boto3 generates a presigned URL
4. URL is valid for a limited time (e.g., 1 hour)
5. User is redirected to S3
6. File opens securely in browser

---

 What I Learned

- Working with AWS S3 and IAM
- Implementing least-privilege access
- Generating presigned URLs using Boto3
- Designing secure backend APIs
- Understanding real-world cloud security practices

---

 Project Structure

project
├
upload_app.py
├ 
requirements.txt
└ README.md

---

 Conclusion

This project demonstrates a practical approach to secure file access using AWS services, ensuring that sensitive data remains private while still being accessible through controlled, temporary links.
