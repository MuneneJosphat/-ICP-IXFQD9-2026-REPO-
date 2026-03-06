
const API_BASE = "http://127.0.0.1:8000";
const API_KEY = "mysecretkey123"; // must match backend config

export async function predictMessage(text) {
  const res = await fetch(`${API_BASE}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": API_KEY,
    },
    body: JSON.stringify({ text }),
  });

  if (!res.ok) {
    throw new Error(`Error ${res.status}`);
  }
  return res.json(); // { label, is_spam }
}

export async function fetchPredictions(limit = 20) {
  const res = await fetch(`${API_BASE}/predictions?limit=${limit}`, {
    headers: {
      "x-api-key": API_KEY,
    },
  });

  if (!res.ok) {
    throw new Error(`Error ${res.status}`);
  }
  return res.json(); // list of PredictionLog
}
