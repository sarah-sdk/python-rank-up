import { useState } from "react";
import { Checked, Unchecked } from "../../../public/Checkbox";
import type { ItemType } from "../../types/types";

const token = import.meta.env.VITE_USER_TOKEN;
const url = import.meta.env.VITE_API_URL;

export default function Item({ item }: { item: ItemType }) {
  const [isChecked, setIsChecked] = useState<boolean>(item.done);

  const handleChecked = async () => {
    const updateDone = {
      done: !item.done,
    };

    const response = await fetch(`${url}/items/${item.id}/`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${token}`,
      },
      body: JSON.stringify(updateDone),
    });

    const data = await response.json();

    setIsChecked(data.done);
  };

  return (
    <>
      <button type="button" onClick={handleChecked}>
        {isChecked ? <Checked /> : <Unchecked />}
      </button>
      <h1>{item.name}</h1>
    </>
  );
}
