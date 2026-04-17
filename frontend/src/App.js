import { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
 
  const handleSearch = async () => {
  setLoading(true);   // 🔥 start loading

  try {
    const response = await fetch("http://127.0.0.1:8000/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query: query }),
    });

    const data = await response.json();
    setResults(data);
  } catch (error) {
    console.error(error);
  }

  setLoading(false);  // 🔥 stop loading
};

  const highlightText = (text) => {
  if (!text) return "";
  if (!query) return text;

  const words = query.toLowerCase().split(" ").filter(w => w);

  let result = text;

  words.forEach((word) => {
    const regex = new RegExp(`(${word})`, "gi");
    result = result.replace(regex, "<mark>$1</mark>");
  });

  return result;
};

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Email Assistant</h1>

      <input
        type="text"
        placeholder="Enter query (e.g. Java developer)"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        style={{ padding: "10px", width: "300px" }}
      />

      <button onClick={handleSearch} style={{ marginLeft: "10px", padding: "10px" }}>
        Search
      </button>

      <div style={{ marginTop: "20px" }}>
        {loading && <p>🔄 Loading emails...</p>}
        {!loading && results.length === 0 && query && (
          <p style={{ color: "#888", fontStyle: "italic" }}>No results found for "{query}"</p>
        )}
        {results.map((email, index) => (
          <div key={index} style={{ border: "1px solid gray", padding: "10px", marginBottom: "10px" }}>
          
            <h3 dangerouslySetInnerHTML={{ __html: highlightText(email.subject) }} />
            <p><b>Sender:</b> {email.sender}</p>
            <p dangerouslySetInnerHTML={{ __html: highlightText(email.preview) }} />
            <p><b>Tag:</b> {email.tag}</p>
            
          </div>
        ))}
        
      </div>
    </div>
  );
}

export default App;