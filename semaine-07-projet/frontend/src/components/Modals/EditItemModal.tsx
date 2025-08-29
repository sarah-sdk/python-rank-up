import { type FormEvent, useEffect, useRef, useState } from "react";
import type { ItemType } from "../../types/types";

export default function EditItemModal({
  item,
  isOpen,
  onClose,
  onSubmit,
}: {
  item: ItemType;
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (item: ItemType) => void;
}) {
  const dialogRef = useRef<HTMLDialogElement>(null);

  const [formData, setFormData] = useState<ItemType>({
    id: 0,
    name: "",
    done: false,
    category: "",
  });

  useEffect(() => {
    if (item) {
      setFormData(item);
    }
  }, [item]);

  useEffect(() => {
    if (isOpen) {
      dialogRef.current?.showModal();
    }
  }, [isOpen]);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    await onSubmit(formData);
    dialogRef.current?.close();
  };

  return (
    <dialog ref={dialogRef}>
      <h3>Modifer un item</h3>
      <form method="dialog" onSubmit={handleSubmit}>
        <label htmlFor="nameItem">Nom de l'item : </label>
        <input
          type="text"
          id="nameItem"
          value={formData.name}
          onChange={(e) => {
            setFormData((prev) => ({ ...prev, name: e.target.value }));
          }}
          required
        />

        <label htmlFor="select-category">Catégorie : </label>
        <select
          name="categories"
          id="select-category"
          value={formData.category}
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
          checked={formData.done}
          onChange={(e) => {
            setFormData((prev) => ({
              ...prev,
              done: e.target.checked,
            }));
          }}
        />

        <button type="submit">Ajouter</button>
        <button type="button" onClick={onClose}>
          Annuler
        </button>
      </form>
    </dialog>
  );
}
