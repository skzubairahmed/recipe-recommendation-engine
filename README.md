# Recipe Recommendor

## 👤 Developer
**Developed by:** Zubair  
**Platform:** Deployed via **Vercel**

---

## ✨ Features
* **Smart Ingredient Search:** Input any combination of ingredients (e.g., *chicken, cheese, pepper*).
* **Deep Linking:** Automatically fetches the `sourceUrl` so users get the full original recipe for free.
* **Secure API Handling:** Uses Next.js Serverless Functions to mask private API keys from the client-side.
* **Clean UI:** Minimalist, mobile-responsive interface built for quick kitchen use.

---

## 🛠️ Tech Stack
* **Framework:** [Next.js 14+](https://nextjs.org/) (App Router)
* **Styling:** [Tailwind CSS](https://tailwindcss.com/)
* **Backend:** Next.js API Routes (Node.js runtime)
* **Deployment:** [Vercel](https://vercel.com/)
* **Data Source:** [Spoonacular Food API](https://spoonacular.com/food-api)

---

## 🛣️ Project Routes

| Route | Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | The main dashboard and search interface. |
| `/api/recipes` | `GET` | The "Proxy" route. Takes `?ingredients=...`, fetches IDs from Spoonacular, and returns bulk recipe details including images and source links. |

---