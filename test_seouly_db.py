import unittest
import sqlite3
import os
from seouly_db_schema import setup_seouly_database

class TestSeoulyDatabase(unittest.TestCase):
    def setUp(self):
        # Arrange: Tạo database tạm thời phục vụ kiểm thử
        self.temp_db = "temp_test_seouly.db"
        setup_seouly_database(self.temp_db)
        self.conn = sqlite3.connect(self.temp_db)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")

    def tearDown(self):
        # Dọn dẹp sau khi chạy xong test case
        self.conn.close()
        if os.path.exists(self.temp_db):
            os.remove(self.temp_db)

    def test_total_spice_levels(self):
        # Act: Đếm tổng số cấp độ cay trong bảng
        self.cursor.execute("SELECT COUNT(*) FROM SpiceLevels;")
        total = self.cursor.fetchone()[0]
        # Assert: Bảng phải chứa đủ 8 cấp độ (0-7)
        self.assertEqual(total, 8)

    def test_reject_out_of_range_spice_level(self):
        # Act & Assert: Chặn cấp độ cay ngoài phạm vi 0-7 (ví dụ cấp 8)
        with self.assertRaises(sqlite3.IntegrityError):
            self.cursor.execute(
                "INSERT INTO SpiceLevels (SpiceLevelID, LevelName) VALUES (8, 'Cấp độ 8');"
            )

    def test_add_valid_product(self):
        # Act: Thêm một món mì cay hợp lệ
        self.cursor.execute(
            "INSERT INTO Products (ProductName, Price, Category, DefaultSpiceLevelID) VALUES ('Mì cay Kim Chi Bò', 55000, 'Mì cay', 2);"
        )
        self.cursor.execute("SELECT ProductName, Price FROM Products WHERE ProductName = 'Mì cay Kim Chi Bò';")
        item = self.cursor.fetchone()
        # Assert: Kiểm tra dữ liệu được lưu chính xác
        self.assertIsNotNone(item)
        self.assertEqual(item[0], 'Mì cay Kim Chi Bò')
        self.assertEqual(item[1], 55000)

if __name__ == '__main__':
    unittest.main()