## Oncology-Monitoring-Platform

![Oncology Monitoring Platform Demo](https://github.com/PrecisionHealthIntelligence/Oncology-Monitoring-Platform/blob/main/demo/Animation.gif)


Start the uvicorn and elastic search backend <br>
`cd backend\app` <br>
`docker-compose up`

Start the streamlit frontend <br>
`cd frontend` <br>
`docker build -t streamlit/app --no-cache . -f Dockerfile.yml` <br>
`docker run -d --name streamlit_app -p 8501:8501 streamlit/app`

