from io import BytesIO


class Reader:
    def __init__(self, buffer_bytes):
        self._sio = BytesIO(buffer_bytes)
        self._temp_buffer = []
        self.row = 0
        self.column = 1

    def read(self):
        char = self._sio.read(1).decode('utf-8')
        self._temp_buffer.append(char)
        self.row += 1
        return char

    def get_temp_buffer(self):
        return self._temp_buffer

    def clear_temp_buffer(self):
        self._temp_buffer.clear()

    def viewNextChar(self):
        char = self._sio.read(1).decode('utf-8')
        if not char:
            return char
        self._sio.seek(-1, 1)
        return char
