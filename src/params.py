from pydantic import BaseModel, Field
from typing import Dict, Any

class Model_Params(BaseModel):
    '''Class for Model Parameters '''
    n_estimators: int = Field(default = 500, description = 'Numbers of Iterations')
    random_state: int = Field(default = 42, description = 'Static State of Change')
    criterion: str = Field(default = 'log_loss', description = 'Type of Optimizer')
    n_jobs: int = Field(default = -1, description = ' Number of CPU Cores to Use')
    class_weight: str = Field(default = 'balanced', description = 'State Of Class Distribution')


    def to_dict(self) -> Dict[str, Any]:
        return self.dict()
