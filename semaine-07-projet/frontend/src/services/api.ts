const token = import.meta.env.VITE_USER_TOKEN;
const url = import.meta.env.VITE_API_URL;

const loadUserData = async () => {
  const response = await fetch(`${url}/me`, {
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`,
    },
  });

  const user = await response.json();

  return { user };
};

const loadBucketItems = async () => {
  const response = await fetch(`${url}/items`, {
    headers: {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`,
    },
  });

  const bucketList = await response.json();

  return { bucketList };
};

export const loadUserAndItems = async () => {
  const [user, bucketList] = await Promise.all([
    loadUserData(),
    loadBucketItems(),
  ]);

  return { ...user, ...bucketList };
};
