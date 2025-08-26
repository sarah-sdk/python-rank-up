import "./NavBar.css";

export default function NavBar({ name }: { name: string }) {
  return (
    <header className="navbar">
      <h1>Bonjour, {name}</h1>
      <nav>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="2rem"
          height="2rem"
          viewBox="0 0 24 24"
        >
          <title>Recherche</title>
          <path
            fill="none"
            stroke="currentColor"
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="1.5"
            d="M15.553 15.553a7.06 7.06 0 1 0-9.985-9.985a7.06 7.06 0 0 0 9.985 9.985m0 0L20 20"
          />
        </svg>
        <img
          src="https://i.pinimg.com/736x/f4/bc/c0/f4bcc0e261b41bfccdc47dcfca7d4b63.jpg"
          alt="avatar"
          className="avatar"
        />
      </nav>
    </header>
  );
}
