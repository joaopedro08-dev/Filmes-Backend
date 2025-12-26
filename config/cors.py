from fastapi.middleware.cors import CORSMiddleware

# API access settings
def setup_cors(app):
    app.add_middleware(
        CORSMiddleware, # Communication
        allow_origins=["*"], # Web URL
        allow_credentials=True, # Credentials
        allow_methods=["*"], # HTTP Methods
        allow_headers=["*"], # Header
    )