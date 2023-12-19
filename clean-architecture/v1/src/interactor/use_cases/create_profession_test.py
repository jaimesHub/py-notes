from src.interactor.use_cases import create_profession
from src.domain.entities.profession import Profession
from src.interactor.dtos.create_profession_dtos \
    import CreateProfessionInputDto, CreateProfessionOutputDto
from src.interactor.interfaces.presenters.create_profession_presenter \
    import CreateProfessionPresenterInterface
from src.interactor.interfaces.repositories.profession_repository \
    import ProfessionRepositoryInterface

def test_create_profession(mocker, fixture_profession_developer):
    profession = Profession(
        profession_id=fixture_profession_developer["profession_id"],
        name=fixture_profession_developer["name"],
        description=fixture_profession_developer["description"]
    )

    presenter_mock = mocker.patch.object(
        CreateProfessionPresenterInterface,
        "present"
    )

    repository_mock = mocker.patch.object(
        ProfessionRepositoryInterface,
        "create"
    )

    repository_mock.create.return_value = profession
    presenter_mock.present.return_value = "Test output"
    use_case = create_profession.CreateProfessionUseCase(
        presenter_mock,
        repository_mock
    )

    create_profession_input_dto = CreateProfessionInputDto(
        name=fixture_profession_developer["name"],
        description=fixture_profession_developer["description"]
    )

    result = use_case.execute(create_profession_input_dto)

    repository_mock.create.assert_called_once()

    output_dto = CreateProfessionOutputDto(profession)
    presenter_mock.present.assert_called_once_with(output_dto)
    
    assert result == "Test output"