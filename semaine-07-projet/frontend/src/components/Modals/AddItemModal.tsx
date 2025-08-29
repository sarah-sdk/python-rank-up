import { type FormEvent, useEffect, useRef, useState } from "react";
import type { ItemType } from "../../types/types";

export default function AddItemModal({
  isOpen,
  onClose,
  onSubmit,
}: {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (item: Omit<ItemType, "id">) => void;
}) {
  const dialogRef = useRef<HTMLDialogElement>(null);

  const [formData, setFormData] = useState<Omit<ItemType, "id">>({
    name: "",
    done: false,
    category: "",
  });

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
              done: e.target.checked,
            }));
          }}
        />

        <button type="submit">Ajouter</button>
        <button
          type="button"
          onClick={() => {
            dialogRef.current?.close();
            onClose();
          }}
        >
          Annuler
        </button>
      </form>
    </dialog>
  );
}
