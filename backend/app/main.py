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
        "name": "Prabhas",
        "industry": "Indian Cinema",
        "greeting": "Hey, welcome to my world of epic cinema!",
        "dialogue": "A powerful cinematic intro appears here.",
        "known_for": ["Action", "Epic", "Drama"],
        "featured_movies": ["Baahubali", "Mirchi", "Chatrapathi", "Saaho"],
        "image_url": ""
    },
    {
        "id": 2,
        "name": "Mahesh Babu",
        "industry": "Telugu Cinema",
        "greeting": "Hey, how are you? Welcome to my cinema journey!",
        "dialogue": "A cinematic superstar-style dialogue appears here.",
        "known_for": ["Action", "Drama", "Thriller"],
        "featured_movies": ["Pokiri", "Dookudu", "Businessman", "Srimanthudu"],
        "image_url": ""
    },
    {
        "id": 3,
        "name": "Pawan Kalyan",
        "industry": "Telugu Cinema",
        "greeting": "Hey, welcome! Let’s explore my powerful cinema journey.",
        "dialogue": "A fan-style power star intro appears here.",
        "known_for": ["Action", "Drama", "Political Drama"],
        "featured_movies": ["Tholi Prema", "Gabbar Singh", "Jalsa", "Attarintiki Daredi"],
        "image_url": ""
    },
    {
        "id": 4,
        "name": "Allu Arjun",
        "industry": "Telugu Cinema",
        "greeting": "Hey, welcome! Ready to explore my stylish movie journey?",
        "dialogue": "A stylish fan-style dialogue appears here.",
        "known_for": ["Action", "Dance", "Drama"],
        "featured_movies": ["Arya", "Race Gurram", "Pushpa", "Ala Vaikunthapurramuloo"],
        "image_url": ""
    },
    {
        "id": 5,
        "name": "Jr NTR",
        "industry": "Telugu Cinema",
        "greeting": "Hey, welcome! Let’s explore my powerful cinema journey.",
        "dialogue": "A mass cinematic intro appears here.",
        "known_for": ["Action", "Drama", "Performance"],
        "featured_movies": ["RRR", "Temper", "Janatha Garage", "Aravinda Sametha"],
        "image_url": ""
    },
    {
        "id": 6,
        "name": "Chiranjeevi",
        "industry": "Telugu Cinema",
        "greeting": "Hello, welcome to my legendary cinema journey.",
        "dialogue": "A megastar-style cinematic intro appears here.",
        "known_for": ["Action", "Dance", "Drama"],
        "featured_movies": ["Indra", "Tagore", "Khaidi", "Sye Raa Narasimha Reddy"],
        "image_url": ""
    },
    {
        "id": 7,
        "name": "Nagarjuna Akkineni",
        "industry": "Telugu Cinema",
        "greeting": "Hey, welcome! Let’s explore my classic cinema journey.",
        "dialogue": "A charming star-style intro appears here.",
        "known_for": ["Romance", "Drama", "Action"],
        "featured_movies": ["Shiva", "Manam", "Geetanjali", "Soggade Chinni Nayana"],
        "image_url": ""
    },
    {
        "id": 8,
        "name": "Venkatesh Daggubati",
        "industry": "Telugu Cinema",
        "greeting": "Hello, welcome to my family entertainer cinema journey.",
        "dialogue": "A warm cinematic intro appears here.",
        "known_for": ["Family Drama", "Comedy", "Action"],
        "featured_movies": ["Drushyam", "F2", "Nuvvu Naaku Nachav", "Narappa"],
        "image_url": ""
    },
    {
        "id": 9,
        "name": "Ram Charan",
        "industry": "Telugu Cinema",
        "greeting": "Hey, ready to explore my action-packed movie journey?",
        "dialogue": "A high-energy star-style dialogue appears here.",
        "known_for": ["Action", "Drama", "Dance"],
        "featured_movies": ["Magadheera", "Rangasthalam", "RRR", "Dhruva"],
        "image_url": ""
    },
    {
        "id": 10,
        "name": "Nani",
        "industry": "Telugu Cinema",
        "greeting": "Hey, welcome to my natural cinema journey!",
        "dialogue": "A warm and natural star-style dialogue appears here.",
        "known_for": ["Drama", "Romance", "Comedy"],
        "featured_movies": ["Jersey", "Eega", "Bhale Bhale Magadivoy", "Dasara"],
        "image_url": ""
    },
    {
        "id": 11,
        "name": "Vijay Deverakonda",
        "industry": "Telugu Cinema",
        "greeting": "Hey, welcome! Let’s explore my bold cinema journey.",
        "dialogue": "A modern star-style cinematic intro appears here.",
        "known_for": ["Romance", "Drama", "Youth"],
        "featured_movies": ["Arjun Reddy", "Geetha Govindam", "Dear Comrade", "Taxiwaala"],
        "image_url": ""
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