# 🎬 Movie Catalog API - Backend (FastAPI & MongoDB)

This is the production-ready REST API for the Movie Catalog application. Developed with **FastAPI**, it provides a high-performance interface to manage movie records persisted in **MongoDB Atlas**.

## 🚀 Key Improvements (Persistence)

Unlike previous versions that used volatile RAM storage, this API is now integrated with **MongoDB**. 
* **Data Persistence:** Your movies are safely stored in the cloud.
* **Security:** Uses SSL/TLS encryption with `certifi` for secure database handshakes on Render.

## 🛠️ Technologies Used

* **Python 3.13+**: Latest stable Python version.
* **FastAPI**: Modern, high-performance web framework.
* **MongoDB Atlas**: Cloud NoSQL database.
* **Motor/PyMongo**: Asynchronous MongoDB driver.
* **Pydantic**: For strict data validation and JSON schemas.
* **Render**: Cloud hosting with automated CI/CD.

## 📌 API Features & Endpoints

* `GET /films`: Fetches the complete list of movies from the database.
* `POST /films`: Adds a new movie to the catalog.
* **Swagger UI**: Interactive documentation available at `/docs`.

## 📥 Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/joaopedro08-dev/Filmes-Backend.git](https://github.com/joaopedro08-dev/Filmes-Backend.git)
   cd Filmes-Backend
2. **Setup Environment Variables: Create a .env file in the root folder:**
   ```bash
   MONGODB_URL=your_mongodb_atlas_connection_string
   MONGODB_DB=python_fastapi
   MONGODB_COLLECTION=films
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Run the Server:**
   ```bash
   python main.py
## 🌐 Deployment

The API is live on Render.

* Live Endpoint: https://filmes-backend-pal2.onrender.com/films

* Production Command: uvicorn main:app --host 0.0.0.0 --port $PORT

## 🔒 Security Configuration

To ensure a stable connection between Render and MongoDB Atlas, the project implements:
tlsCAFile via certifi to handle SSL certificate verification.
tlsAllowInvalidCertificates for environment compatibility.
CORS Middleware configured for Vercel (Frontend) integration.
