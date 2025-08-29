import { useState } from "react";
import { useLoaderData, useRevalidator } from "react-router-dom";
import { Add } from "../public/Add";
import Item from "./components/Item/Item";
import AddItemModal from "./components/Modals/AddItemModal";
import NavBar from "./components/NavBar/NavBar";
import type { ItemType, UserType } from "./types/types";
import "./App.css";
import EditItemModal from "./components/Modals/EditItemModal";

export default function App() {
  const token = import.meta.env.VITE_USER_TOKEN;
  const url = import.meta.env.VITE_API_URL;

  const revalidator = useRevalidator();

  const { user, bucketList } = useLoaderData() as {
    user: UserType;
    bucketList: ItemType[];
  };

  const [isAddItemOpen, setIsAddItemOpen] = useState<boolean>(false);
  const handleAddItemOpen = () => {
    setIsAddItemOpen(true);
  };
  const handleAddItemSubmit = async (item: Omit<ItemType, "id">) => {
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
      setIsAddItemOpen(false);
      revalidator.revalidate();
    }
  };

  const [isEditItemOpen, setIsEditItemOpen] = useState<boolean>(false);
  const [itemToEdit, setItemToEdit] = useState<ItemType>({
    id: 0,
    name: "",
    done: false,
    category: "",
  });
  const handleEditItemSubmit = async (item: ItemType) => {
    const response = await fetch(`${url}/items/${item.id}/`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
      body: JSON.stringify(item),
    });

    const data = await response.json();

    if (data) {
      setIsEditItemOpen(false);
      revalidator.revalidate();
    }
  };

  return (
    <>
      <NavBar name={user?.username} />
      <main>
        <button type="button" onClick={handleAddItemOpen}>
          <Add />
        </button>
        <ul>
          {bucketList.map((item) => (
            <li key={item.id}>
              <Item
                item={item}
                token={token}
                url={url}
                onEdit={(it) => {
                  setItemToEdit(it);
                  setIsEditItemOpen(true);
                }}
              />
            </li>
          ))}
        </ul>

        <AddItemModal
          isOpen={isAddItemOpen}
          onClose={() => {
            setIsAddItemOpen(false);
          }}
          onSubmit={handleAddItemSubmit}
        />

        <EditItemModal
          item={itemToEdit}
          isOpen={isEditItemOpen}
          onClose={() => {
            setIsEditItemOpen(false);
          }}
          onSubmit={handleEditItemSubmit}
        />
      </main>
    </>
  );
}
