from .routes.Breed import Breed
from .routes.Breeds import Breeds

class PyDogCeo:
    """Main Class"""
    def __init__(self) -> None:
        self._breed = Breed()
        self._breeds = Breeds()

    @property
    def breed(self) -> Breed:
        """Interface to the breed endpoints

        Returns:
            Breed:
        """
        return self._breed

    @property
    def breeds(self) -> Breeds:
        """Interface to the breeds endpoints

        Returns:
            Breeds:
        """
        return self._breeds
