import { useLoaderData, useRevalidator } from "react-router-dom";
import { Add } from "../public/Add";
import Item from "./components/Item/Item";
import NavBar from "./components/NavBar/NavBar";
import type { ItemType, UserType } from "./types/types";
import "./App.css";
import { useState } from "react";

export default function App() {
  const token = import.meta.env.VITE_USER_TOKEN;
  const url = import.meta.env.VITE_API_URL;

  const revalidator = useRevalidator();

  const { user, bucketList } = useLoaderData() as {
    user: UserType;
    bucketList: ItemType[];
  };

  const [isOpen, setIsOpen] = useState<boolean>(false);
  const [formData, setFormData] = useState<Omit<ItemType, "id">>({
    name: "",
    done: false,
    category: "",
  });

  const handleOpen = () => {
    setIsOpen(true);
  };

  const handleSubmit = async () => {
    const newItem = {
      user: user.id,
      name: formData.name,
      done: formData.done,
      category: formData.category,
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

        {isOpen && (
          <div>
            <h3>Ajouter un item à la liste</h3>
            <form method="dialog" onSubmit={handleSubmit}>
              <label htmlFor="nameItem">Nom de l'item : </label>
              <input
                type="text"
                id="nameItem"
                onChange={(e) => {
                  setFormData((prev) => ({ ...prev, name: e.target.value }));
                }}
                required
              />

              <label htmlFor="select-category">Catégorie : </label>
              <select
                name="categories"
                id="select-category"
                onChange={(e) => {
                  setFormData((prev) => ({
                    ...prev,
                    category: e.target.value,
                  }));
                }}
              >
                <option value="">--Choisis une catégorie--</option>
                <option value="travel">Voyage</option>
                <option value="reading">Lecture</option>
                <option value="exp">Expérience</option>
                <option value="sport">Sport</option>
                <option value="skill">Compétence</option>
                <option value="other">Autre</option>
              </select>

              <label htmlFor="doneItem">Réalisé : </label>
              <input
                type="checkbox"
                id="doneItem"
                onChange={(e) => {
                  setFormData((prev) => ({
                    ...prev,
                    done: e.target.value === "on",
                  }));
                }}
              />

              <button type="submit">Ajouter</button>
              <button
                type="button"
                onClick={() => {
                  setIsOpen(false);
                }}
              >
                Annuler
              </button>
            </form>
          </div>
        )}
      </main>
    </>
  );
}
