import { useState } from "react";
import { Edit } from "../../../public/Edit";
import { Trash } from "../../../public/Trash";
import type { ItemType } from "../../types/types";

export default function Item({
  item,
  token,
  url,
  onEdit,
  onDelete,
}: {
  item: ItemType;
  token: string;
  url: string;
  onEdit: (item: ItemType) => void;
  onDelete: (item: ItemType) => void;
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
          <Edit />
        </button>
        <button type="button" onClick={() => onDelete(item)}>
          <Trash />
        </button>
      </div>
    </>
  );
}
