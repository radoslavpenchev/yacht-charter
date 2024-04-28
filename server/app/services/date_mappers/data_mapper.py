from abc import ABC, abstractmethod
from typing import List


class DataMapper(ABC):
    @abstractmethod
    def to_entity(self, model):
        raise NotImplementedError()

    @abstractmethod
    def to_model(self, entity):
        raise NotImplementedError()

    def to_entities(self, models: List) -> List:
        return [self.to_entity(model=model) for model in models]

    def to_models(self, entities) -> List:
        return [self.to_model(entity=entity) for entity in entities]
