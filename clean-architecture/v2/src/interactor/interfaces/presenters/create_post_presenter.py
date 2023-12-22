""" Module for the CreatePostPresenterInterface
"""

from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.create_post_dtos import CreatePostOutputDto

class CreatePostPresenterInterface(ABC):
    """Class for the Interface of the PostPresenter
    """
    @abstractmethod
    def present(self, out_dto: CreatePostOutputDto) -> Dict:
        """Present the Post"""