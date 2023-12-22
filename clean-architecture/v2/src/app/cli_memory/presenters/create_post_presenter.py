""" Module for the CreatePostPresenter
"""

from typing import Dict
from src.interactor.dtos.create_post_dtos import CreatePostOutputDto
from src.interactor.interfaces.presenters.create_post_presenter \
    import CreatePostPresenterInterface

class CreatePostPresenter(CreatePostPresenterInterface):
    """ Class for the CreateProfessionPresenter
    """
    def present(self, out_dto: CreatePostOutputDto) -> Dict:
        """ Present the CreatePost
        :param output_dto: CreatePostOutputDto
        :return: Dict
        """
        return {
                    "id": out_dto.post.id,
                    "title": out_dto.post.title,
                    "description": out_dto.post.description,
                    "created_at": out_dto.post.created_at,
                    "updated_at": out_dto.post.updated_at
        }