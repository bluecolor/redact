from typing import Optional
from pydantic import BaseModel


class ColumnOut(BaseModel):
    object_owner: str
    object_name: str
    column_name: str
    function_type: str
    function_parameters: Optional[str]
    regexp_pattern: Optional[str]
    regexp_replace_string: Optional[str]
    regexp_position: Optional[int]
    regexp_occurance: Optional[int]
    regexp_match_parameter: Optional[str]
    column_description: Optional[str]
