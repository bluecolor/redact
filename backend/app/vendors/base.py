from abc import ABC, abstractmethod
from typing import List, Optional, Any
from app.models.orm import Connection
from app.models.schemas import MetadataOut, Schema, Table, Column


class VendorABC(ABC):
    @abstractmethod
    def connect(self) -> Any:
        ...

    @abstractmethod
    def get_users(self) -> Any:
        ...

    @abstractmethod
    def execute(self, stmt: str):
        ...

    @abstractmethod
    def get_schemas(self) -> List[Schema]:
        ...

    @abstractmethod
    def get_tables(self, schema_name: Optional[str]) -> List[Table]:
        ...

    @abstractmethod
    def get_columns(
        self, schema_name: Optional[str], table_name: Optional[str],
    ) -> List[Column]:
        ...

    @abstractmethod
    def fetchall(self, cursor, lower_keys):
        ...

    @abstractmethod
    def queryall(self, query: str, lower_keys=True) -> List[dict]:
        ...

    @abstractmethod
    def ping(self):
        ...

    @abstractmethod
    def callproc(self, proc: str, params: Optional[dict] = dict(),) -> Any:
        ...

    @abstractmethod
    def search(self, q: str) -> List[MetadataOut]:
        ...


class Vendor(VendorABC):
    def __init__(self, config: Connection, *args, **kwargs) -> None:
        self.config = config

    def fetchall(self, cursor, lower_keys=True):
        columns = [
            col[0].lower() if lower_keys else col[0]
            for col in cursor.description
        ]
        rows = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return rows

    def execute(self, stmt: str):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(stmt)
            conn.commit()

    def queryall(self, query: str, lower_keys=True) -> List[dict]:
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            result = self.fetchall(cursor=cursor, lower_keys=lower_keys)
            cursor.close()
        return result

    def ping(self):
        result = False
        with self.connect() as conn:
            try:
                result = True
            except Exception as e:
                print(e)
                result = False
        return result

    def callproc(self, proc: str, params: Optional[dict] = dict(),) -> Any:
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.callproc(proc, keywordParameters=params)
            cursor.close()
