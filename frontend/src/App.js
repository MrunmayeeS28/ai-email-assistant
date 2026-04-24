import { useState } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedTag, setSelectedTag] = useState("All");
  const [visibleCount, setVisibleCount] = useState(5);
  const [useCache, setUseCache] = useState(true);

  const handleSearch = async () => {
    setLoading(true);
    setVisibleCount(5); // reset pagination

    try {
      const response = await fetch("http://127.0.0.1:8000/search", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
        use_cache: useCache
      });

      const data = await response.json();

      // supports both: array OR { results: [] }
      setResults(Array.isArray(data) ? data : data || []);
      setSelectedTag("All"); 
    } catch (error) {
      console.error(error);
      alert("Backend not responding");
    }

    setLoading(false);
  };

  const highlightText = (text) => {
    if (!text || !query) return text;

    const words = query.toLowerCase().split(" ").filter(w => w);
    let result = text;

    words.forEach((word) => {
      const regex = new RegExp(`(${word})`, "gi");
      result = result.replace(regex, "<mark>$1</mark>");
    });

    return result;
  };

 const filteredResults =
  selectedTag === "All"
    ? results
    : results.filter(
        (email) =>
          (email.tag || "").toLowerCase().trim() === selectedTag.toLowerCase()
      );
      console.log("Filtered:", filteredResults.length);
      console.log("Visible:", visibleCount);
      console.log("Tags:", results.map(e => e.tag));

  return (
    <div className="container">

      {/* Sidebar */}
      <div className="sidebar">
        <h2>Filters</h2>

        {["All", "Job", "Internship", "Shopping", "General"].map((tag) => (
          <div
            key={tag}
            className={`sidebar-item ${selectedTag === tag ? "active" : ""}`}
            onClick={() => setSelectedTag(tag)}
          >
            {tag}
          </div>
        ))}
      </div>

      {/* Main */}
      <div className="main">

        <h1>AI Email Assistant</h1>

      <label style={{ marginLeft: "10px" }}>
      <input
        type="checkbox"
        checked={useCache}
        onChange={() => setUseCache(!useCache)}
      />
         Use Cached Emails
      </label>

        {/* Search */}
        <div className="search-box">
          <input
            type="text"
            placeholder="Search emails..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />

          <button onClick={handleSearch}>Search</button>
        </div>

        {/* Loading */}
        {loading && <p className="loading">Loading emails...</p>}

        {/* No results */}
        {!loading && filteredResults.length === 0 && query && (
          <p className="no-results">No results found</p>
        )}

        {/* Email list */}
        <div className="email-list">
          {filteredResults.slice(0, visibleCount).map((email, index) => (
            <div className="email-card" key={index}>
              <h3 dangerouslySetInnerHTML={{ __html: highlightText(email.subject) }} />
              <p><b>Sender:</b> {email.sender}</p>
              <p dangerouslySetInnerHTML={{ __html: highlightText(email.preview) }} />
              <p className="date">{email.date}</p>
              <span className="tag">{email.tag}</span>
            </div>
          ))}
        </div>

        {/* Load more */}
        {filteredResults.length > visibleCount && (
        <button
          className="load-more"
          onClick={() => setVisibleCount(visibleCount + 5)}
        >
        Load More
        </button>
        )}
      </div>
    </div>
  );
}

export default App;