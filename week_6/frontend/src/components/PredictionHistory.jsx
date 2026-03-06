function PredictionHistory({ items }) {
  return (
    <div className="card">
      <h2>Recent Predictions</h2>
      {items.length === 0 ? (
        <p>No predictions yet.</p>
      ) : (
        <table>
          <thead>
            <tr>
              <th>Time (EAT)</th>
              <th>Message</th>
              <th>Label</th>
            </tr>
          </thead>
          <tbody>
            {items.map((p) => {
              const createdUtc = new Date(p.created_at);
              const createdEat = new Date(
                createdUtc.getTime() + 3 * 60 * 60 * 1000
              );
              return (
                <tr key={p.id}>
                  <td>{createdEat.toLocaleString()}</td>
                  <td className="msg-cell">{p.text}</td>
                  <td className={p.is_spam ? "spam" : "ham"}>
                    {p.is_spam ? "SPAM" : "HAM"}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default PredictionHistory;
