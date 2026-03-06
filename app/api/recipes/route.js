import { NextResponse } from "next/server";

export async function GET(request){
    const {searchParams} = new URL(request.url);
    const ingredients = searchParams.get('ingredients');
    const apiKey = process.env.SPOONACULAR_API_KEY;

    const result = await fetch(
        `https://api.spoonacular.com/recipes/findByIngredients?ingredients=${ingredients}&number=9&apiKey=${apiKey}`
    );

    const recipes = await result.json();
    if(!Array.isArray(recipes)){
        return NextResponse.json({"error":"Unexpected API response format."}), {status:500};
    }

    const ids = recipes.map(r => r.id).join(',');
    const infoRes = await fetch(
        `https://api.spoonacular.com/recipes/informationBulk?ids=${ids}&apiKey=${apiKey}`
    );

    const detailedRecipes = await infoRes.json();

    return NextResponse.json(detailedRecipes);
}