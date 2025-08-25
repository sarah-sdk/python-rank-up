import "./App.css";

function App() {
  // const token = import.meta.env.VITE_USER_TOKEN;

  return (
    <>
      <nav className="navbar">
        <img
          src="https://i.pinimg.com/736x/f4/bc/c0/f4bcc0e261b41bfccdc47dcfca7d4b63.jpg"
          alt="avatar"
          className="avatar"
        />
        <h1>Ma bucketlist</h1>
        <div>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            fill="currentColor"
            className="bi bi-search"
            viewBox="0 0 16 16"
          >
            <title>Recherche</title>
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0" />
          </svg>
        </div>
      </nav>
    </>
  );
}

export default App;
