from commandfile.model_generated import (
    Commandfile as BaseCommandfile,
)
from commandfile.model_generated import (
    Filelist,
    Parameter,
)


class Commandfile(BaseCommandfile):
    """Extended Commandfile model with helper methods."""

    def find_parameter(self, key: str) -> Parameter:
        """Find a parameter by its key."""
        for param in self.parameters:
            if param.key == key:
                return param
        raise KeyError(f"Parameter {key!r} not found")

    def find_filelist(self, key: str) -> Filelist:
        raise NotImplementedError()
