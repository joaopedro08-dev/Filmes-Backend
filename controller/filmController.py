from fastapi import APIRouter, HTTPException
from model.films import Film, FilmUpdate
from config.database import collection 
from typing import List
from bson import ObjectId

# Starts the route for building endpoints
router = APIRouter()

# Fixed function for catch the ID
def fix_id(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

# Movies list
@router.get("/films", response_model=List[Film])
def list_films():
    cursor = collection.find().sort("name", 1)
    return [fix_id(f) for f in cursor]

# Search movie by ID
@router.get("/films/{id}", response_model=Film)
def get_movie_by_id(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID in invalid format")
        
    film = collection.find_one({"_id": ObjectId(id)})
    if film:
        return fix_id(film)
    raise HTTPException(status_code=404, detail="Movie not found")

# Add the Movie
@router.post("/films", response_model=Film)
def add_movie(film: Film):
    new_film = film.dict(exclude={"id"}, exclude_unset=True)
    result = collection.insert_one(new_film)
    
    created_film = collection.find_one({"_id": result.inserted_id})
    return fix_id(created_film)

# Update the movie by ID
@router.put("/films/{id}", response_model=Film)
def update_movie(id: str, data: FilmUpdate):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID in invalid format")
    
    update_data = data.dict(exclude_unset=True)
    
    if len(update_data) > 0:
        result = collection.update_one(
            {"_id": ObjectId(id)}, 
            {"$set": update_data}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Movie not found")
    
    updated_film = collection.find_one({"_id": ObjectId(id)})
    return fix_id(updated_film)

# Delete the filme by ID
@router.delete("/films/{id}")
def delete_movie(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="ID in invalid format")
        
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return {"message": "Movie delete successfully!"}
    
    raise HTTPException(status_code=404, detail="Movie not found")