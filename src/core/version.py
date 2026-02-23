from dataclasses import dataclass

@dataclass(frozen=True)
class Version:
    major: int
    minor: int
    patch: int
    status: str
    build: str

    @property
    def text(self) -> str:
        version = f"{self.major}.{self.minor}.{self.patch}"
        return f"{version}.{self.status}.{self.build}"

    @staticmethod
    def from_text(version: str) -> "Version":
        parts = version.split(".")
        major = int(parts[0])
        minor = int(parts[1])
        patch = int(parts[2])
        status = parts[3]
        build = parts[4]
        return Version(major, minor, patch, status, build)