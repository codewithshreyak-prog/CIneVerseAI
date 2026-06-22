import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import "./App.css";

type Actor = {
  id: number;
  name: string;
  industry: string;
  greeting: string;
  dialogue: string;
  known_for: string[];
  featured_movies: string[];
};

function App() {
  const [actors, setActors] = useState<Actor[]>([]);
  const [selectedActor, setSelectedActor] = useState<Actor | null>(null);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/actors")
      .then((response) => response.json())
      .then((data) => setActors(data))
      .catch((error) => console.error("Error fetching actors:", error));
  }, []);

  const filteredActors = actors.filter((actor) => {
    const searchText = searchTerm.toLowerCase();

    return (
      actor.name.toLowerCase().includes(searchText) ||
      actor.industry.toLowerCase().includes(searchText) ||
      actor.known_for.some((tag) => tag.toLowerCase().includes(searchText)) ||
      actor.featured_movies.some((movie) =>
        movie.toLowerCase().includes(searchText)
      )
    );
  });

  const speakGreeting = (actor: Actor) => {
    setSelectedActor(actor);

    const message = new SpeechSynthesisUtterance(actor.greeting);
    message.rate = 0.95;
    message.pitch = 1;

    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(message);
  };

  return (
    <main className="app">
      <section className="hero-section">
        <p className="eyebrow">AI Cinema Discovery Platform</p>
        <h1>CineVerse AI 🎬</h1>
        <p className="subtitle">
          Explore actor filmographies, hear interactive greetings, ask cinema
          questions, and get mood-based movie recommendations.
        </p>
      </section>

      <section className="search-section">
        <input
          type="text"
          value={searchTerm}
          onChange={(event) => setSearchTerm(event.target.value)}
          placeholder="Search heroes by name, genre, industry, or movie..."
        />
      </section>

      <section className="actor-grid">
        {filteredActors.map((actor) => (
          <motion.div
            key={actor.id}
            className="actor-card"
            whileHover={{ scale: 1.04 }}
            whileTap={{ scale: 0.97 }}
            onClick={() => speakGreeting(actor)}
          >
            <div className="actor-avatar">
              {actor.name
                .split(" ")
                .map((word) => word[0])
                .join("")}
            </div>

            <h2>{actor.name}</h2>
            <p>{actor.industry}</p>

            <div className="tags">
              {actor.known_for.map((tag) => (
                <span key={tag}>{tag}</span>
              ))}
            </div>

            <button>Play Star Greeting</button>
          </motion.div>
        ))}
      </section>

      {selectedActor && (
        <section className="selected-panel">
          <h2>{selectedActor.name}</h2>
          <p className="quote">“{selectedActor.dialogue}”</p>
          <p>{selectedActor.greeting}</p>

          <h3>Featured Movies</h3>
          <div className="movie-list">
            {selectedActor.featured_movies.map((movie) => (
              <span key={movie}>{movie}</span>
            ))}
          </div>
        </section>
      )}
    </main>
  );
}

export default App;