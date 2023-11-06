# Coderetreat 2023 - Game of Life

## Prerequisites

- Python 3.x
- [pytest](https://pytest.org/)
- [pytest-cov](https://pypi.org/project/pytest-cov/)
- [pytest-mock](https://pypi.org/project/pytest-mock/) (version 3.3.1)
- [pygame](https://www.pygame.org/)

You can install these dependencies using `pip`:

```bash
pip install pytest pytest-cov pytest-mock==3.3.1 pygame
```

## Project Structure

The project has the following structure:

```
coderetreat-2023-game-of-life/
├── app/
│   └── main.py
├── tests/
│   └── test_gol.py
├── README.md
```

- `app/main.py`: This is the main file of the Game of Life application.
- `tests/test_gol.py`: This is the test suite for the Game of Life.

## Running Tests

We use `pytest` for running our tests. To execute the test suite, open a terminal, navigate to the project's root directory, and run the following command:

```bash
pytest
```

This will discover and run all the tests in the `tests/` directory. The `pytest-cov` plugin is also included, which will generate code coverage reports.

## Running the Game

To run the Game of Life, you can execute `main.py`:

```bash
python app/main.py
```

This will launch the Game of Life application using the `pygame` library. 

## Additional Information


Have a great time coding at Coderetreat 2023, and enjoy working on the Game of Life project! If you have any questions or need further assistance, don't hesitate to reach out to the organizers or your fellow participants.
```

You can copy and paste this code block as your README.md.
