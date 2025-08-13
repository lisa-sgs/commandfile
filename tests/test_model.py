from pathlib import Path

from commandfile.model import Commandfile, Parameter


def test_find_parameter(commandfile_path: Path):
    cmdfile = Commandfile(
        header={},
        parameters=[Parameter(key=f"param-{i}", value=i) for i in range(10)],
        inputs=[],
        outputs=[],
    )
    param = cmdfile.find_parameter("param-7")
    assert param.key == "param-7"
    assert param.value == 7
