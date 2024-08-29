class HelloDallas:
    def __init__(self, address: str, zip: int):
        self._address = address
        self._zip = zip

    def address(self) -> str:
        return self._address

    def zip(self) -> int:
        return self._zip
