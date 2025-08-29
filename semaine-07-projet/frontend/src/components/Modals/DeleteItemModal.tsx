import { type FormEvent, useEffect, useRef, useState } from "react";
import type { ItemType } from "../../types/types";

export default function DeleteItemModal({
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
      <form method="dialog" onSubmit={handleSubmit}>
        <h1>Êtes-vous sûr de vouloir supprimer cet item ?</h1>
        <button type="submit">Oui</button>
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
