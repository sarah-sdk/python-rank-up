import { useState } from "react";
import { useLoaderData, useRevalidator } from "react-router-dom";
import { Add } from "../public/Add";
import AddItemModal from "./components/AddItemModal/AddItemModal";
import Item from "./components/Item/Item";
import NavBar from "./components/NavBar/NavBar";
import type { ItemType, UserType } from "./types/types";
import "./App.css";

export default function App() {
  const token = import.meta.env.VITE_USER_TOKEN;
  const url = import.meta.env.VITE_API_URL;

  const revalidator = useRevalidator();

  const { user, bucketList } = useLoaderData() as {
    user: UserType;
    bucketList: ItemType[];
  };

  const [isOpen, setIsOpen] = useState<boolean>(false);

  const handleOpen = () => {
    setIsOpen(true);
  };

  const handleSubmit = async (item: Omit<ItemType, "id">) => {
    const newItem = {
      user: user.id,
      name: item.name,
      done: item.done,
      category: item.category,
    };

    const response = await fetch(`${url}/items/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
      body: JSON.stringify(newItem),
    });

    const data = await response.json();

    if (data) {
      setIsOpen(false);
      revalidator.revalidate();
    }
  };

  return (
    <>
      <NavBar name={user?.username} />
      <main>
        <button type="button" onClick={handleOpen}>
          <Add />
        </button>
        {bucketList.map((item) => (
          <figure key={item.id}>
            <Item item={item} token={token} url={url} />
          </figure>
        ))}

        <AddItemModal
          isOpen={isOpen}
          onClose={() => {
            setIsOpen(false);
          }}
          onSubmit={handleSubmit}
        />
      </main>
    </>
  );
}
