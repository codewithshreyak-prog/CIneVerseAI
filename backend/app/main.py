from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="CineVerse AI API",
    description="Backend API for actor profiles, movie data, recommendations, and AI cinema chatbot.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ACTORS = [
    {
        "id": 1,
        "name": "Mahesh Babu",
        "industry": "Telugu Cinema",
        "greeting": "Hey, how are you? Welcome to my cinema journey!",
        "dialogue": "A cinematic superstar-style dialogue appears here.",
        "known_for": ["Action", "Drama", "Thriller"],
        "featured_movies": ["Pokiri", "Dookudu", "Businessman", "Srimanthudu"]
    },
    {
        "id": 2,
        "name": "Allu Arjun",
        "industry": "Telugu Cinema",
        "greeting": "Hey, welcome! Ready to explore my movie journey?",
        "dialogue": "A stylish fan-style dialogue appears here.",
        "known_for": ["Action", "Dance", "Drama"],
        "featured_movies": ["Arya", "Race Gurram", "Pushpa", "Ala Vaikunthapurramuloo"]
    },
    {
        "id": 3,
        "name": "Samantha Ruth Prabhu",
        "industry": "Indian Cinema",
        "greeting": "Hi there! Let’s explore my movie journey.",
        "dialogue": "A memorable cinema quote appears here.",
        "known_for": ["Romance", "Drama", "Thriller"],
        "featured_movies": ["Ye Maaya Chesave", "Eega", "Theri", "Oh! Baby"]
    }
]


@app.get("/")
def home():
    return {"message": "Welcome to CineVerse AI"}


@app.get("/health")
def health_check():
    return {"status": "running", "service": "CineVerse AI API"}


@app.get("/actors")
def get_actors():
    return ACTORS


@app.get("/recommend")
def recommend_movies(mood: str):
    return {
        "user_request": mood,
        "recommendations": [
            {
                "title": "Example Mystery Thriller",
                "reason": "Recommended because you asked for suspense and thriller without heavy horror."
            },
            {
                "title": "Example Crime Series",
                "reason": "This fits your interest in thriller and mystery while avoiding supernatural horror."
            }
        ]
    }