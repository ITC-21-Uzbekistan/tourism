class CommonResult:
    def __init__(self):
        self.success = False
        self.message = "Try again later"
        self.data = None

    def write_message(self, message):
        self.message = message

    def set_true(self, data):
        self.success = True
        self.message = "SUCCESS"
        self.data = data


class CommonMessageResult:
    def __init__(self):
        self.success = False
        self.message = "Try again later"

    def set_true(self):
        self.success = True
        self.message = "SUCCESS"

    def write_msg(self, message):
        self.message = message
