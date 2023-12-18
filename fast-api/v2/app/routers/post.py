from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     # query = db.query(models.Post)
#     # print(query)
#     return {"status": "success", "data": posts}

"""
Using fastapi's decorator make this function turn into a special path operation function
"""
@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.Post]) # the first matches path operation
def get_posts(
    db: Session = Depends(get_db), 
    current_user = Depends(oauth2.get_current_user),
    limit: int = 10,
    skip: int = 0,
    search: Optional[str] = ""
): # path operation function
    
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()

    # print(current_user)
    # query_statement = db.query(models.Post).filter(models.Post.owner_id == current_user.id)
    query_statement = db.query(models.Post)

    # posts = query_statement.all()
    posts = query_statement.filter(models.Post.title.contains(search)).limit(limit=limit).offset(offset=skip).all()
    
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    #                (post.title, post.content, post.published))
    
    # new_post = cursor.fetchone()

    # conn.commit()
    # print(**post.dict())

    # new_post = models.Post(
    #     title=post.title, 
    #     content=post.content, 
    #     published=post.published
    # )

    # If we have more than 50 fields
    # new_post = models.Post(**post.dict()) # error when we added more column: owner_id
    new_post = models.Post(owner_id=current_user.id, **post.dict())

    db.add(new_post)
    db.commit()
    db.refresh(new_post) # == RETURNING *
    
    return new_post

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    """Order does matter"""
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (id, ))
    # post = cursor.fetchone()

    query_statement = db.query(models.Post).filter(models.Post.id == id)
    post = query_statement.first()

    # query = db.query(models.Post).filter(models.Post.id == id)
    # print(query)
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id:{id} was not found!")
    
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorize to perform requested action")

    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (id, ))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    query_statement = db.query(models.Post).filter(models.Post.id == id)

    deleted_post = query_statement.first()

    # query = db.query(models.Post).filter(models.Post.id == id)
    # print(query)
    
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"The id:{id} does not exist!")
    
    # permission to delete
    if deleted_post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorize to perform requested action")
    
    query_statement.delete(synchronize_session=False)
    
    # db.delete(deleted_post)

    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostUpdate, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", 
    # (post.title, post.content, post.published, id))

    # updated_post = cursor.fetchone()

    # conn.commit()

    query_statement = db.query(models.Post).filter(models.Post.id == id)

    post = query_statement.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"The post has id:{id} does not exist")
    
    # query.update({
    #     "title": "hey this is my updated title",
    #     "content": "this is my updated content"
    # }, synchronize_session=False)

    # permission to update
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorize to perform requested action")

    query_statement.update(updated_post.dict(), synchronize_session=False)

    db.commit()

    updated_post = query_statement.first()
    
    return updated_post