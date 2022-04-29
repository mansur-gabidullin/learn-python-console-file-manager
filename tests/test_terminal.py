import json

from src.terminal.utils import resolve_json_file_path, save_json, is_exists, read_json, remove_file


def test_save_json():
    import os

    test_file_name = 'test_json_file'
    test_data = {'key': 'value'}
    root_path = os.path.normpath(os.path.join(__file__, '../test_data'))
    file_path = resolve_json_file_path(test_file_name, root_path=root_path)

    remove_file(file_path)

    assert not is_exists(file_path)

    save_json(test_file_name, test_data, root_path=root_path)

    assert is_exists(file_path)

    content = read_json(test_file_name, root_path=root_path)

    assert test_data == content

    remove_file(file_path)
