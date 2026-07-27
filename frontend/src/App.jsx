import { useState } from "react";
import "./App.css";
import API from "./api";

function App() {
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setResponse("");

    try {
      const res = await API.post("/ask", {
        question: question,
      });

      setResponse(res.data.answer);
    } catch (error) {
      console.error(error);
      setResponse("Error connecting to backend.");
    } finally {
      setLoading(false);
    }
  };

  const handleSuggestion = (text) => {
    setQuestion(text);
  };

  const clearChat = () => {
    setQuestion("");
    setResponse("");
  };

  return (
    <div className="app">
      <header className="header">
        <h1>Monday.com Business Intelligence Agent</h1>
        <p>Skylark Drones</p>
      </header>

      <div className="chat-container">

        <div className="input-section">
          <input
            type="text"
            placeholder="Ask a business question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                askQuestion();
              }
            }}
          />

          <button
            onClick={askQuestion}
            disabled={loading}
          >
            {loading ? "Thinking..." : "Ask"}
          </button>

          <button
            onClick={clearChat}
            disabled={loading}
          >
            Clear
          </button>
        </div>

        <div className="suggestions">

          <button
            onClick={() => handleSuggestion("How many deals are there?")}
          >
            How many deals?
          </button>

          <button
            onClick={() =>
              handleSuggestion(
                "Which sector has the highest number of deals?"
              )
            }
          >
            Top Sector
          </button>

          <button
            onClick={() =>
              handleSuggestion(
                "Summarize the business for the CEO"
              )
            }
          >
            CEO Summary
          </button>

          <button
            onClick={() =>
              handleSuggestion(
                "What is the execution status?"
              )
            }
          >
            Execution Status
          </button>

        </div>

        <div className="response-box">
          <h3>AI Response</h3>

          {loading ? (
            <p>Thinking...</p>
          ) : response ? (
            <p>{response}</p>
          ) : (
            <p>Your response will appear here...</p>
          )}

        </div>

      </div>
    </div>
  );
}

export default App;