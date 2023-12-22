"""Create Post Controller Module"""

from src.app.cli_memory.interfaces.cli_memory_controller_interface \
    import CliMemoryControllerInterface
from src.interactor.dtos.create_post_dtos import CreatePostInputDto
from src.infra.repositories.post_in_memory_repository \
    import PostInMemoryRepository
from ..presenters.create_post_presenter import CreatePostPresenter
from ..views.create_post_view import CreatePostView
from src.interactor.use_cases.create_post import CreatePostUseCase
from datetime import datetime
class CreatePostController(CliMemoryControllerInterface):
    """ Create Post Controller Class
    """
    def _get_post_info(self) -> CreatePostInputDto:
        title = input("Enter the post title:")
        description = input("Enter the post description:")
        created_at = datetime.now()
        updated_at = datetime.now()
        return CreatePostInputDto(title, description, created_at, updated_at)
    
    def execute(self):
        """ Execute the create profession controller
        """
        repository = PostInMemoryRepository()
        presenter = CreatePostPresenter()
        input_dto = self._get_post_info()
        use_case = CreatePostUseCase(presenter, repository)
        result = use_case.execute(input_dto)
        view = CreatePostView()
        view.show(result)