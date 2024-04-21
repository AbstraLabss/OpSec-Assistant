# OpSec-Assistant
OpSec Assistant is a Exclusive customer service that can help you thoroughly understand OpSec.

# Goal
After crawling information about OpSec, this AI customer service can answer any question regarding to OpSec. Utilizing AI, RAG, LLm technique. Our OpSec Assistant can efficiently assist users in resolving issues.

# Execution Frontend
```
streamlit run app.py --server.port 7666
```

# Execution Swagger
```
uvicorn server:app --port 8080 --reload
```

# Local Server vector db
http://172.21.10.105:6333/