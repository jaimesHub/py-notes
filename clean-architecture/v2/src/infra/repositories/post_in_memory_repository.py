""" Module for PostInMemoryRepository
"""

from typing import Dict
import copy
import uuid
from src.interactor.dtos.create_post_dtos import CreatePostInputDto
from src.interactor.dtos.update_post_dtos import UpdatePostInputDto
from src.domain.entities.post import Post
from src.interactor.interfaces.repositories.post_repository \
    import PostRepositoryInterface
from src.domain.value_objects import PostId

class PostInMemoryRepository(PostRepositoryInterface):
    """In-Memory Repository for Post
    """
    def __init__(self) -> None:
        self._data: Dict[PostId, Post] = {}

    def get(self, post_id: PostId) -> Post:
        """ Get Post by id

        :param post_id: PostId
        :return: Post
        """
        return copy.deepcopy(self._data[post_id])
    
    def create(self, create_post_dto: CreatePostInputDto) -> Post:
        post = Post(
            id=uuid.uuid4(),
            title=create_post_dto.title,
            description=create_post_dto.description,
            created_at=create_post_dto.created_at,
            updated_at=create_post_dto.updated_at
        )

        self._data[post.id] = copy.deepcopy(post)

        return copy.deepcopy(self._data[post.id])
    
    def update(self, update_post_dto: UpdatePostInputDto) -> Post:
        self._data[update_post_dto.id] = copy.deepcopy(update_post_dto)
        return copy.deepcopy(self._data[update_post_dto.id])