from app.services.dataset_service import DatasetService

# ----------------------------------------
# Teste - Lista os datasets disponíveis.
# ----------------------------------------
def test_list_datasets_returns_list():
    result = DatasetService.list_datasets()
    assert isinstance(result, list)

# ----------------------------------------
# Teste - Adiciona um novo dataset.
# ----------------------------------------
def test_add_dataset_creates_file(tmp_path): 
    dataset_name = "test_dataset"
    dataset_path = tmp_path / f"{dataset_name}.csv"

    DatasetService.add_dataset(dataset_name, "id:int,value:str", base_path=tmp_path)

    assert dataset_path.exists()