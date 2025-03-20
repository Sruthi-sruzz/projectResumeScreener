Automated Resume Screener
This project is a Resume Screening AI that helps recruiters automatically analyze and score resumes against a given job description. It uses FastAPI, Scikit-learn (TF-IDF), Cosine Similarity, and React.js to provide an intuitive interface for uploading resumes and viewing match scores.
Features
•	Upload multiple PDF resumes
•	Enter a Job Description and get match scores
•	View resumes via a public link
•	Uses TF-IDF Vectorization + Cosine Similarity for matching
•	FastAPI backend and React frontend
•	Deployed on AWS EC2
Tech Stack
Component	Technology
Backend	FastAPI, Python, Scikit-learn
Frontend	React.js, Vite
Storage	Local storage (can be extended to S3)
Deployment	AWS EC2, Nginx, Uvicorn
Project Structure
Quick Start Guide
1. Clone the Repository
2. Backend Setup (FastAPI)
Install dependencies
Start the backend server
Backend will be running at http://<EC2-Public-IP>:8000
3. Frontend Setup (React.js)
Install dependencies
Start the React development server
Frontend will be running at http://<EC2-Public-IP>:5173
How to Use
1.	Enter a Job Description
2.	Upload Resumes (PDFs)
3.	Click "Upload & Get Scores"
4.	View Matching Score & Resume Link
Deployment on AWS EC2
1. Launch an EC2 Instance
•	Instance Type: t3.medium (Recommended)
•	OS: Amazon Linux 2
•	Allow port 8000 & 5173 in Security Groups
2. SSH into the instance
3. Install Dependencies
4. Clone and Setup Project
5. Start Backend on Public IP
6. Start Frontend
7. Serve Frontend with Nginx
Now your app is accessible at http://your-ec2-ip
Troubleshooting
Issue	Solution
CORS Error	Add CORS middleware in main.py
Port Blocked	Allow 8000 and 5173 in Security Groups
File Not Found	Check if the uploaded file exists in uploaded_resumes/
License
This project is licensed under the MIT License.
Contributing
Feel free to submit a PR if you have improvements or bug fixes!
Author
Your Name
GitHub: https://github.com/Sruthi-sruzz
Email: vanamalasruthi013@gmail.com

