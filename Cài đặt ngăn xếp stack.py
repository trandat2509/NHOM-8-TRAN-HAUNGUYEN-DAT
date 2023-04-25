class Stack:
    def __init__(self):
        self.items = []  # Khởi tạo một danh sách rỗng để lưu trữ các phần tử của stack.

    def push(self, item):
        self.items.append(item)  # Thêm phần tử vào đầu danh sách.

    def pop(self):
        if not self.is_empty():  # Nếu stack không rỗng.
            return self.items.pop()  # Xóa và trả về phần tử đầu danh sách.

    def peek(self):
        if not self.is_empty():  # Nếu stack không rỗng.
            return self.items[-1]  # Trả về phần tử đầu danh sách.

    def is_empty(self):
        return len(self.items) == 0  # Kiểm tra xem stack có rỗng hay không.

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)  # Trả về số lượng phần tử trong stack.


if __name__ == '__main__':
    stack = Stack()  # Khởi tạo đối tượng stack.

    while True:
        user_input = input("Nhập vào phần tử hoặc nhập 'exit' để kết thúc: ")
        if user_input == "exit":
            break
        else:
            stack.push(user_input)  # Thêm phần tử vào đầu stack.

    print("Các phần tử trong stack là: ")
    while not stack.is_empty():  # Nếu stack không rỗng.
        print(stack.pop())  # In phần tử đầu stack và xóa nó khỏi stack.
