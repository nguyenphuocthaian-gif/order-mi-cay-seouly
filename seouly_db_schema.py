import sqlite3

def setup_seouly_database(db_path="seouly_store.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Kích hoạt kiểm tra khóa ngoại
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Bảng cấp độ cay SpiceLevels (từ 0 đến 7)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SpiceLevels (
        SpiceLevelID INTEGER PRIMARY KEY,
        LevelName TEXT NOT NULL,
        Description TEXT,
        CONSTRAINT CHK_SpiceLevel_Valid CHECK (SpiceLevelID BETWEEN 0 AND 7)
    );
    """)

    # 2. Bảng món ăn Products
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductName TEXT NOT NULL,
        Price REAL NOT NULL CHECK (Price >= 0),
        Category TEXT,
        IsAvailable INTEGER DEFAULT 1,
        DefaultSpiceLevelID INTEGER NULL,
        FOREIGN KEY (DefaultSpiceLevelID) REFERENCES SpiceLevels(SpiceLevelID)
    );
    """)

    # Dữ liệu chuẩn cho 8 cấp độ cay
    levels = [
        (0, 'Cấp độ 0', 'Không cay'),
        (1, 'Cấp độ 1', 'Cay nhẹ'),
        (2, 'Cấp độ 2', 'Cay vừa'),
        (3, 'Cấp độ 3', 'Cay nồng'),
        (4, 'Cấp độ 4', 'Rất cay'),
        (5, 'Cấp độ 5', 'Siêu cay'),
        (6, 'Cấp độ 6', 'Cực đại'),
        (7, 'Cấp độ 7', 'Bùng nổ')
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO SpiceLevels (SpiceLevelID, LevelName, Description) VALUES (?, ?, ?);",
        levels
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_seouly_database()
    print("Da tao xong CSDL Products va SpiceLevels!")