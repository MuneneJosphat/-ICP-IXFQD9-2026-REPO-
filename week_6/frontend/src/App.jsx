
import { useEffect, useState } from "react";
import MessageForm from "./components/MessageForm.jsx";
import PredictionHistory from "./components/PredictionHistory.jsx";
import { predictMessage, fetchPredictions } from "./api.js";

function App() {
  const [lastResult, setLastResult] = useState(null);
  const [history, setHistory] = useState([]);
  const [loadingHistory, setLoadingHistory] = useState(false);
  const [error, setError] = useState("");

  const loadHistory = async () => {
    setLoadingHistory(true);
    setError("");
    try {
      const items = await fetchPredictions(20);
      setHistory(items);
    } catch (err) {
      console.error(err);
      setError("Failed to load history.");
    } finally {
      setLoadingHistory(false);
    }
  };

  useEffect(() => {
    loadHistory();
  }, []);

  const handlePredict = async (text) => {
    const res = await predictMessage(text);
    setLastResult({ text, ...res });
    await loadHistory(); // refresh table after saving to DB
  };

  return (
    <div className="app">
      <header>
        <h1>SMS Spam Classifier Dashboard</h1>
        <p>Week 6 – Capstone Project</p>
      </header>

      <main>
        <div className="left">
          <MessageForm onResult={handlePredict} />
          {lastResult && (
            <div className="card">
              <h2>Last Result</h2>
              <p>
                <strong>Message:</strong> {lastResult.text}
              </p>
              <p>
                <strong>Prediction:</strong>{" "}
                <span className={lastResult.is_spam ? "spam" : "ham"}>
                  {lastResult.is_spam ? "SPAM" : "HAM"}
                </span>
              </p>
            </div>
          )}
        </div>

        <div className="right">
          {loadingHistory ? (
            <div className="card">
              <p>Loading history...</p>
            </div>
          ) : (
            <PredictionHistory items={history} />
          )}
          {error && <p className="error">{error}</p>}
        </div>
      </main>
    </div>
  );
}

export default App;
