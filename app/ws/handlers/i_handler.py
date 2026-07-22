from abc import ABC, abstractmethod

class IHandler(ABC):
    @abstractmethod
    async def handle(self, data: dict, gateway_id: int, session):
        pass
