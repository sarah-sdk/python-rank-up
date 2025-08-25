// Import necessary modules from React and React Router
import { createRoot } from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";

/* ************************************************************************* */
import App from "./App";
import "./index.css";
/* ************************************************************************* */
const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
]);
/* ************************************************************************* */

const rootElement = document.getElementById("root");
if (rootElement == null) {
  throw new Error(`Your HTML Document should contain a <div id="root"></div>`);
}

createRoot(rootElement).render(<RouterProvider router={router} />);
