import { useLoaderData } from "react-router-dom";
import { Checked, Unchecked } from "../public/Checkbox";
import NavBar from "./components/NavBar/NavBar";
import "./App.css";

type User = {
  id: number;
  username: string;
};

type Item = {
  id: number;
  category: string;
  done: boolean;
  name: string;
};

function App() {
  const { user, bucketList } = useLoaderData() as {
    user: User;
    bucketList: Item[];
  };

  return (
    <>
      <NavBar name={user?.username} />
      <main>
        {bucketList.map((item) => (
          <figure key={item.id}>
            {item.done ? <Checked /> : <Unchecked />}
            <h1>{item.name}</h1>
          </figure>
        ))}
      </main>
    </>
  );
}

export default App;
