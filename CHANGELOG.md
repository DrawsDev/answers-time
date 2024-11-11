# Changelog
All notable changes will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.3] - 2024-11-11
### Added
- New core `timer.py`: class `Timer`;
- New font Ramona-Bold.

### Changed
- Tags in labels are tested in `intro.py` (spaghetti code :D):
  - The `[rgb]` tag makes the text move in waves and shimmer with all colors;
  - The `[shake]` tag makes the text shake and turn red;
  - The `[/]` tag will make plain text.
- Added getters and setters in the `label.py` to the `FontParams` class:
  - fontpath;
  - size;
  - color;
  - align;
  - wraplength.

## [0.0.2] - 2024-11-10
### Added
- CHANGELOG.md;
- New core `utility.py`: functions `clamp` and `lerp`;
- New component `label.py`: classes `Label` and `FontParams`.

### Changed
- New hand sprite; 
- New labels are being tested in `intro.py`.

## [0.0.1] - 2024-10-05
### Added
- A full rework of the project in python 3.8.10 has begun!
