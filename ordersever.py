class OrderService:
    def __init__(self):
        # Danh sách lưu trữ các món đã gọi trong đơn hàng hiện tại
        self.current_order = []

    def add_dish_to_order(self, product: dict, spice_level: int, quantity: int) -> str:
        """
        Hàm Service xử lý gọi món:
        - product: Thông tin món ăn dưới dạng từ điển (dictionary), ví dụ:
          {'id': 'P01', 'name': 'Mì Kim Chi Hải Sản', 'price': 49000, 'is_available': True}
        - spice_level: Cấp độ cay (yêu cầu từ 0 đến 7)
        - quantity: Số lượng gọi (phải lớn hơn 0)
        """
        # 1. Kiểm tra trạng thái món (còn hàng / hết hàng)
        if not product or not product.get("is_available", False):
            dish_name = product.get('name', 'Món ăn không xác định') if product else 'Món ăn'
            return f"Lỗi: Món '{dish_name}' hiện tại đã HẾT! Vui lòng chọn món khác."

        # 2. Kiểm tra cấp độ cay hợp lệ (từ 0 đến 7 theo quy định bảng SpiceLevels)
        if not isinstance(spice_level, int) or not (0 <= spice_level <= 7):
            return "Lỗi: Cấp độ cay không hợp lệ! Vui lòng chọn từ cấp độ 0 đến cấp 7."

        # 3. Kiểm tra số lượng gọi món
        if not isinstance(quantity, int) or quantity <= 0:
            return "Lỗi: Số lượng món phải lớn hơn 0."

        # 4. Gắn cấp độ cay, tính thành tiền và thêm vào danh sách đơn hàng
        subtotal = product["price"] * quantity
        order_item = {
            "product_id": product["id"],
            "name": product["name"],
            "spice_level": spice_level,
            "quantity": quantity,
            "unit_price": product["price"],
            "subtotal": subtotal
        }
        
        self.current_order.append(order_item)
        return f"Thành công: Đã thêm {quantity}x [{product['name']} - Cấp độ cay {spice_level}] vào đơn hàng."

    def calculate_total_order(self) -> float:
        """Tính tổng tiền toàn bộ các món trong đơn hàng"""
        return sum(item["subtotal"] for item in self.current_order)

    def get_order_details(self) -> list:
        """Lấy danh sách chi tiết đơn hàng hiện tại"""
        return self.current_order


# ==========================================
# KHU VỰC CHẠY THỬ (TEST CASE)
# ==========================================
if __name__ == "__main__":
    # Khởi tạo Service
    service = OrderService()

    # Giả lập dữ liệu món ăn trong CSDL (Products & SpiceLevels)
    mon_con_hang = {"id": "P01", "name": "Mì Kim Chi Hải Sản", "price": 49000, "is_available": True}
    mon_het_hang = {"id": "P02", "name": "Mì Kim Chi Bò Mỹ", "price": 52000, "is_available": False}

    print("--- KIỂM TRA CHỨC NĂNG ORDER SERVICE ---")
    
    # Test 1: Gọi món còn hàng, chọn cấp độ cay hợp lệ (Cấp 3) -> Kỳ vọng: Thành công
    print(service.add_dish_to_order(mon_con_hang, spice_level=3, quantity=2))

    # Test 2: Gọi món đã hết hàng -> Kỳ vọng: Báo lỗi hết món
    print(service.add_dish_to_order(mon_het_hang, spice_level=2, quantity=1))

    # Test 3: Chọn cấp độ cay vượt mức cho phép (Cấp 9) -> Kỳ vọng: Báo lỗi cấp độ cay
    print(service.add_dish_to_order(mon_con_hang, spice_level=9, quantity=1))

    # Kiểm tra tổng tiền đơn hàng hiện tại
    print(f"\n=> Tổng tiền thanh toán: {service.calculate_total_order():,} VND")