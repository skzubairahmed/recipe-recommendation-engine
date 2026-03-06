"use client";
import { useState } from "react";

export default function Home(){
  const [ingredients, setIngredients] = useState('');
  const [recipes, setRecipes] = useState([]);

  const showLimitReachedModal = () => {
    const modal = document.getElementById('limit-reached-modal');
    modal.style.display = 'flex';
  }

  const hideLimitReachedModal = () => {
    const modal = document.getElementById('limit-reached-modal');
    modal.style.display = 'none';
  }

  const searchRecipes = async () => {
    const res = await fetch(`/api/recipes?ingredients=${ingredients}`);
    const data = await res.json();
    console.log(data);
    if(data.response == 402 || data.response == 429 || data.response == 200 || data.status == 500){
      showLimitReachedModal();
      console.log(50000);
    }

    setRecipes(data);
  }

  return(
    <main className="p-8 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6 text-white">
        What's in your fridge ?
      </h1>
      <div className="limitModal" id="limit-reached-modal">
        <div className="modal-card">
          <div className="icon">⚠️</div>
          <h2 className="modal-header">
            API Limit Reached
          </h2>
          <p className="modal-message">
            If you want more of this site then please fund me :(
          </p>
          <button className="close-modal-button" onClick={hideLimitReachedModal}>
            Close
          </button>
        </div>
      </div>
      <div className="flex gap-2 mb-8">
        <input
        className="border p-2 flex-1 rounded text-white"
        placeholder="e.g. cheese, tomato, chicken, milk [separated by commas(,)]"
        onChange={(e) => setIngredients(e.target.value)}
        />
        <button className="bg-orange-500 text-white px-6 py-2 rounded hover:bg-orange-600" onClick={searchRecipes}>
          Find Recipes
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {recipes.map((recipe) => (
          <div key={recipe.id} className="border rounded-lg overflow-hidden shadow-lg bg-white">
            <image src={recipe.image} alt={recipe.title} className="w-full h-48 object-cover" />
            <div className="p-4">
              <h2 className="font-bold text-lg mb-2 text-black line-clamp-1">
                {recipe.title}
              </h2>
              <a 
              href={recipe.sourceUrl}
              target="_blank"
              className="inline-block mt-4 text-orange-600 font-semibold hover:underline"
              >
                View Full Recipe →
              </a>
            </div>
          </div>
        ))}
      </div>
    </main>
  )
}