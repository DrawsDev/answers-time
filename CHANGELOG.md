# Changelog
All notable changes will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.5] - 2024-11-13
### Added
- CHANGELOG.ru.md;
- New methods in the `Dialogue` class from the component `dialogue.py`:
  - `is_typing_finished` allows you to know whether the text is typed or not;
  - `skip_typing` allows you to skip typing text;
  - `get_text_from_lines` allows you to get the total text from a list with `Line`.

### Changed
- The new `Dialogue` functionality is demonstrated in `intro.py`.

## [0.0.4] - 2024-11-12
### Added
- New component - `dialogue.py`: classes `Dialogue` and `Line` to replace the spaghetti code in `intro.py`:
  - `Line` contains the text and the effects that will be applied to it;
  - `Dialogue` is used to display the `Line` with effects.
- New `etu_voice` sound, which is being used experimentally in the `Dialogue`.

### Removed
- Experimental label tags from the `intro.py` (spaghetti code too).

## [0.0.3] - 2024-11-11
### Added
- New core `timer.py`: class `Timer`;
- New font Ramona-Bold;
- Experimental label tags in `intro.py` (spaghetti code :D):
  - The `[rgb]` tag makes the text move in waves and shimmer with all colors;
  - The `[shake]` tag makes the text shake and turn red;
  - The `[/]` tag will make plain text.
- Getters and setters in the `label.py` to the `FontParams` class:
  - fontpath;
  - size;
  - color;
  - align;
  - wraplength.

## [0.0.2] - 2024-11-10
### Added
- CHANGELOG.md;
- New core `utility.py`: functions `clamp` and `lerp`;
- New component `label.py`: classes `Label` and `FontParams`;
- New `hand_1` sprite.

### Changed
- New `Label` and `FontParams` are demonstrated in `intro.py`.

## [0.0.1] - 2024-10-05
### Added
- A full rework of the project in python 3.8.10 has begun!
