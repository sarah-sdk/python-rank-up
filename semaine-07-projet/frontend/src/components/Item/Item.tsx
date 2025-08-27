import { useState } from "react";
import { Checked, Unchecked } from "../../../public/Checkbox";
import type { ItemType } from "../../types/types";

export default function Item({ item }: { item: ItemType }) {
  const [isChecked, setIsChecked] = useState<boolean>(item.done);

  const handleChecked = () => {
    setIsChecked(!isChecked);
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
