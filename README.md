Secure File Access System using AWS S3 + IAM
📌 Project Overview
This project demonstrates a secure way to access private files stored in AWS S3 using IAM and presigned URLs.
Instead of making files public, access is controlled dynamically through a backend service.
🛠️ Technologies Used
AWS S3
AWS IAM
Python
Flask
Boto3
🔐 Key Concept
Files are stored privately in S3
IAM is used to control access permissions
Backend generates temporary secure links (presigned URLs)
Users can access files only through controlled API requests
🚀 API Endpoint
GET /download?file=
Example:
http://:5000/download?file=kishore%20resume.pdf
🔄 Project Evolution
This project was developed step-by-step through multiple improvements:
Step 1: Static File Access (Initial Testing)
Generated presigned URL for a fixed file
File name was hardcoded
Verified S3 and IAM integration
Step 2: JSON Response
Returned presigned URL in API response
Used for testing and debugging
Step 3: Direct File Access
Implemented redirect functionality
File opens directly in browser
Improved user experience
Step 4: Dynamic File Access (Final Version)
File name passed as query parameter
Backend dynamically generates access URL
Same API supports multiple files
🔐 Security Benefits
No public access to S3 bucket
Temporary access using presigned URLs
IAM-based permission control
Secure file sharing
🧠 What I Learned
Working with AWS S3 and IAM
Generating presigned URLs using Boto3
Designing secure backend systems
Building APIs using Flask
Handling real-world cloud security scenarios
📌 Conclusion
This project demonstrates a real-world approach to secure file access using AWS services and backend logic, following best practices for cloud security.
