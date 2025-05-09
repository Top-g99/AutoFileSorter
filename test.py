def test_create_folder(tmp_path):
    from sorter.utils import create_folder
    test_folder = tmp_path / "test"
    create_folder(test_folder)
    assert test_folder.exists()
