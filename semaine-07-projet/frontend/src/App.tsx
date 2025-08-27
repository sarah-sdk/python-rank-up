import { useLoaderData } from "react-router-dom";
import Item from "./components/Item/Item";
import NavBar from "./components/NavBar/NavBar";
import type { ItemType, UserType } from "./types/types";
import "./App.css";

function App() {
  const { user, bucketList } = useLoaderData() as {
    user: UserType;
    bucketList: ItemType[];
  };

  return (
    <>
      <NavBar name={user?.username} />
      <main>
        {bucketList.map((item) => (
          <figure key={item.id}>
            <Item item={item} />
          </figure>
        ))}
      </main>
    </>
  );
}

export default App;
