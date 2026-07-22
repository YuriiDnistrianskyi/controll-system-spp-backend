from abc import ABC, abstractmethod

class IAuthHandler(ABC):
    @abstractmethod
    async def handle(self, data: dict, session):
        pass
