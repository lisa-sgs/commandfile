from pathlib import Path

import yaml

from commandfile.argparse import CommandfileArgumentParser
from commandfile.model import Commandfile, Filelist, Parameter


def write_cmdfile(cmdfile: Commandfile, tmp_path: Path) -> str:
    path = tmp_path / "commandfile.yaml"
    with open(path, "w") as f:
        yaml.dump(cmdfile.model_dump(), f, default_flow_style=False)
    return str(path)


def test_standard_arguments():
    parser = CommandfileArgumentParser()
    parser.add_argument("--some-arg", type=int)
    args = parser.parse_args(["--some-arg", "42"])
    assert args.some_arg == 42


def test_commandfile_parameter(tmp_path: Path):
    cmdfile = Commandfile(
        header={},
        parameters=[Parameter(key="some-arg", value="42")],
        inputs=[],
        outputs=[],
    )
    parser = CommandfileArgumentParser()
    parser.add_argument("--some-arg", type=int)
    args = parser.parse_args(["--commandfile", write_cmdfile(cmdfile, tmp_path)])
    assert args.some_arg == 42


def test_commandfile_parameter_override(tmp_path: Path):
    cmdfile = Commandfile(
        header={},
        parameters=[Parameter(key="some-arg", value="42")],
        inputs=[],
        outputs=[],
    )
    parser = CommandfileArgumentParser()
    parser.add_argument("--some-arg", type=int)
    args = parser.parse_args(
        ["--commandfile", write_cmdfile(cmdfile, tmp_path), "--some-arg", "100"]
    )
    assert args.some_arg == 100


def test_commandfile_filelist(tmp_path: Path):
    cmdfile = Commandfile(
        header={},
        parameters=[],
        inputs=[
            Filelist(
                key="some-file-input",
                files=["file1.txt", "file2.txt"],
            ),
        ],
        outputs=[],
    )
    parser = CommandfileArgumentParser()
    parser.add_argument("--some-file-input", type=str, nargs="+")
    args = parser.parse_args(["--commandfile", write_cmdfile(cmdfile, tmp_path)])
    assert args.some_file_input == ["file1.txt", "file2.txt"]


def test_commandfile_empty_filelist(tmp_path: Path):
    cmdfile = Commandfile(
        header={},
        parameters=[],
        inputs=[
            Filelist(
                key="some-file-input",
                files=[],
            ),
        ],
        outputs=[],
    )
    parser = CommandfileArgumentParser()
    parser.add_argument("--some-file-input", type=str, nargs="*")
    args = parser.parse_args(["--commandfile", write_cmdfile(cmdfile, tmp_path)])
    assert args.some_file_input == []
