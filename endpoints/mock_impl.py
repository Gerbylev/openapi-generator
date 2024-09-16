from endpoints.apis.mock_api_base import BaseMockApi
from endpoints.models.create_mock_data import CreateMockData
from endpoints.models.mock_data_response import MockDataResponse
from endpoints.models.response_create_mock import ResponseCreateMock


class MockImpl(BaseMockApi):
    data = [MockDataResponse(id=1, info="hello world!"), MockDataResponse(id=2, info="bye world!")]

    async def add_mock(self, create_mock_data: CreateMockData) -> ResponseCreateMock:
        new_id = max(mock.id for mock in self.data) + 1  #
        new_mock = MockDataResponse(id=new_id, info=create_mock_data.info)
        self.data.append(new_mock)
        return ResponseCreateMock(id=new_id)

    async def mock(self, id: int) -> MockDataResponse:
        for mock in self.data:
            if mock.id == id:
                return mock
        raise ValueError("Data with given ID not found.")

