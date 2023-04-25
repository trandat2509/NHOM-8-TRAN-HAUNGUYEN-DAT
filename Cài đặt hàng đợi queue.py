class Queue:
    def __init__(self):
        self.items = []  # Tạo một danh sách trống để lưu trữ các phần tử của hàng đợi

    def enqueue(self, item):
        self.items.append(item)  # Thêm phần tử vào cuối danh sách

    def dequeue(self):
        return self.items.pop(0)  # Xóa phần tử đầu tiên khỏi danh sách và trả về giá trị đã bị xóa

    def isEmpty(self):
        return self.items == []  # Trả về True nếu danh sách rỗng và False nếu ngược lại

    def size(self):
        return len(self.items)  # Trả về số lượng phần tử trong danh sách

    def front(self):
        return self.items[0]  # Trả về phần tử đầu tiên của danh sách, không xóa phần tử này ra khỏi danh sách

# Sử dụng hàng đợi để lưu trữ các chuỗi nhập vào từ bàn phím
queue = Queue()
n = int(input("Nhập số lượng phần tử cần thêm vào hàng đợi: "))
for i in range(n):
    item = input("Nhập phần tử {}: ".format(i+1))
    queue.enqueue(item)

# Lưu giữ kích thước của hàng đợi
queue_size = queue.size()

# In ra các phần tử của hàng đợi theo thứ tự FIFO
print("Các phần tử trong hàng đợi theo thứ tự FIFO:")
while not queue.isEmpty():
    print(queue.front())
    queue.dequeue()

# In kích thước của hàng đợi
print("Kích thước của hàng đợi:", queue_size)
