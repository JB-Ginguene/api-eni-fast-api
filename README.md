# Build an API with FastAPI

Here is a small project to show you how easy it is to build an API with [FastAPI](https://fastapi.tiangolo.com/).

## Run the project

I decided to use a MongoDB database because I am familiar with this NoSQL DB.
To use this project, you will need a MongoDB deployed on an Atlas Cluster, more infos [here](https://www.mongodb.com/cloud/atlas)

The application will automatically create a DB 'eni' and a collection 'students' if you don't have them yet.

```bash
# Install the requirements:
pip install -r requirements.txt

# Configure the location of your MongoDB database:
export MONGODB_URL="mongodb+srv://<username>:<password>@<url>/<db>?retryWrites=true&w=majority"

# Start the service:
uvicorn app:app --reload
```

You can now open this URL : http://localhost:8000/docs in your browser 	:-)