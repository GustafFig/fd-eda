from dataclasses import dataclass
import uuid

@dataclass(frozen=True, kwargs=True)
class Balance():
    id: uuid.UUIDV4
    value: int
