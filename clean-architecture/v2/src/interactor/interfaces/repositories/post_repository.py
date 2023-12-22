""" This module contains the interface for the PostRepository
"""

from abc import ABC, abstractmethod
from src.domain.value_objects import PostId
from src.domain.entities.post import Post
from src.interactor.dtos.create_post_dtos import CreatePostInputDto, CreatePostOutputDto
from src.interactor.dtos.update_post_dtos import UpdatePostInputDto, UpdatePostOutputDto

class PostRepositoryInterface(ABC):
    """This class is the Interface for the PostRepository
    """

    @abstractmethod
    def get(self, post_id: PostId) -> Post:
        """ Get a Post by id
        :param post_id: PostId
        :return: Post
        """

    @abstractmethod
    def create(self, create_post_dto: CreatePostInputDto) -> Post:
        """Create a Post
        :param create_post_dto: CreatePostInputDto
        :return: CreatePostOutputDto
        """

    @abstractmethod
    def update(self, update_post_dto: UpdatePostInputDto) -> Post:
        """Update a Post
        :param update_post_dto: UpdatePostInputDto
        :return UpdatePostOutputDto
        """

    # @abstractmethod
    # def delete(self, post_id: PostId) -> Post:
    #     """Delete a Post
    #     :param post_id: PostId
    #     :return: Post
    #     """
