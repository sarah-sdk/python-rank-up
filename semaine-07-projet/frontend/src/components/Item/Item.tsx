import { useState } from "react";
import type { ItemType } from "../../types/types";

export default function Item({
  item,
  token,
  url,
  onEdit,
}: {
  item: ItemType;
  token: string;
  url: string;
  onEdit: (item: ItemType) => void;
}) {
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
      <input
        type="checkbox"
        checked={isChecked}
        onChange={handleChecked}
        id={`item-${item.id}`}
      />
      <label htmlFor={`item-${item.id}`}>{item.name}</label>
      <div>
        <button type="button" onClick={() => onEdit(item)}>
          ✏️
        </button>
        <button type="button">🗑️</button>
      </div>
    </>
  );
}
