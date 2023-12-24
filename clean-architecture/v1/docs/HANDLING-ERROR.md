# Error Handling, Logging and Validation
This note talks about error handling, logging and validation, including some Python best practices around these topics.

## Why is Error Handling Important?
- Our program should not crash if an error occurs and we should show a meaningful message to the user as much as possible.
    - It helps the user can check the message and correct the problem without asking for assistance from author's project
- Good Error Handling will help developers and software support debug and solve problems.

## Python Error Handling Best Practices

### Never ignore errors
- [bad-practice](../examples/never_ignore_errors.py)
- We should let the user know we have a problem

### Handle Specific Errors
- [Never catch all errors like in this example](../examples/handle_specific_errors.py)
- With this code above it is more difficult to debug, especially when the problem is not something obvious

### Why is Data Validation Important?
- Data Validation is important to verify if the data received by the use case is what the business rules define.
- It is also good practice to define appropriate messages and show these to users

### Cerberus Data Validation Library
- With Cerberus, we can define the rules that the data should have.
- Cerberus validates the data considering the rules we defined and provides personalized error messages depending on the specific field and rule violated.

### Why Logging?
- It is critical to have logging capabilities in a production environment to facilitate the support, monitoring and debugging of the application.

### The Logging Python Module
- The logging Python module is used to log messages to a file
- It has five standard levels in order of severity
    - debug
    - info
    - warning
    - error
    - critical
- We can also use any of the severity level functions with the parameter `exc_info=True`
- While logging, pay attention not to log sensitive information such as social security numbers, passwords and credit card numbers.

### Logging Configuration
To configure the logging Python module, we call the `basicConfig` function. We can pass these parameters:

- filename: We pass the filename parameter to set the filename to save the logs
- filemode: It can be w (to rewrite the file), or a (to append)
- level: Severity level. For instance, if we set the level to logging.ERROR, only error and critical messages will be saved.
- datefmt: To set the datetime format
- format: To define the format saved in the file. Here are some possibilities:
    - %(asctime)s: To show the logging time
    - %(message)s: The most meaningful part, the message we want to log

### The implementation in Clean Architecture
- The `BaseInputValidator` Class & The `BaseInputValidator` Class Tests
    - [validations](../src/interactor/validations/)
        - [base_input_validator.py](../src/interactor/validations/base_input_validator.py)
        - [base_input_validator_test.py](../src/interactor/validations/base_input_validator_test.py)

- A Personalized Exception Class & Personalized Exception Class Test
Here we define a personalized exception class for a case that is beyond the scope of the Cerberus library
    - [errors](../src/interactor/errors/)
        - [error_classes.py](../src/interactor/errors/errors_classes.py)
        - [errpr_classes_test.py](../src/interactor/errors/errors_classes_test.py)

- The `CreateProfessionInputDtoValidator` Class
    - [create_prfession_validator.py](../src/interactor/validations/create_profession_validator.py)
    - [create_prfession_validator_test.py](../src/interactor/validations/create_profession_validator_test.py)

- The `LoggerInterface`: [interactor/interfaces/logger](../src/interactor/interfaces/logger/)
    - [logger.py](../src/interactor/interfaces/logger/logger.py)

- The `LoggerDefault` class
    - The `LoggerDefault` class uses the abstract class `LoggerInterface`, configures and uses the Python logging method to implement our logging system
    - [infra/loggers]
    - [logger_default.py](../src/infra/loggers/logger_default.py)

- The `LoggerDefault` class tests
    - [logger_default_test.py](../src/infra/loggers/logger_default_test.py)

- The new version of the `CreateProfessionUseCase` class
    - We updated the `CreateProfessionUseCase` class, calling the `validate` method of the `CreateProfessionInputDtoValidator` class. 
    - We also added the "`Profession created successfully`" message.
    - Update: [create_profession.py](../src/interactor/use_cases/create_profession.py)

- The New Version of the `CreateProfessionUseCase` Class Test
    - Update: [create_profession_test.py](../src/interactor/use_cases/create_profession_test.py)

- The new version of `CliMemoryProcessHandler`
    - Added `exception` handling and `logging`
    - Update: [cli_memory_process_handler.py](../cli_memory_process_handler.py)

# References
- [Part 2](https://www.linkedin.com/pulse/implementation-clean-architecture-python-part-2-error-watanabe/)