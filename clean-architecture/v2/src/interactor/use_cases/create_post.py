""" This module is responsible for creating a new post.
"""
from typing import Dict

from src.interactor.interfaces.presenters.create_post_presenter \
    import CreatePostPresenterInterface
from src.interactor.interfaces.repositories.post_repository \
    import PostRepositoryInterface
from src.interactor.dtos.create_post_dtos import CreatePostInputDto, CreatePostOutputDto

class CreatePostUseCase():
    """ This class is responsible for creating a new post.
    """
    def __init__(
            self, 
            presenter: CreatePostPresenterInterface,
            repository: PostRepositoryInterface
    ):
        self.presenter = presenter
        self.repository = repository

    def execute(
            self,
            input_dto: CreatePostInputDto
    ) -> Dict:
        """ This method is responsible for creating a new post.
        :param input_dto: The input data transfer object.
        :type input_dto: CreatePostInputDto
        :return: Dict
        """
        print(input_dto)
        post = self.repository.create(
            input_dto
        )

        output_dto = CreatePostOutputDto(post)

        return self.presenter.present(output_dto)