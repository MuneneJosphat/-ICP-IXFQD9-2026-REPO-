
import { useState } from "react";

function MessageForm({ onResult }) {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (!text.trim()) {
      setError("Please enter a message.");
      return;
    }

    setLoading(true);
    try {
      await onResult(text);
      setText("");
    } catch (err) {
      console.error(err);
      setError("Failed to get prediction.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="card">
      <h2>Classify SMS</h2>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={4}
        placeholder="Paste SMS text here..."
      />
      {error && <p className="error">{error}</p>}
      <button type="submit" disabled={loading}>
        {loading ? "Predicting..." : "Predict"}
      </button>
    </form>
  );
}

export default MessageForm;
